import can
import can.interfaces
from can.interface import Bus
from can import Message
import subprocess
from subprocess import call
from EPB_CRC import *

import datetime

import getByte
import numpy as np
import sched,time
import threading


bus = None
printFlag = False
counter = 0
counter1 = 0
counter2 = 0
counter3 = 0
EPB_STATUS_ID = 0x1B0
All_Node_Request_ID =0x101
AXLE_Torque_Data_ID =0x194
Brake_Status1_ID =0x1B3       # add counter and CRC
Brake_Status_HCU_ID =0x330
CCP1_ID =0x6FD
CCP2_ID =0x6FB
Climate_Status_ID =0x290
Diag_Request_ID =0x756
EBCM_Brake_Torque_ID =0xF5
EPB_Comm_ID =0x1AF
Gear_Position_ID =0x196      # add CRC
HCU_PNM12V_ID =0x432
HCU_Regen_Feedback_ID = 0xC6
HCU2_PT_Status_ID = 0x197
Long_Accel_ID =0x189
Power_Mode_ID =0x104
Vehicle_Speed_ID =0x410        # add counter and CRC
Steering_Angle_ID = 0x180
Time_Status_RTC_ID =0x491
Total_Milage_ID =0x421
Wheel_GND_Driven_ID =0x348     # add counter and CRC
Wheel_GND_Non_Driven_ID =0x34A # add counter and CRC
Wheel_Velocity_ID =0x347       # add counter and CRC
Wheel_Rotat_UNDriven_ID =0xC5  # add counter
Wheel_Rotat_Driven_ID =0xC1    # add counter


