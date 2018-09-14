#!/usr/bin/python3
""" Author: Khuong Nguyen, Vu Le, Tai Le, Tim Medina
    Script for controlling 2.0  Inverter"""


import can
import can.interfaces
from can.interface import Bus
from can import Message
import time
import subprocess
import datetime
import numpy as np                                                                                                                                                                   

######## CAN ID ################
TM1_TORQUE_CMD_ID     = 0x47
TM1_TORQUE_PROTECT_ID = 0x41
TM1_STATUS_ID         = 0x153
TM1_FEEDBACK_ID       = 0xCA


TM2_TORQUE_CMD_ID     = 0x48
TM2_TORQUE_PROTECT_ID = 0x42
TM2_STATUS_ID         = 0x154
TM2_FEEDBACK_ID       = 0xCB


####### Miscellaneous #######
bus = None

##################################### RDM Class definition ############################################
class RDM:
    def __init__(self):
        
        # Initilize signals
        self.direction           = 'D'
        self.legacy_enable_cmd   = 0x5
        self.legacy_shutdown_cmd = 0x0
        self.enable_cmd          = 0x0
        self.shutdown_cmd        = 0x0
        self.torque_cmd          = 0x0
        self.torque_protect_val  = 0x0
        self.AccPedalPos         = 0x0
        self.arc                 = 0
        self.crc                 = 0

        ######## Inverter Status  ######
        self.TM1_inv_temp_sens   = 9999
        self.TM1_motor_temp_sens = 9999
        self.TM1_pcm_test_fail   = 9999
        self.TM1_status_sig      = 'None'
        self.TM2_inv_temp_sens   = 9999
        self.TM2_motor_temp_sens = 9999
        self.TM2_pcm_test_fail   = 9999
        self.TM2_status_sig      = 'None'

        ######## Inverter Feedback #####
        self.TM1_current_sens    = 9999
        self.TM1_speed_sens      = 9999
        self.TM1_torque_sens     = 9999
        self.TM1_voltage_sens    = 9999
        self.TM2_current_sens    = 9999
        self.TM2_speed_sens      = 9999
        self.TM2_torque_sens     = 9999
        self.TM2_voltage_sens    = 9999

        #### Single/Double Run Mode (0: both TMs, 1: TM1 Only, 2: TM2 Only ####
        self.run_mode = 0    
        # Initialize message
        self.msg_list =[]
        self.update_CAN_msg()

