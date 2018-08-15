#!/usr/bin/python3
""" Author: Khuong Nguyen, Vu Le, Tai Le
    Script for controlling 2.0  Inverter"""


import can
import can.interfaces
from can.interface import Bus
from can import Message
import time
import subprocess
import datetime

######## CAN ID ################
TM1_TORQUE_CMD_ID     = 0x47
TM1_TORQUE_PROTECT_ID = 0x41
TM1_STATUS_ID         = 0x153

TM2_TORQUE_CMD_ID     = 0x48
TM2_TORQUE_PROTECT_ID = 0x42
TM2_STATUS_ID         = 0x154

####### Miscellaneous #######
bus = None
counter = 0
counter1 = 0
counter2 = 0
##################################### RDM Class definition ############################################
class RDM:
    def __init__(self,
                 AccPedalPos = 0x50,
                 arc = 0,
                 crc = 0,
                 direction = 'D',
                 legacy_enable_cmd = 'not_enabled',
                 legacy_shutdown_cmd = 'no_shutdown_requested',
                 torque_cmd = 0,
                 torque_protect_val = 1024):
        
        # Initilize signals
        self.direction           = direction
        self.legacy_enable_cmd   = legacy_enable_cmd
        self.legacy_shutdown_cmd = legacy_shutdown_cmd
        self.enable_cmd          = "off"
        self.shutdown_cmd        = "no_cmd"
        self.torque_cmd          = torque_cmd
        self.torque_protect_val  = torque_protect_val
        self.AccPedalPos         = AccPedalPos
        self.arc                 = arc
        self.crc                 = crc
        ######## Inverter Status  ######
        self.TM1_inv_temp_sens   = 9999
        self.TM1_motor_temp_sens = 9999
        self.TM1_pcm_test_fail   = 9999
        self.TM1_status_sig      = 9999
        self.TM1_status_string   = 'None'

        self.TM2_inv_temp_sens   = 9999
        self.TM2_motor_temp_sens = 9999
        self.TM2_pcm_test_fail   = 9999
        self.TM2_status_sig      = 9999
        self.TM2_status_string   = 'None'

        # Initialize message
        self.update_CAN_msg()

