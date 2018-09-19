""" Author: Khuong Nguyen, Vu Le
    2.0 RDM Application Script"""


from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QTimer
import sys

import os.path
from os import path

from rdm_gui import *
from inv_control_v2 import *
import threading
import re
import logging


TransmitFlag = False
EnableFlag   = False                                                                                                                                   
ReadFlag     = False

bus         = None
listener    = None
notifier    = None
lock        = None
timer       = None
logger      = None

torque_value = 10
vehicle_in_test_num = 0


#logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)


class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Show default torque cmd value
        global torque_value
        self.torqueCmdBox.setText('{} Nm'.format(torque_value))
        # Show default vehicle in test number
        global vehicle_in_test_num
        self.vehicle_number.setValue(vehicle_in_test_num)

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
        self.vehicle_number.valueChanged.connect(lambda:self.veh_num_change())

        
        # Pop Up meassage box
        self.mode_msg_box = QMessageBox()
        self.mode_msg_box.setIcon(QMessageBox.Information)
        self.mode_msg_box.setText('RDM is running!')
        self.mode_msg_box.setInformativeText('Please Stop RDM and try again.')
        self.mode_msg_box.setWindowTitle("Run Mode Message")
        self.mode_msg_box.setStyleSheet('background-color: rgb(59, 56, 56)')
        self.mode_msg_box.setStandardButtons(QMessageBox.Close)        
        
    #######################################        
    ############# GUI methods #############           
    #######################################
    def veh_num_change(self):
        global vehicle_in_test_num
        vehicle_in_test_num = self.vehicle_number.value()
        print('Vehicle in test number: {}'.format(vehicle_in_test_num))
                
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
        print('Torque command minus 1...')
        # Decrease torque command by 1 and ensure it is within (0,14)
        torque_value = limit(torque_value - 1, 0, 14)   
        self.rdm.set_torque(torque_value)
        # Update torque display
        self.torqueCmdBox.setText('{} Nm'.format(torque_value))

    def plus_torque(self):
        global torque_value
        print('Torque command plus 1...')
        # Increase torque command by 1 and ensure it is within (0,14)
        torque_value = limit(torque_value + 1, 0, 14)   
        self.rdm.set_torque(torque_value)
        # Update torque display
        self.torqueCmdBox.setText('{} Nm'.format(torque_value))

                    
    def update_gui(self):
        #print('Updating GUI...\n')
        global lock
        with lock:
            self.tm1StatusBox.setText(self.rdm.TM1_status_sig)
            self.tm2StatusBox.setText(self.rdm.TM2_status_sig)
            self.rpmLCD.display(self.rdm.TM1_speed_sens)
            self.torqueLCD.display(self.rdm.TM1_torque_sens)
            
  
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

        line = ''
        Tx_Rx_Timestamp_offset = 5
        # Unlock Enable Button
        self.enableBtn.setEnabled(True)

        # Lock Run Mode radio btns
        self.set_radio_btns_state('locked')
       
        # Send CAN continously
        while(TransmitFlag):
            try:
                if EnableFlag:
                    self.rdm.enable(bus)
                    EnableFlag = False
                self.rdm.update_CAN_msg()               
                for msg in self.rdm.msg_list:
                    bus.send(msg,0.1)
                    # Logging Tx message
                    line = msg2str(msg)
                    # Need to figure out the time to add to EPOCH
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
            msg = listener.get_message(timeout = 0.05)
            with lock:
                self.rdm.get_inverters_status(msg)

        
    def start_CAN_thread(self):
        global TransmitFlag
        TransmitFlag = True

        global ReadFlag
        ReadFlag = True


        # change SSB text to STOP
        self.startStopBtn.setText('Stop')
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.stop_transmit())

        ## Init CAN  ##
        initCAN()
         
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
        
        # Set this flag to  disable RDM
        print ("Disable RDM...")
        EnableFlag = False

        # Set this flag to stop the ongoing transmittion
        print ("Stop CAN transmit...")
        TransmitFlag = False
        self.rdm.disable(bus)

        # Set this flag to stop reading  inverter status
        print ("Stop CAN read..")
        ReadFlag = False
        notifier.stop()
        listener.stop()
        

        # Wait for threads termination
        print ("Stop Transmit & Read CAN threads...")
        global send_thread
        global read_thread
        send_thread.join()
        read_thread.join()


        # shutdown bus
        print ("Stop CAN bus...")
        bus.shutdown()
        bus.flush_tx_buffer()

        # reset GUI
        self.reset_gui()
        #print('Active threads: {}'.format(threading.active_count()))



                                  
    #######################################        
    ############# Main functions ##########          
    #######################################
 

def initCAN():
    global bus
    try:
        can.rc['interface'] = 'socketcan'
        can.rc['bitrate'] = 500000
        can.rc['channel'] = 'can0'
        bus = Bus()
        bus.flush_tx_buffer()

        ## CAN listerner ##
        global listener
        global notifier
        global logger
        # Logging Rx message 
        logger   = can.ASCWriter(log_file_name())
        listener = can.BufferedReader()
        notifier = can.Notifier(bus, [listener,logger])
        #notifier = can.Notifier(bus, [listener])
    except:
        print('No can0 device ')


def create_file_name(vehicle_number = 0):
    if isinstance(vehicle_number,int):
        file_name = 'PV{:02d}.asc'.format(vehicle_number)
    else:
        # file name range from .1 to .9
        file_name = 'PV{:02.1f}.asc'.format(vehicle_number)
    return file_name

def log_file_name():
    global vehicle_in_test_num
    file_name = create_file_name(vehicle_in_test_num)
    while path.exists(file_name) :
        print (file_name)
        # file already exists, add 0.1 to vehicle test number
        vehicle_in_test_num = vehicle_in_test_num + 0.1
        file_name = create_file_name(vehicle_in_test_num) 
    return file_name

              
def msg2str(msg):
    #t = msg.timestamp (timestamp is already handled by the log_event function)
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


	
def main():

    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    #form.showFullScreen()   


    ## Thread Rlock for thread safety for
    ## read/write status to GUI
    global lock
    lock = threading.RLock()

    ## QTimer for updating GUI every second ##
    ## Timer need to start in Main Thread i.e in main()
    timer = QTimer()
    timer.timeout.connect(form.update_gui)
    timer.start(1000)

    ## Start App ##
    app.exec_()
	
if __name__ == '__main__':
    main()