#################################   RDM methods ########################################################
    def set_torque(self,target_torque):                            
        self.torque_cmd = target_torque


    def enable(self,bus):
        # pull WUP2 high
        self.WUP2('ON')
        # no commmand
        self.legacy_shutdown_cmd = 0x0
        self.shutdown_cmd = 0x0
        # enable command
        self.legacy_enable_cmd = 0xA
        # set torque command to zero
        self.set_torque(0)
        # Must enable in the following sequence
        
        enable_seq = [0x0, 0x1, 0x2, 0x3]

        for step in enable_seq:        
            startTime = time.time()
            self.enable_cmd = step
           
            while(True):
                # update in the loop to ensure ARC increment correctly
                self.update_CAN_msg()
                for msg in self.msg_list: 
                    bus.send(msg,0.1)
                time.sleep(0.008)
                if time.time() - startTime > 0.5:
                    break
                
    def WUP2(self,command = 'ON'):
        if command == 'OFF':
        # send logic LOW
            pass
        else:
        # send logic HIGH
            pass
    
    def disable(self,bus):
        # TODO: PULL WUP LINE LOW
        self.WUP2('OFF')
        # set torque command to zero
        self.set_torque(0)
        # disable with the following sequence
        
        disable_seq = [0x3, 0x2, 0x1, 0x0]

        # Wait 0.1 second before transition to next step
        for step in disable_seq:
            startTime = time.time()
            self.enable_cmd = step
            while(time.time() - startTime < 0.1):

                # update in the loop to ensure ARC increment correctly
                self.update_CAN_msg()
                # use try - except to avoid App crashing when tx_buffer overflow 
                try:
                    for msg in self.msg_list:
                        bus.send(msg)
                except:
                    print('...Send CAN bus error...')
                    # clear tx buffer to avoid crashing
                    bus.flush_tx_buffer()
                    return
                time.sleep(0.008)
                
        # After enable_cmd becomes zero, send shutdown request for ab+it more time (2 seconds)
        # shutdown requested
        self.legacy_shutdown_cmd = 0x1
        # shutdown w/ active discharge
        self.shutdown_cmd = 0x2
        # not enabled
        self.legacy_enable_cmd = 0x5       
        while(True):
            # update in the loop to ensure ARC increment correctly
            self.update_CAN_msg()
            for msg in self.msg_list: 
                bus.send(msg,0.1)
            time.sleep(0.008)
            if time.time() - startTime > 2:
                break
        
        # Finally, reset all shutdown command to default value
        self.legacy_enable_cmd   = 0x5
        self.legacy_shutdown_cmd = 0x0
        self.shutdown_cmd = 0x0 


    def set_direction(self,new_direction):                             
        if new_direction == 'D':
            self.direction = 'D'
        elif new_direction == 'R':
            self.direction = 'R'



    def get_inverters_status(self,msg):
        try:
            #print(msg)
            if msg.arbitration_id == TM1_STATUS_ID:
                self.TM1_inv_temp_sens   = msg.data[0] - 40
                self.TM1_motor_temp_sens = msg.data[1] - 40
                self.TM1_pcm_test_fail   = msg.data[2] >> 6
                self.TM1_status_sig      = self.decode_inv_status((msg.data[2] & 0x3F << 8) | msg.data[3])
         
            elif msg.arbitration_id == TM1_FEEDBACK_ID:
                self.TM1_current_sens    =  (((msg.data[6] & 0x1F) << 8 | msg.data[7]) * 0.25) - 1024
                self.TM1_speed_sens      =   ((msg.data[2]         << 8 | msg.data[3]) * 0.5 ) - 16384
                self.TM1_torque_sens     =   ((msg.data[0] & 0x7)  << 8 | msg.data[1])         - 1024
       
            elif msg.arbitration_id == TM2_STATUS_ID:
                self.TM2_inv_temp_sens   = msg.data[0] - 40
                self.TM2_motor_temp_sens = msg.data[1] - 40
                self.TM2_pcm_test_fail   = msg.data[2] >> 6
                self.TM2_status_sig      = self.decode_inv_status((msg.data[2] & 0x3F << 8) | msg.data[3])
              
            elif msg.arbitration_id == TM2_FEEDBACK_ID:
                self.TM2_current_sens    =  (((msg.data[6] & 0x1F) << 8 | msg.data[7]) * 0.25) - 1024
                self.TM2_speed_sens      =   ((msg.data[2]         << 8 | msg.data[3]) * 0.5 ) - 16384
                self.TM2_torque_sens     =   ((msg.data[0] & 0x7)  << 8 | msg.data[1])         - 1024
                self.TM2_voltage_sens    =   ((msg.data[4] & 0xF)  << 8 | msg.data[5]) * 0.25
        except:
                #print('...Read CAN bus error...')
                return
        
            
    def decode_inv_status(self,status):                                     
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
            


    def update_CAN_msg(self):
     
        # Convert input to hex
        if self.direction == 'R':
            self.TM1_direction_hex =  0x5             # CCW
            self.TM2_direction_hex =  0xA             # CW
        elif self.direction == 'D':
            self.TM1_direction_hex =  0x0A            # CW
            self.TM2_direction_hex =  0x05            # CCW

        # legacy commands
        self.legacy_enable_cmd_hex = self.legacy_enable_cmd
        self.legacy_shutdown_cmd_hex = self.legacy_shutdown_cmd

        
        # 2.0 commands
        self.enable_cmd_hex = self.enable_cmd
        self.shutdown_cmd_hex = self.shutdown_cmd
        

        self.arc                    = (self.arc + 1) % 4                                   # rolling counter 0 - 3
        self.torque_cmd_hex         = limit(self.torque_cmd + 1024,0x0,0x7FF)              # torque command
        self.torque_protect_val_hex = self.torque_protect_val                              # torque protect = torque command
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

        #self.TM1_torque_cmd_msg = can.Message(arbitration_id=TM1_TORQUE_CMD_ID, extended_id=False, data=old_data1)
        #self.TM2_torque_cmd_msg = can.Message(arbitration_id=TM2_TORQUE_CMD_ID, extended_id=False, data=old_data2)
        
        self.TM1_torque_cmd_msg = can.Message(arbitration_id=TM1_TORQUE_CMD_ID, extended_id=False, data=TM1_torque_cmd_bytes)
        self.TM2_torque_cmd_msg = can.Message(arbitration_id=TM2_TORQUE_CMD_ID, extended_id=False, data=TM2_torque_cmd_bytes)

    
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

        #self.TM1_torque_protect_msg = can.Message(arbitration_id = TM1_TORQUE_PROTECT_ID, extended_id = False, data=old_data3)
        #self.TM2_torque_protect_msg = can.Message(arbitration_id = TM2_TORQUE_PROTECT_ID, extended_id = False, data=old_data4)


        ############## TM Torque Command Message ###############
        self.TM1_torque_protect_msg = can.Message(arbitration_id = TM1_TORQUE_PROTECT_ID, extended_id = False, data=TM1_torque_protect_bytes)
        self.TM2_torque_protect_msg = can.Message(arbitration_id = TM2_TORQUE_PROTECT_ID, extended_id = False, data=TM2_torque_protect_bytes)


        # Compile to a list to use on GUI code
        if self.run_mode == 0:
            self.msg_list = [self.TM1_torque_cmd_msg,
                             self.TM2_torque_cmd_msg,
                             self.TM1_torque_protect_msg,
                             self.TM2_torque_protect_msg]
        elif self.run_mode == 1:
            self.msg_list = [self.TM1_torque_cmd_msg,
                             self.TM1_torque_protect_msg]
        elif self.run_mode == 2:
            self.msg_list = [self.TM2_torque_cmd_msg,
                                 self.TM2_torque_protect_msg]
        else:
            print ('Invalid run mode')
            
    def assign_id(self,bus,goal_ID = 'GEN'):
        # Use this ID to enable Programming Mode 
        Inv_Diag_Msg_ID = {'TM1'    : 0x781,
                           'TM2'    : 0x782,
                           'GEN'    : 0x780,
                           'DEFAULT': 0x783}
        
        ID_to_name = {1921 :'TM1',
                      1922 :'TM2',
                      1920 :'GEN',
                      1923 :'BOOT'}
        
        # Use this to assign new ID
        B100_Values = {'TM1': 0x1,
                       'TM2': 0x2,
                       'GEN': 0x0}

        curr_ID = None
        b100_resp = []
        prog_pos_resp = False
        b100_pos_resp = False

        # Compile message to enable programming mode regardless of the current ID
        diag_msg_TM1     = can.Message(arbitration_id = Inv_Diag_Msg_ID['TM1'],     extended_id = False, dlc = 8, data=[0x2,0x10,0x2])
        diag_msg_TM2     = can.Message(arbitration_id = Inv_Diag_Msg_ID['TM2'],     extended_id = False, dlc = 8, data=[0x2,0x10,0x2])
        diag_msg_GEN     = can.Message(arbitration_id = Inv_Diag_Msg_ID['GEN'],     extended_id = False, dlc = 8, data=[0x2,0x10,0x2])
        diag_msg_DEFAULT = can.Message(arbitration_id = Inv_Diag_Msg_ID['DEFAULT'], extended_id = False, dlc = 8, data=[0x2,0x10,0x2])
        diag_msg_list = [diag_msg_TM1,diag_msg_TM2,diag_msg_GEN,diag_msg_DEFAULT]
        
        # Enable programming mode on inverter. IMPORTANT: expect only 1 response from the inverter even if 4 msg are sent
        print('...Enabling programming mode...')
        for diag_msg in diag_msg_list:
            bus.send(diag_msg)
            response = bus.recv(timeout = 0.1)
            if response != None:
                curr_ID = diag_msg.arbitration_id
                break
        # Confirm positive response, then send programming command
        print('...Waiting for programing mode response...')
        if response != None:
            if response.data[0] == 0x6 and response.data[1] == 0x50 and response.data[2] == 0x2:
                prog_pos_resp = True
                
            if prog_pos_resp:
                
                print('...{} confirmed Programming Mode. New ID is {}. Writing DID $B100...'.format(ID_to_name[curr_ID],goal_ID))
                diag_msg = can.Message(arbitration_id = curr_ID, extended_id = False, dlc = 8, data=[0x5,0x2E,0xB1,0x0,0x0,B100_Values[goal_ID]])
                bus.send(diag_msg)
                # Confirm positive response. The confirmation comes in the 2nd response from the inverter. Need to save all the response for processing
                print('...Waiting for $B100 response...')
                startTime = time.time()
                while(time.time() - startTime < 0.1):
                    b100_resp.append(bus.recv(0.05))
                    
                if len(b100_resp) != 0:
                    for resp in b100_resp:
                        if resp.data[0] == 0x3 and resp.data[1] == 0x6E and resp.data[2] == 0xB1 and resp.data[3] == 0x0:
                            print('...DID $B100 Written Successfully...\nPlease Cycle Power\n')
                            b100_pos_resp = True           
                else:
                    print('...DID $B100 Not Written...\nPlease Cycle Power And Try Again\n...')
                
        else:
            print('...Programming mode no response...\n')        

#################################   RDM methods END ########################################################

def limit(num,min_num,max_num):                 #limit range for torque command or any other command
    if num < max_num and num > min_num:
        return num
    elif num <= min_num:
        return min_num
    elif num >= max_num:
        return max_num


def crc8(RAW_DATA):
    remainder = np.uint32(0xff)
    CRCResult = 0

    for byte_index in range(0,6):
        remainder = remainder ^ RAW_DATA[byte_index]
        

        for bit_index in range(8,0,-1):
            if remainder & 0x80:
                remainder = (remainder << 1) ^ 0x1d
            else:
                remainder = (remainder << 1)
        
        remainder = np.uint32(remainder) 
        

    CRCResult = ~remainder & 0x00FF
    return CRCResult


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
    rdm = RDM()
    rdm.assign_id(bus,'GEN')
    # For some reason, need 5 second in between calls to print out the right from ID and goal ID
    time.sleep(5)              
    rdm.assign_id(bus,'TM2')
 
