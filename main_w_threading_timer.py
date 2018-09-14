""" Author: Khuong Nguyen, Vu Le
    2.0 RDM Application Script"""


from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import sys,os

# system import
import threading
import re
import logging

import visa
import os.path
from os import path
from subprocess import call

# import the file with EPB page
from rdm_gui_stackedpages import *
#from inv_control_v2 import *
from inv_control_w_theading_timer import *
from PS_Control import *

# Flags
TransmitFlag = False
EnableFlag   = False                                                                                                                                   
ReadFlag     = False
TM1_Fault_Flag = False
TM2_Fault_Flag = False
Test_Result    = None
# CAN objects 
bus         = None
listener    = None
notifier    = None
lock        = None
timer       = None
logger      = None
PEAK_CAN_connected = 1   # 1 is not connected 

torque_value = 10
vehicle_in_test_num = 0
num_test_performed = 0
Tx_Rx_Timestamp_offset = None
duration           =  20
file_name          = None
form            = None
#path_to_storage     = '/home/pi/rdm_bench/RDM_logs'
path_to_storage     = '/mnt/Sdrive'

#logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)


class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Show default torque cmd value
        global torque_value
        self.torqueCmdBox.setText('{} Nm'.format(torque_value))
  
        # Buttons
        self.enableBtn.setEnabled(False)
        self.Both_radio_btn.setChecked(True)
        self.radio_btns = [self.Both_radio_btn, self.TM1_radio_btn, self.TM2_radio_btn]
        
        # Create RDM object
        self.rdm = RDM()

        # Event handlers
        self.startStopBtn.clicked.connect       (lambda:self.start_CAN_thread())
        self.enableBtn.clicked.connect          (lambda:self.enable_RDM())
        self.torqueCmdMinus.clicked.connect     (lambda:self.minus_torque())
        self.torqueCmdPlus.clicked.connect      (lambda:self.plus_torque())
        self.Both_radio_btn.clicked.connect     (lambda:self.run_mode(0))
        self.TM1_radio_btn.clicked.connect      (lambda:self.run_mode(1))
        self.TM2_radio_btn.clicked.connect      (lambda:self.run_mode(2))
        self.profile_test_btn.clicked.connect   (lambda:self.profile_test(1))
        
        # Show default vehicle in test number
        # RDM Page
        self.veh_num_label.setText(str(vehicle_in_test_num))
        # Operator Page
        self.op_veh_num_label.setText(str(vehicle_in_test_num))
        

        # Progress bar
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(duration)
        self.progressBar.hide()
        
        # Change vehicle number
        # RDM Page
        self.veh_num_down.clicked.connect      (lambda:self.veh_num_down_func())
        self.veh_num_up.clicked.connect        (lambda:self.veh_num_up_func())
        self.veh_num_save_btn.clicked.connect  (lambda:self.veh_num_save())
        # Operator Page
        self.op_veh_num_down.clicked.connect      (lambda:self.veh_num_down_func())
        self.op_veh_num_up.clicked.connect        (lambda:self.veh_num_up_func())
        self.op_veh_num_save_btn.clicked.connect  (lambda:self.veh_num_save())

        # Default page
        self.change_page('RDM page')

        # Page switch
        self.epbBtn.clicked.connect             (lambda:self.change_page('EPB page'))
        self.rdmBtn.clicked.connect             (lambda:self.change_page('RDM page'))
        self.menuBtn.clicked.connect            (lambda:self.change_page('Operator page'))
        self.op_epbBtn.clicked.connect          (lambda:self.change_page('EPB page'))
    
        # Pop Up meassage box
        self.CAN_adapter_msg = QMessageBox()
        self.CAN_adapter_msg.setIcon(QMessageBox.Critical)
        self.CAN_adapter_msg.setText('CAN bus can not be found.')
        self.CAN_adapter_msg.setInformativeText('Please check PEAK CAN adapter and try again.')
        self.CAN_adapter_msg.setWindowTitle("PEAK CAN connection")
        self.CAN_adapter_msg.setStyleSheet('background-color: rgb(59, 56, 56)')
        self.CAN_adapter_msg.setStandardButtons(QMessageBox.Retry| QMessageBox.Abort)        
        self.CAN_adapter_msg.buttonClicked.connect(self.msgBtn)

        # LED indicator for Operator Page
        self.green_led = QPixmap('graphics/green_led.png')
        self.red_led = QPixmap('graphics/red_led.png')
        self.grey_led = QPixmap('graphics/grey_led.png')
        # default LED
        self.LED.setPixmap(self.grey_led)

        # Check PEAK CAN connection
        global PEAK_CAN_connected
        check_PEAK_CAN_connection()
        while PEAK_CAN_connected == 1:
            ret = self.CAN_adapter_msg.exec_()
            if ret == 0x40000:
                # Abort
                exit()
            # if PEAK CAN is connected, loop will exit
            check_PEAK_CAN_connection()
        # Confirmed connection. Initialize CAN bus
        initCAN()
        
    #######################################        
    ############# GUI methods #############           
    #######################################



    def veh_num_up_func(self):
        global vehicle_in_test_num
        vehicle_in_test_num =  limit(vehicle_in_test_num + 1,0,1000)
        self.veh_num_label.setText(str(vehicle_in_test_num))
        self.op_veh_num_label.setText(str(vehicle_in_test_num))
    def veh_num_down_func(self):
        global vehicle_in_test_num
        vehicle_in_test_num =  limit(vehicle_in_test_num - 1,0,1000)
        self.veh_num_label.setText(str(vehicle_in_test_num))
        self.op_veh_num_label.setText(str(vehicle_in_test_num))

    def veh_num_save(self):
        global vehicle_in_test_num
        global Test_Result
        global file_name
        print('Vehicle in test number: {}'.format(vehicle_in_test_num))
        # When test a new vehicle, reset num of test performed
        global num_test_performed
        num_test_performed = 0
        # Close any opened log session and write to file
        logger.stop()
        # Append FAILED to file name if Test failed
        if Test_Result == 'FAILED':
            os.rename(file_name, 'FAILED_' + file_name)
            Test_Result = None
        # Start a new log file
        status = create_log()
        # Update status box on RDM page
        self.save_file_status.setText(status)
        # Update status box on Operator page
        self.op_save_file_status.setText(status)

        

    def msgBtn(self):
        ret = self.CAN_adapter_msg.exec_()

    def change_page(self,target = 'EPB page'):
        pages = {'EPB page': self.EPB_page, 'RDM page': self.RDM_page,'Operator page': self.Operator_page, 'Assign ID page': self.Assign_ID_page}
        self.stackedWidget.setCurrentWidget(pages[target])

    def profile_test(self,test = 1):
        if test == 1:
            # Start Tx and Rx thread
            self.start_CAN_thread()
            # Start another thread to run autotest and prevent read thread frozen
            ## Start RDM, run for 15 seconds, Stop ##
            auto_test_thread = threading.Timer(duration,self.complete_test)
            auto_test_thread.daemon = True
            print('Start auto test')
            # Auto test LED default to grey
            self.LED.setPixmap(self.grey_led)
            auto_test_thread.start()
            # NOTE: For some reason, auto test causes the SSB on the Engineer Control Page to disconnect
            #       and does not reconnect to start_CAN_thread(). Need to restart the application to fix
            #       DONT USE BOTH PAGE IN THE SAME SESSION FOR NOW
            
            # Set Enable in 1 seconds
            enable_thread = threading.Timer(1,self.enable_RDM)
            enable_thread.daemon = True
            enable_thread.start()

            # Start progress bar
            show_progress_thread = threading.Thread(target=self.show_progress, args=())
            show_progress_thread.daemon = True
            show_progress_thread.start()

            
    def complete_test(self):
        print('End auto test')

        global TM2_Fault_Flag
        global TM1_Fault_Flag
        global Test_Result
        
        # Auto Test LED 
        if TM1_Fault_Flag == True or TM2_Fault_Flag == True:
            self.LED.setPixmap(self.red_led)
            Test_Result = 'FAILED'
            # reset flag for next run
            TM1_Fault_Flag = False
            TM2_Fault_Flag = False
        elif self.rdm.TM1_status_sig == 'NORMAL_ENABLE' and abs(self.rdm.TM1_speed_sens) < 10:
            self.LED.setPixmap(self.red_led)
            Test_Result = 'FAILED'
        elif self.rdm.TM2_status_sig == 'NORMAL_ENABLE' and abs(self.rdm.TM2_speed_sens) < 10:
            self.LED.setPixmap(self.red_led)
            Test_Result = 'FAILED'
        elif self.rdm.TM1_status_sig == 'SHUTDWN' or self.rdm.TM2_status_sig == 'SHUTDWN':
        # if this signal is shutdown before disable cmd is sent. that means it failed the test
            self.LED.setPixmap(self.red_led)
            Test_Result = 'FAILED'
        else:
            self.LED.setPixmap(self.green_led)
            Test_Result = 'PASSED'
            
        # Stop RDM
        self.stop_transmit()

    def show_progress(self):
        # show progress bar
        self.progressBar.show()
        # progress increasing for 15 seconds
        self.completed = 0
        while self.completed < duration:
            self.completed = self.completed + 1 
            self.progressBar.setValue(self.completed)
            time.sleep(1)
        self.progressBar.reset()
        self.progressBar.hide()

    def run_mode(self,mode):
        global EnableFlag
        if EnableFlag != True:
            self.rdm.run_mode = mode
            print('Run Mode Changed')

        
    def set_radio_btns_state(self, state = 'unlocked'):
        for btn in self.radio_btns:
            if state == 'locked':
                btn.setEnabled(False)
            elif state == 'unlocked':
                btn.setEnabled(True)
        print("Mode buttons are {}...\n".format(state))

           
    def minus_torque(self):
        global torque_value
        # Decrease torque command by 1 and ensure it is within (0,14)
        torque_value = limit(torque_value - 1, 0, 14)   
        self.rdm.set_torque(torque_value)
        # Update torque display
        self.torqueCmdBox.setText('{} Nm'.format(torque_value))
        print('Torque command: {}'.format(torque_value))

    def plus_torque(self):
        global torque_value
       
        # Increase torque command by 1 and ensure it is within (0,14)
        torque_value = limit(torque_value + 1, 0, 14)   
        self.rdm.set_torque(torque_value)
        # Update torque display
        self.torqueCmdBox.setText('{} Nm'.format(torque_value))
        print('Torque command: {}'.format(torque_value))
                    
    def update_gui(self):
        #print('Updating GUI...\n')
        global lock
        with lock:
            # Update RDM page 
            self.tm1StatusBox.setText(self.rdm.TM1_status_sig)
            self.tm2StatusBox.setText(self.rdm.TM2_status_sig)
            self.tm1_temp_LCD.display(self.rdm.TM1_inv_temp_sens)
            self.tm2_temp_LCD.display(self.rdm.TM2_inv_temp_sens)
            self.tm1_motor_rpm_LCD.display(abs(self.rdm.TM1_speed_sens))
            self.tm2_motor_rpm_LCD.display(abs(self.rdm.TM2_speed_sens))
            # Update Operator Page
            self.op_tm1StatusBox.setText(self.rdm.TM1_status_sig)
            self.op_tm2StatusBox.setText(self.rdm.TM2_status_sig)
            self.op_tm1_inv_temp_LCD.display(self.rdm.TM1_inv_temp_sens)
            self.op_tm2_inv_temp_LCD.display(self.rdm.TM2_inv_temp_sens)
            self.op_tm1_motor_rpm_LCD.display(abs(self.rdm.TM1_speed_sens))
            self.op_tm2_motor_rpm_LCD.display(abs(self.rdm.TM2_speed_sens))
            
    def reset_gui(self):
        print('Reset GUI...\n')
        # reset torque command box
        global torque_value
        self.torqueCmdBox.setText('{} Nm'.format(torque_value))

        # reset SSB 
        self.startStopBtn.setText('Start')
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.start_CAN_thread())

        # reset enable button
        self.enableBtn.setEnabled(False)

        # reset radio button
        self.set_radio_btns_state('unlocked')


                                  
    #######################################        
    ############# CAN methods #############           
    #######################################
        

    def enable_RDM(self):
        print("Enable RDM...")
        global EnableFlag
        global torque_value
        # Turn ON HV Power Supply Output
        power_supply_control(output = 'ON', voltage = 340, current = 1.5)
        # Enable RDM
        self.rdm.enable()
        self.rdm.set_torque(torque_value)

        # change button to disabled mode
        self.enableBtn.setEnabled(False)

    def start_transmit(self):
        print("Start CAN transmit...\n")
        global TransmitFlag
        global bus
        global torque_value
        global cycle_time
        global EnableFlag 
        global logger
        global Tx_Rx_Timestamp_offset
        
        epoch = time.time()
        
        # May need to change when adding processing time between Rx and Tx
        # Take the time stamp of 1 Rx message for reference
        sample_rx = bus.recv(timeout = 0.05)
        if sample_rx is None:
            # An average delay
            Tx_Rx_Timestamp_offset = 22
        else:
            # CAN time stamp is recorded time since EPOCH. Therefore we need to recalculate the offset
            Tx_Rx_Timestamp_offset = sample_rx.timestamp - epoch
            
        # Unlock Enable Button
        self.enableBtn.setEnabled(True)

        # Lock Run Mode radio btns
        self.set_radio_btns_state('locked')
       
        # Send CAN continously
        while(TransmitFlag):
            try:
                self.rdm.update_CAN_msg()               
                for msg in self.rdm.msg_list:
                    bus.send(msg,0.1)
                    # Logging Tx message
                    line = msg2str(msg)
                    logger.log_event(line,timestamp = time.time() + Tx_Rx_Timestamp_offset)
                # Send messages every 10 ms    
                time.sleep(0.007)

            except:
                print('Unable to send on CAN bus...\n')
                break
       

    def start_read(self):
        print('Start CAN read...')
        global ReadFlag
        global TM2_Fault_Flag
        global TM1_Fault_Flag
        global listener
        global notifier
        global lock
        while(ReadFlag):
            try:
                msg = listener.get_message(timeout = 0.05)
                with lock:
                    self.rdm.get_inverters_status(msg)
            except:
                print('Unable to read on CAN bus')
                
            # Check for inverter fault
            if self.rdm.TM1_status_sig == 'FAULT': TM1_Fault_Flag = True
            if self.rdm.TM2_status_sig == 'FAULT': TM2_Fault_Flag = True

    def start_CAN_thread(self):
        global TransmitFlag
        TransmitFlag = True

        global ReadFlag
        ReadFlag = True


        # change SSB text to STOP
        self.startStopBtn.setText('Stop')
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.stop_transmit())

         
        # separate thread to prevent gui freezing. PASS HANDLE NOT FUNCTION CALL
        print("Start Transmit & Read CAN threads...")
        global send_thread
        global read_thread
        
        send_thread = threading.Thread(target=self.start_transmit, args=())
        send_thread.setName('Send Thread')
        send_thread.daemon = True
        send_thread.start()                

        read_thread = threading.Thread(target=self.start_read, args=())
        read_thread.setName('Read Thread')
        read_thread.daemon = True
        read_thread.start()

    def stop_transmit(self):
        global TransmitFlag
        global EnableFlag
        global ReadFlag
        global bus
        global notifier
        global listener
        global timer
        global logger
        global Tx_Rx_Timestamp_offset
        
        # Set this flag to  disable RDM
        self.rdm.disable()


        # Set this flag to stop the ongoing transmittion
        print ("Stop CAN transmit...")
        TransmitFlag = False

        # Turn OFF PS output
        power_supply_control(output = 'OFF', voltage = 0.1, current  = 0.1)


        # Set this flag to stop reading  inverter status
        #print ("Stop CAN read..")
        #ReadFlag = False
        
        # Dont stop reading status
        #notifier.stop()
        #listener.stop()
        

        # Wait for threads termination
        #print ("Stop Transmit threads...")
        global send_thread
        global read_thread
        send_thread.join()
        # Should not stop thread. Continue reading status
        #read_thread.join()

        # Dont shutdown bus to let operator do multiple cycle
        #bus.shutdown()
        bus.flush_tx_buffer()

        # reset GUI
        self.reset_gui()

        

                                  
    #######################################        
    ############# Main functions ##########          
    #######################################