#################################   RDM methods ########################################################
    def set_torque(self,target_torque):                            # Change current torque cmd to target torque cmnd
        self.torque_cmd = target_torque
        self.update_CAN_msg()

    def enable(self):                                                 # Send enable command to INV
        self.legacy_shutdown_cmd = "no_shutdown_requested"
        self.shutdown_cmd = "no_cmd"
        time.sleep(0.1)
        self.legacy_enable_cmd = "enabled"
        self.enable_cmd        = "prop_ready"
        self.update_CAN_msg()

        #print('RDM enabled: ',self.legacy_enable_cmd)
        #print('RDM shutdown: ',self.legacy_shutdown_cmd)

    def disable(self):                                                # Send disable command to INV
        self.legacy_enable_cmd = "not_enabled"
        self.enable_cmd = "off"
        time.sleep(0.1)
        self.legacy_shutdown_cmd = "inverter_shutdown_requested"
        self.shutdown_cmd = "shutdown_w_discharge"
        self.update_CAN_msg()

        #print('RDM enabled: ',self.legacy_enable_cmd)
        #print('RDM shutdown: ',self.legacy_shutdown_cmd)

    def change_direction(self,new_direction):                                         # Flip between D -> R
        if new_direction == 'D':
            self.direction = 'D'
        elif new_direction == 'R':
            self.direction = 'R'
        self.update_CAN_msg()


    def get_TM1_status(self,msg):                                      # Pass CAN message in as argument
        self.TM1_inv_temp_sens   = msg.data[0] - 40
        self.TM1_motor_temp_sens = msg.data[1] - 40
        self.TM1_pcm_test_fail   = msg.data[2] >> 6
        self.TM1_status_sig      = (msg.data[2] & 0x3F << 8) | msg.data[3]
        self.TM1_status_string   = self.decode_inv_status(self.TM1_status_sig)
        ####### Testing method #########
        #global counter1
        #if counter1 == 100:
        #    print('TM1 Status: ', self.TM1_status_string, '\n')
        #    counter1 = 0
        #else:
        #    counter1 += 1


    def get_TM2_status(self,msg):                                      # Pass CAN message in as argument
        self.TM2_inv_temp_sens   = msg.data[0] - 40
        self.TM2_motor_temp_sens = msg.data[1] - 40
        self.TM2_pcm_test_fail   = msg.data[2] >> 6
        self.TM2_status_sig      = (msg.data[2] & 0x3F << 8) | msg.data[3]
        self.TM2_status_string   = self.decode_inv_status(self.TM2_status_sig)
        ####### Testing method #########
        #global counter2
        #if counter2 == 100:
        #    print('TM2 Status: ', self.TM2_status_string, '\n')
        #    counter2 = 0
        #else:
        #    counter2 += 1

    def decode_inv_status(self,status):                                     # Pass status signal in as argument
        status2str = {0x1: 'INIT_ECU',
                      0x2: 'INIT_SYS',
                      0x3: 'NORMAL_ENABLE',
                      0x4: 'NORMAL_DISABLE',
                      0x5: 'SHUTDWN',
                      0x6: 'SHUTDWN_ACTIVE_CAP_DISCHARGE',
                      0x7: 'PWR_DWN',
                      0x8: 'FAULT',
                      0x9: 'PCM_ENABLE_TEST',
                      }

        try:
            return status2str[status]
        except:
            return 'Not Available'
            

    def printAll(self):                                # Use for while/for loop only
        global counter
        if counter == 500:
            print('direction:\t',self.direction)
            print('legacy enable:\t',self.legacy_enable_cmd)
            print('legacy shutdown:\t',self.legacy_shutdown_cmd)
            print('torque command:\t',self.torque_cmd)
            print('torque protect value:\t',self.torque_protect_val)
            print('accel pedal sensor:\t',self.AccPedalPos)
            print('arc:\t\t',self.arc)
            print('TM1 torque command msg:\t', self.TM1_torque_cmd_msg)
            print('TM1 torque protect msg:\t', self.TM1_torque_protect_msg)
            print('TM1 status signal:\t',       self.TM1_status_string)
            print('TM2 torque protect msg:\t', self.TM2_torque_protect_msg)
            print('TM2 torque command msg:\t', self.TM2_torque_cmd_msg)
            print('TM2 status signal:\t',       self.TM2_status_string)
            counter = 0
        else:
            counter += 1




    def update_CAN_msg(self):
        cmd2hex = {'R_TM1': 0x5,
                   'R_TM2': 0xA,
                   'D_TM1': 0x0A,
                   'D_TM2': 0x05,
                   # legacy commands
                   'not_enabled': 0x05,
                   'enabled': 0x0A,
                   'no_shutdown_requested': 0x00,
                   'inverter_shutdown_requested': 0x01,
                   # 2.0 commands
                   'prop_ready': 0x03,
                   'off': 0x0,
                   'no_cmd': 0x0,
                   'shutdown_w_discharge': 0x2,
                   }

        
        # Convert input to hex
        if self.direction == 'R':
            self.TM1_direction_hex =  0x5             # CCW
            self.TM2_direction_hex =  0xA             # CW
        elif self.direction == 'D':
            self.TM1_direction_hex =  0x0A            # CW
            self.TM2_direction_hex =  0x05            # CCW

        # legacy commands
        self.legacy_enable_cmd_hex = cmd2hex[self.legacy_enable_cmd]
        self.legacy_shutdown_cmd_hex = cmd2hex[self.legacy_shutdown_cmd]

        # 2.0 commands
        self.enable_cmd_hex = cmd2hex[self.enable_cmd]
        self.shutdown_cmd_hex = cmd2hex[self.shutdown_cmd]
        

        self.arc                    = (self.arc + 1) % 4                                   # rolling counter 0 - 3
        self.torque_cmd_hex         = limit(self.torque_cmd + 1024,0x0,0x7FF)              # torque command
        self.torque_protect_val_hex = self.torque_cmd_hex                                  # torque protect = torque command
        self.torque_env_high_hex    = limit((self.torque_cmd_hex + 0xfa),0x0,0x7FF)
        self.torque_env_low_hex     = limit((self.torque_cmd_hex - 0xfa),0x0,0x7FF)


	############## TM Torque Command bytes ###############
        # Update all messages. Only CRC and Direction signals are different between TM torque_cmd messages. The rest of the signals are exactly the same for both
        # a0: ARC (bit 6-7), shutdown_legacy (bit 3), torque_cmd (MSB bit 0-2)
        #self.a0 =  (self.arc << 6) | (self.legacy_shutdown_cmd_hex << 3) | ((self.torque_cmd_hex & 0x700) >> 8)
        TM1_torque_cmd_bytes = [0] * 7
        TM1_torque_cmd_bytes[0] = getByte(self.arc, [0,1], TM1_torque_cmd_bytes[0], [6,7])
        TM1_torque_cmd_bytes[0] = getByte(self.legacy_shutdown_cmd_hex, [0], TM1_torque_cmd_bytes[0], [3])
        TM1_torque_cmd_bytes[0] = getByte(self.torque_cmd_hex, [8,9,10], TM1_torque_cmd_bytes[0], [0,1,2])

        # a1: Torque_cmd
        #self.a1 =  (self.torque_cmd_hex & 0x0FF)
        TM1_torque_cmd_bytes[1] = getByte(self.torque_cmd_hex, [0,1,2,3,4,5,6,7], TM1_torque_cmd_bytes[1], [0,1,2,3,4,5,6,7])
        
        # a2: Shutdown command (bit 6-7), Enable command (bit 3-5), Torque_protect_val (MSB bit 0-2)
        #self.a2 = ( (self.torque_protect_val_hex & 0x700) >> 8) | self.shutdown_cmd_hex << 6 | self.enable_cmd_hex << 3
        TM1_torque_cmd_bytes[2] = getByte(self.shutdown_cmd_hex, [0,1], TM1_torque_cmd_bytes[2], [6,7])
        TM1_torque_cmd_bytes[2] = getByte(self.enable_cmd_hex, [0,1,2], TM1_torque_cmd_bytes[2], [3,4,5])
        TM1_torque_cmd_bytes[2] = getByte(self.torque_protect_val_hex, [8,9,10], TM1_torque_cmd_bytes[2], [0,1,2])

        # a3: Torque_protect_val
        #self.a3 =  (self.torque_protect_val_hex & 0x0FF)
        TM1_torque_cmd_bytes[3] = getByte(self.torque_protect_val_hex, [0,1,2,3,4,5,6,7], TM1_torque_cmd_bytes[3], [0,1,2,3,4,5,6,7])
        
        # a4: Accel Pedal Pos
        #self.a4 =  self.AccPedalPos
        TM1_torque_cmd_bytes[4] = self.AccPedalPos

        # a5: Enable_legacy (bit 4-7), direction (bit 0-3)
        #self.a5_TM1 =  (self.legacy_enable_cmd_hex << 4) |  self.TM1_direction_hex     #TM1 direction
        #self.a5_TM2 =  (self.legacy_enable_cmd_hex << 4) |  self.TM2_direction_hex     #TM2 direction
        
        TM1_torque_cmd_bytes[5] = getByte(self.legacy_enable_cmd_hex, [0,1,2,3], TM1_torque_cmd_bytes[5], [4,5,6,7])
        TM1_torque_cmd_bytes[5] = getByte(self.TM1_direction_hex, [0,1,2,3], TM1_torque_cmd_bytes[5], [0,1,2,3])

        TM2_torque_cmd_bytes = TM1_torque_cmd_bytes.copy()
        TM2_torque_cmd_bytes[5] = getByte(self.legacy_enable_cmd_hex, [0,1,2,3], TM2_torque_cmd_bytes[5], [4,5,6,7])
        TM2_torque_cmd_bytes[5] = getByte(self.TM2_direction_hex, [0,1,2,3], TM2_torque_cmd_bytes[5], [0,1,2,3])

        # a6: CRC
        TM1_torque_cmd_bytes[6] = crc8(TM1_torque_cmd_bytes[0:-1])
        TM2_torque_cmd_bytes[6] = crc8(TM2_torque_cmd_bytes[0:-1])

        #self.a6_TM1 = crc8([self.a0, self.a1, self.a2, self.a3, self.a4, self.a5_TM1])
        #self.a6_TM2 = crc8([self.a0, self.a1, self.a2, self.a3, self.a4, self.a5_TM2])
        
        ############## TM Torque Command Message ###############
        #old_data1 = [self.a0, self.a1, self.a2, self.a3, self.a4, self.a5_TM1, self.a6_TM1]
        #old_data2 = [self.a0, self.a1, self.a2, self.a3, self.a4, self.a5_TM2, self.a6_TM2]
        
        self.TM1_torque_cmd_msg = can.Message(arbitration_id=TM1_TORQUE_CMD_ID, extended_id=False, data=TM1_torque_cmd_bytes)
        self.TM2_torque_cmd_msg = can.Message(arbitration_id=TM2_TORQUE_CMD_ID, extended_id=False, data=TM2_torque_cmd_bytes)

        
        #print('{} {} {}'.format(old_data1==TM1_torque_cmd_bytes, old_data1, TM1_torque_cmd_bytes))
        #print('{} {} {}'.format(old_data2==TM2_torque_cmd_bytes, old_data2, TM2_torque_cmd_bytes))

        ############## TM Torque Protect bytes ###############
        # b0: arc protect (bit 6-7), torque env high (MSB bit 0-2)
        #self.b0 = (self.arc << 6) | ((self.torque_env_high_hex & 0x700) >> 8)
        TM1_torque_protect_bytes = [0] * 6
        TM1_torque_protect_bytes[0] = getByte(self.arc, [0,1], TM1_torque_protect_bytes[0], [6,7])
        TM1_torque_protect_bytes[0] = getByte(self.torque_env_high_hex, [8,9,10], TM1_torque_protect_bytes[0], [0,1,2])
        
        # b1: torque env high
        #self.b1 = self.torque_env_high_hex & 0x0FF
        TM1_torque_protect_bytes[1] = getByte(self.torque_env_high_hex, [0,1,2,3,4,5,6,7], TM1_torque_protect_bytes[1], [0,1,2,3,4,5,6,7])
        
        # b2: AccPedalPos red
        #self.b2 = self.AccPedalPos
        TM1_torque_protect_bytes[2] = self.AccPedalPos

        # b3: torque env low (MSB bit 0-2)
        #self.b3 =  (self.torque_env_low_hex & 0x700) >> 8
        TM1_torque_protect_bytes[3] = getByte(self.torque_env_low_hex, [8,9,10], TM1_torque_protect_bytes[3], [0,1,2])
        
        # b4: torque env low
        #self.b4 = self.torque_env_low_hex & 0x0FF
        TM1_torque_protect_bytes[4] = getByte(self.torque_env_low_hex, [0,1,2,3,4,5,6,7], TM1_torque_protect_bytes[4], [0,1,2,3,4,5,6,7])
        
        # b5: neutral red (bit 4-7), direction red (bit 0-3)
        #self.b5_TM1 = (0xA << 4) | self.TM1_direction_hex           #always transmitt NEUTRAL
        #self.b5_TM2 = (0xA << 4) | self.TM2_direction_hex
        TM2_torque_protect_bytes = TM1_torque_protect_bytes.copy()
        TM1_torque_protect_bytes[5] = (0xA << 4) | self.TM1_direction_hex           #always transmitt NEUTRAL
        TM2_torque_protect_bytes[5] = (0xA << 4) | self.TM2_direction_hex

        #old_data3 = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5_TM1]
        #old_data4 = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5_TM2]

        ############## TM Torque Command Message ###############
        self.TM1_torque_protect_msg = can.Message(arbitration_id = TM1_TORQUE_PROTECT_ID, extended_id = False, data=TM1_torque_protect_bytes)
        self.TM2_torque_protect_msg = can.Message(arbitration_id = TM2_TORQUE_PROTECT_ID, extended_id = False, data=TM2_torque_protect_bytes)

        #print('{} {} {}'.format(old_data3==TM1_torque_protect_bytes, old_data3, TM1_torque_protect_bytes))
        #print('{} {} {}'.format(old_data4==TM2_torque_protect_bytes, old_data4, TM2_torque_protect_bytes))

