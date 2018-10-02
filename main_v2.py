""" Author: Khuong Nguyen, Vu Le
    2.0 RDM Application Script"""


from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QTimer
import sys

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
from inv_control_v2 import *
from PS_Control import *

# Flags
TransmitFlag = False
EnableFlag   = False                                                                                                                                   
ReadFlag     = False
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

        
        # Show default vehicle in test number
        self.veh_num_label.setText(str(vehicle_in_test_num))
        # Change vehicle number
        self.veh_num_down.clicked.connect      (lambda:self.veh_num_down_func())
        self.veh_num_up.clicked.connect        (lambda:self.veh_num_up_func())
        self.veh_num_save_btn.clicked.connect  (lambda:self.veh_num_save())

        # Page switch
        self.epbBtn.clicked.connect             (lambda:self.change_page('EPB page'))
        self.rdmBtn.clicked.connect             (lambda:self.change_page('RDM page'))
        self.menuBtn.clicked.connect            (lambda:self.change_page('Operator page'))
    
        # Pop Up meassage box
        self.CAN_adapter_msg = QMessageBox()
        self.CAN_adapter_msg.setIcon(QMessageBox.Critical)
        self.CAN_adapter_msg.setText('CAN bus can not be found.')
        self.CAN_adapter_msg.setInformativeText('Please check PEAK CAN adapter and try again.')
        self.CAN_adapter_msg.setWindowTitle("PEAK CAN connection")
        self.CAN_adapter_msg.setStyleSheet('background-color: rgb(59, 56, 56)')
        self.CAN_adapter_msg.setStandardButtons(QMessageBox.Retry| QMessageBox.Abort)        
        self.CAN_adapter_msg.buttonClicked.connect(self.msgBtn)

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

    def veh_num_down_func(self):
        global vehicle_in_test_num
        vehicle_in_test_num =  limit(vehicle_in_test_num - 1,0,1000)
        self.veh_num_label.setText(str(vehicle_in_test_num))

    def veh_num_save(self):
        global vehicle_in_test_num
        print('Vehicle in test number: {}'.format(vehicle_in_test_num))
        # When test a new vehicle, reset num of test performed
        global num_test_performed
        num_test_performed = 0
        # Close any opened log session and write to file
        logger.stop()
        # Start a new log file
        create_log()
        

    def msgBtn(self):
        ret = self.CAN_adapter_msg.exec_()

    def change_page(self,target = 'EPB page'):
        pages = {'EPB page': self.EPB_page, 'RDM page': self.RDM_page,'Operator page': self.Operator_page}
        self.stackedWidget.setCurrentWidget(pages[target])

    def profile_test(self,test = 1):
        if test == 1:
            ## Start RDM, run for 10 seconds, Stop
            pass
        if test == 2:
            pass
        
                
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
            self.tm1StatusBox.setText(self.rdm.TM1_status_sig)
            self.tm2StatusBox.setText(self.rdm.TM2_status_sig)
            self.tm1_temp_LCD.display(self.rdm.TM1_inv_temp_sens)
            self.tm2_temp_LCD.display(self.rdm.TM2_inv_temp_sens)
            
  
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
        EnableFlag = True
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
                if EnableFlag:
                    self.rdm.enable(bus, logger, Tx_Rx_Timestamp_offset, msg2str)
                    # Set torque value to 10
                    self.rdm.set_torque(torque_value)
                    EnableFlag = False
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
        print ("Disable RDM...")
        EnableFlag = False

        # Set this flag to stop the ongoing transmittion
        print ("Stop CAN transmit...")
        TransmitFlag = False
        self.rdm.disable(bus, logger, Tx_Rx_Timestamp_offset, msg2str)

        # Turn OFF PS output
        power_supply_control(output = 'OFF', voltage = 0.1, current  = 0.1)


        # Set this flag to stop reading  inverter status
        #print ("Stop CAN read..")
        #ReadFlag = False
        
        # Dont stop reading status
        #notifier.stop()
        #listener.stop()
        

        # Wait for threads termination
        print ("Stop Transmit & Read CAN threads...")
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
    file_name = create_file_name(vehicle_in_test_num,num_test_performed)
    # Check if path to storage is valid
    if not path.exists(path_to_storage):
        print('"{}" is not a valid path. Please try again'.format(path_to_storage))
    # Change path according to locations of log files
    while path.exists('{}/{}'.format(path_to_storage,file_name)) :
        # file already exists, increase num_test_performed by 1
        num_test_performed = num_test_performed + 1
        file_name = create_file_name(vehicle_in_test_num,num_test_performed)
    logger  = can.ASCWriter('{}/{}'.format(path_to_storage,file_name))
    listener = can.BufferedReader()
    notifier = can.Notifier(bus, [listener,logger])
    print('log file {} is created'.format(file_name))
              
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