def check_PEAK_CAN_connection():
    global PEAK_CAN_connected
    # 1 means no can0. prompt user for exit/retry and wait for input
    PEAK_CAN_connected = call("sudo ip link set can0 up", shell=True)

 

def initCAN():
    global form
    # Initilize bus
    global bus
    can.rc['interface'] = 'socketcan'
    can.rc['bitrate'] = 500000
    can.rc['channel'] = 'can0'
    bus = Bus()
    bus.flush_tx_buffer()

    # Logging 
    create_log()


def create_file_name(vehicle_number = 0, num_test_performed = 0):
    file_name = 'PV{:02d}.{:d}.asc'.format(vehicle_number,num_test_performed)
    return file_name


def create_log():
    global vehicle_in_test_num
    global num_test_performed 
    global path_to_storage
    global logger
    global listener
    global notifier
    global file_name
    file_name = create_file_name(vehicle_in_test_num,num_test_performed)
    # Check if path to storage is valid
    if not path.exists(path_to_storage):
        msg = '"{}" is not a valid path. Please try again'.format(path_to_storage)
    else:
        # Change path according to locations of log files
        while path.exists('{}/{}'.format(path_to_storage,file_name)) :
            # file already exists, increase num_test_performed by 1
            num_test_performed = num_test_performed + 1
            file_name = create_file_name(vehicle_in_test_num,num_test_performed)
        logger  = can.ASCWriter('{}/{}'.format(path_to_storage,file_name))
        listener = can.BufferedReader()
        notifier = can.Notifier(bus, [listener,logger])
        msg = 'log file {} is created'.format(file_name)
    return msg
              