#################################   RDM methods END ########################################################

def limit(num,min,max):                 #limit range for torque command or any other command
    if num < max and num > min:
        return num
    elif num < min:
        return min
    elif num > max:
        return max

def crc8(buff):
    crc = 0
    for b in buff:
        crc^= b
        for i in range(7,-1):
            if crc & 0x80:
                crc = (crc << 1) ^ 0x1d
            else:
                crc <<= 1
    return crc

def getByte(sourceByte, sourceIdxRange, destByte, destIdxRange):
    
    def getBit(val, bit):
        return (int((val & (1 << bit)) != 0))

    def setBit(byte, bit, bitval):
        if bitval == 1:
            return (byte | (1 << bit))
        else:
            return (byte & ~(1 << bit))

    
    for s, d in zip(sourceIdxRange, destIdxRange):
        destByte = setBit(destByte, d, getBit(sourceByte, s))

    return destByte


def initCAN():
        global bus
        can.rc['interface'] = 'socketcan'
        can.rc['bitrate'] = 500000
        can.rc['channel'] = 'can0'
        bus = Bus()
        bus.flush_tx_buffer()


if __name__ == "__main__":
    initCAN()
    #def __init__(self,  AccPedalPos = 0x50, arc = 0, crc = 0, direction = 'D', legacy_enable_cmd = 'not_enabled', legacy_shutdown_cmd = 'no_shutdown_requested', torque_cmd = 0, torque_protect_val = 0):
    bunny = RDM()

    ####### Test changing torque command #########
    """while True:

    bus.send(bunny.TM1_torque_cmd_msg)
    #bus.send(bunny.TM2_torque_cmd_msg)
    bunny.enable()
    bus.send(bunny.TM1_torque_cmd_msg)
    #bus.send(bunny.TM2_torque_cmd_msg)
    bunny.change_direction('R')
    for i in range(-2000,2000,10):
        bunny.set_torque(i)
        bus.send(bunny.TM1_torque_cmd_msg)
        #bus.send(bunny.TM2_torque_cmd_msg)
        bus.send(bunny.TM1_torque_protect_msg)
        #bunny.printAll()
    bunny.disable()
    bunny.change_direction('D')
    bus.send(bunny.TM1_torque_cmd_msg)
    bus.send(bunny.TM1_torque_protect_msg)
    #bus.send(bunny.TM2_torque_cmd_msg)"""
    ######## Test enable/disable  ################
    while True:
        bunny.enable()
        #bunny.print_CAN()
        bunny.set_torque(100)
##        bus.send(bunny.TM1_torque_cmd_msg)
##        bus.send(bunny.TM2_torque_cmd_msg)
        time.sleep(5)
        bunny.disable()
##        bus.send(bunny.TM1_torque_cmd_msg)
##        bus.send(bunny.TM2_torque_cmd_msg)
        #bunny.print_CAN()
        time.sleep(5)

    ########### Test reading inverter status #######
    """while True:
        for msg in bus:
            if msg.arbitration_id == TM1_STATUS_ID:
                bunny.get_TM1_status(msg)
            elif msg.arbitration_id == TM2_STATUS_ID:
                bunny.get_TM2_status(msg)
            bunny.printAll()"""