class EPBControl(object):
    def __init__(self):
        print('init')
        ## print flag
        self.printFlag = False


        ## EPB status ##
        self.lt_actr_state = ''
        self.rt_actr_state = ''
        self.lt_actr_fault = ''
        self.lt_actr_fault = ''
        self.epb_sw_state  = ''
        self.epb_fault     = ''
        self.pgear         = ''
        self.pbrake        = ''

        ## Cycle time
        self.group1_cycle_time = 0.1
        self.group2_cycle_time = 0.05
        self.group3_cycle_time = 0.01

        self.t1 = threading.Thread(target=self.send_group1, args=())
        self.t1.setDaemon(True)
        self.t2 = threading.Thread(target=self.send_group2, args=())
        self.t2.setDaemon(True)
        self.t3 = threading.Thread(target=self.send_group3, args=())
        self.t3.setDaemon(True)

        ## Build CAN messages
        # Group 1
        self.BrakeStatus1       =  can.Message( arbitration_id =Brake_Status1_ID, extended_id =False,         data =[0x10,0x03,0xC1,0xB9])                                                                                                   
        self.BrakeStatusHCU     =  can.Message( arbitration_id =Brake_Status_HCU_ID, extended_id =False,      data =[0x01,0x00])
        self.ClimateStatus      =  can.Message( arbitration_id =Climate_Status_ID, extended_id =False,        data =[0x0,0x0,0x0,0x0,0x0,0x7A,0x00,0x00])
        self.TotalMilage        =  can.Message( arbitration_id =Total_Milage_ID , extended_id =False,         data =[0x00,0xA0,0x00,0x0])
        self.HCUPNM12V          =  can.Message( arbitration_id =HCU_PNM12V_ID, extended_id =False,            data =[0x00,0x06,0x18,0x00])
        self.EPBCommand         =  can.Message( arbitration_id =EPB_Comm_ID, extended_id =False,              data =[0x00,0x04,0x00])   
        self.GearPosition       =  can.Message( arbitration_id =Gear_Position_ID, extended_id =False,         data =[0x03,0x00,0x00,0x00])
       
        # Group 2
        self.Powermode          =  can.Message( arbitration_id =Power_Mode_ID, extended_id =False,            data =[0x00,0x00,0x00,0x04])

        # Group 3
        self.HCURegenFeedback   =  can.Message( arbitration_id =HCU_Regen_Feedback_ID, extended_id =False,    data =[0x00,0x00,0x0,0x0,0x0,0x0,0x0,0x0])  
        self.HCU2PTStatus       =  can.Message( arbitration_id =HCU2_PT_Status_ID, extended_id =False,        data =[0x38,0x00,0x80,0x00])
        self.LongACCEL          =  can.Message( arbitration_id =Long_Accel_ID, extended_id =False,            data =[0x00,0x0,0x1D])
        self.VehicleSpeed       =  can.Message( arbitration_id =Vehicle_Speed_ID, extended_id =False,         data =[0x00,0x00,0x00,0x0,0x0,0x0,0x00,0x0])
        self.SteeringAngle      =  can.Message( arbitration_id =Steering_Angle_ID, extended_id =False,        data =[0x7F,0xFF,0x00,0x03,0x00])
        self.WheelGDriven       =  can.Message( arbitration_id =Wheel_GND_Driven_ID, extended_id =False,      data =[0x00,0x00,0x00,0x0,0x0,0x0])
        self.WheelGNONDriven    =  can.Message( arbitration_id =Wheel_GND_Non_Driven_ID , extended_id =False, data =[0x00,0x00,0x00,0x00,0x0,0x0])
        self.WheelVelocity      =  can.Message( arbitration_id =Wheel_Velocity_ID, extended_id =False,        data =[0x00,0x00,0x00,0x0])
        self.WheelRotatUnDriven =  can.Message( arbitration_id =Wheel_Rotat_UNDriven_ID, extended_id =False,  data =[0x00,0x00,0x5E,0x2A,0x00,0x00,0x63,0xBF])
        self.WheelRotatDriven   =  can.Message( arbitration_id =Wheel_Rotat_Driven_ID, extended_id =False,    data =[0x00,0x00,0xA4,0x2A,0x00,0x00,0xA4,0xBA])
        self.EBCMBrake          =  can.Message( arbitration_id =EBCM_Brake_Torque_ID, extended_id =False,     data =[0x00,0x03,0xEF,0x0,0x0,0x0,0x0])
        self.AXLETorqueData     =  can.Message( arbitration_id =AXLE_Torque_Data_ID, extended_id =False,      data =[0x0,0x80,0x43,0x80,0x3A,0x00,0x00,0x00])

        # Add messages to list
        self.update_gp1()
        self.update_gp2()
        self.update_gp3()


    def get_epb_status(self,msg):
        try:
            # confirm ID before processing
            if msg.arbitration_id == EPB_STATUS_ID:
                self.lt_actr_state = actuator_state_decode(msg.data[3] & 0x7)
                self.rt_actr_state = actuator_state_decode((msg.data[3] & 0x70) >> 4)
                self.lt_actr_fault = epb_fault_decode((msg.data[3] & 0x8) >> 3)
                self.rt_actr_fault = epb_fault_decode((msg.data[3] & 0x80)>>7)
                self.epb_sw_state  = epb_sw_decode((msg.data[2] & 0xC0)>>6)
                self.epb_fault     = epb_fault_decode((msg.data[0] & 0x30)>>4)
                self.pgear         = actuator_state_decode(msg.data[2] & 0x7)
                self.pbrake        = actuator_state_decode((msg.data[2] & 0x38)>> 3)
        except:
            print('Error reading EPB status')
            return
        
    def epb_sw_decode(data):
        decode = {0: 'Idle', 1: 'Apply', 2: 'Release', 3: 'Fault'}
        return decode[data]
    
    
    def epb_fault_decode(data):
        decode = {0: 'No Fault', 1: 'Fault'}
        return decode[data]
    
    def actuator_state_decode(data):
        decode = {0: 'Unknown', 1: 'Released', 2: 'Applying', 3: 'Releasing', 4: 'Applied'}
        return decode[data]

    def start_threads(self):
        self.t1.start()
        self.t2.start()
        self.t3.start()
        
    def end_threads(self):
        self.t1.join()
        self.t2.join()
        self.t3.join()

   
    def send_group1(self):
        global printFlag
        if printFlag: print('Send group 1...')
        while True:
            try:
                for msg in self.group1_msg_list:
                    bus.send(msg,timeout = 0.01)
                self.update_gp1()
                #time.sleep(0.096)
                time.sleep(0.106)
            except:
                print('Error sending group 1 message...\n')
                break
            
    def send_group2(self):
        global printFlag
        if printFlag: print('Send group 2...')
        while True:
            try:
                for msg in self.group2_msg_list:
                    bus.send(msg, timeout = 0.01)
                self.update_gp2()
                time.sleep(0.047)
            except:
                print('Error sending group 2 message...\n')
                break
            
    def send_group3(self):
        global printFlag
        if printFlag: print('Send group 3...')
        while True:
            try:
                for msg in self.group3_msg_list:
                    bus.send(msg, timeout = 0.01)
                self.update_gp3()
                time.sleep(0.007)
            except:
                print('Error sending group 3 message...\n')
                break
            
    def update_gp1(self):
        # Counter
        global counter
        counter                      = (counter + 1) % 4
        #group 1
        self.BrakeStatus1.data[1]         = (self.BrakeStatus1.data[1]         & 0xF3)  |(counter<<2)
        self.BrakeStatusHCU.data[0]       = (self.BrakeStatusHCU.data[0]       & 0x3F)  |(counter<<6)  
        self.EPBCommand.data[1]           = (self.EPBCommand.data[1]           & 0xFC)  | counter
        self.GearPosition.data[2]         = (self.GearPosition.data[2]         & 0)     |(counter<<6)

        # CRC
        #BrakeStatus1CRC                   = self.crc8(self.BrakeStatus1.data[:2],2)
        BrakeStatus1CRC                   = crc8_PTECT_BRAKE_STATUS_TRAVEL(self.BrakeStatus1)
        self.BrakeStatus1.data[1]         = self.BrakeStatus1.data[1] & 0xFC | ((BrakeStatus1CRC & 0x300) >> 8)
        self.BrakeStatus1.data[2]         = (BrakeStatus1CRC & 0x0FF)
        
        #self.EPBCommand.data[0]           = self.crc8(self.EPBCommand.data[1:],2)
        self.EPBCommand.data[0]           = crc8(self.EPBCommand,0)    

        #self.BrakeStatusHCU.data[1]       = self.crc8(self.BrakeStatusHCU.data[0],1)
        self.BrakeStatusHCU.data[1]       = crc8(self.BrakeStatusHCU,1)

        #self.GearPosition.data[3]         = self.crc8(self.GearPosition.data[0:3],3)
        self.GearPosition.data[3]         = crc8(self.GearPosition,3)

        
        self.group1_msg_list    = [self.BrakeStatus1, self.BrakeStatusHCU, self.ClimateStatus, self.TotalMilage, self.HCUPNM12V, self.EPBCommand, self.GearPosition ]

          
    def update_gp2(self):
        global counter2
        counter2 = (counter2+ 1) % 256
        #group 2
        self.Powermode.data[0]      = (self.Powermode.data[0]    & 0)     | counter2
        self.group2_msg_list        = [self.Powermode]
                                     

        
    def update_gp3(self):
        # Counter
        global counter3
        global counter1
        
        counter3                     = (counter3 + 1) % 4
        counter1                     = (counter1+ 1) % 16
        #group 3
        self.HCURegenFeedback             = self.HCUREGENFEEDBACK(self.HCURegenFeedback)
        
        self.HCURegenFeedback.data[0]     = (self.HCURegenFeedback.data[0]     & 0)     | counter3
        self.HCU2PTStatus.data[1]         = (self.HCU2PTStatus.data[1]         & 0)     | counter3
        self.LongACCEL.data[0]            = (self.LongACCEL.data[0]            & 0)     | counter1
        self.VehicleSpeed.data[6]         = (self.VehicleSpeed.data[6]         & 0)     | counter1
        self.SteeringAngle.data[4]        = (self.SteeringAngle.data[4]        & 0xF0)  | counter1
        self.WheelGDriven.data[4]         = (self.WheelGDriven.data[4]         & 0)     | counter3
        self.WheelGNONDriven.data[4]      = (self.WheelGNONDriven.data[4]      & 0)     | counter3
        self.WheelVelocity.data[2]        = (self.WheelVelocity.data[2]        & 0)     | counter3
        self.WheelRotatUnDriven.data[0]   = (self.WheelRotatUnDriven.data[0]   & 0x3F)  |(counter3<<6)                            
        self.WheelRotatDriven.data[0]     = (self.WheelRotatDriven.data[0]     & 0x3F)  |(counter3<<6)
        self.EBCMBrake.data[0]            = (self.EBCMBrake.data[0]            & 0)     | counter3
        self.AXLETorqueData.data[0]       = (self.AXLETorqueData.data[0]       & 0xFC)  | counter3
        
        # CRC
        EBCMBrakeTorqueCRC              = crc8_PTECT_DRIV_INTEND_BRAKE_TORQ(self.EBCMBrake)
        self.EBCMBrake.data[5]          = (EBCMBrakeTorqueCRC & 0xF0) >> 8
        self.EBCMBrake.data[6]          = EBCMBrakeTorqueCRC & 0x0F

        self.HCU2PTStatus.data[0]         = crc8(self.HCU2PTStatus,0)
        self.VehicleSpeed.data[7]         = crc8(self.VehicleSpeed,7)
        self.WheelGDriven.data[5]         = crc8(self.WheelGDriven,5)
        self.WheelGNONDriven.data[5]      = crc8(self.WheelGNONDriven,5)
        self.WheelVelocity.data[3]        = crc8(self.WheelVelocity,3)


        
        self.group3_msg_list    = [self.HCURegenFeedback, self.HCU2PTStatus, self.LongACCEL, self.VehicleSpeed, self.SteeringAngle, self.WheelGDriven,
                               self.WheelGNONDriven, self.WheelVelocity, self.WheelRotatUnDriven, self.WheelRotatDriven, self.EBCMBrake,self.AXLETorqueData]
   
  
      

    def HCUREGENFEEDBACK(self, msg):
        curr_num = msg.data[6] << 8 |msg.data[7] # reading the message(combine byte 6 and 7)
        if curr_num == 0: # byte 6 and 7 follow this pattern below.
            curr_num = 65535
        elif curr_num == 65535:
            curr_num = 65534
        elif curr_num == 65534:
            curr_num = 65533
        elif curr_num == 65533:
            curr_num = 0

        msg.data[6] = (curr_num & 0xFF00) >> 8
        msg.data[7] = (curr_num & 0xFF)
    
        return msg

    def initCAN(self):
        # Initial can0
        call('sudo ip link set can0 up', shell=True)
        global bus
        can.rc['interface'] ='socketcan_native'
        can.rc['bitrate'] = 500000
        can.rc['channel'] ='can0'
        bus = Bus()

    
if __name__== '__main__':

    EPB = EPBControl()
    EPB.initCAN()
    EPB.printFlag = False
    EPB.start_threads()
    ##EPB.end_threads()

        