def msg2str(msg):
    ID = msg.arbitration_id
    c = 1
    dlc = msg.dlc
    data = msg.data
    data_str = ''
    for d in data:
        data_str = data_str +'{:02x} '.format(d)
    line =  '{}  {:03x}             Tx   d {} '.format(c,ID,dlc) + data_str
    return line


def numberFromString(string):
    # this return a list of number from the string
    numbers = re.findall('\d+',string)
    # convert to integer
    numbers = [int(num) for num in numbers]
    # just need to access the first item
    return numbers[0]                

    #######################################        
    ######Power Supply functions ##########          
    #######################################

def power_supply_control(output , voltage , current):
    try:
        rm = visa.ResourceManager('@py')
        inst = rm.open_resource('USB0::2391::43271::US17M5344R::0::INSTR') 

        ## Print for debug ##
        PSwrite(inst,'VSET', voltage)
        PSwrite(inst,'CSET', current)
        PSwrite(inst,'ON')

        PSwrite(inst, output)
    except:
        print('Power Supply not found. Please check and try again')

def main():
    global form
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    #form.showFullScreen()   

    # Mount S Drive
    call('sudo mount -t cifs -o username=RDM_Bench,password="AqAErT4AJ@&Rq6KQ",sec=ntlmsspi //fafs02/Engineering/Khuong\ Nguyen/Raspberry\ Pi /mnt/Sdrive', shell=True)
    
    ## Thread Rlock for thread safety for
    ## read/write status to GUI
    global lock
    lock = threading.RLock()

    ## QTimer for updating GUI every second ##
    ## Timer need to start in Main Thread i.e in main()
    timer = QTimer()
    timer.timeout.connect(form.update_gui)
    timer.start(500)

    ## Start App ##
    app.exec_()
	
if __name__ == '__main__':
    main()
