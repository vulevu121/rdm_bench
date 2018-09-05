""" Author: Khuong Nguyen, Vu Le
    2.0 RDM Application Script"""


from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from rdm_gui import *
from inv_control import *
import threading
import re


TransmitFlag = False
EnableFlag   = False                                                                                                                                   
ReadFlag     = False
bus = None
torque_value = 0
cycle_time = 0.01

# Add these options to torqueCmdBox


class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Add items to combo box
        #global torqueCmdBoxValues
        #self.torqueCmdBox.clear()
        #self.torqueCmdBox.addItems(torqueCmdBoxValues)
        self.torqueCmdBox.setText('0 Nm')  
        self.Both_radio_btn.setChecked(True) 
        # Start CAN bus
        initCAN()
        # Create RDM object
        self.rdm = RDM()

        # Event handlers
        #self.torqueCmdBox.currentIndexChanged.connect(lambda:self.update_torque_cmd())
        self.startStopBtn.clicked.connect       (lambda:self.start_CAN_thread())
        self.enableBtn.clicked.connect          (lambda:self.enable_RDM())
        self.torqueCmdMinus.clicked.connect     (lambda:self.minus_torque())
        self.torqueCmdPlus.clicked.connect      (lambda:self.plus_torque())
        self.Both_radio_btn.toggled.connect     (lambda:self.run_mode(0))
        self.TM1_radio_btn.toggled.connect      (lambda:self.run_mode(1))
        self.TM2_radio_btn.toggled.connect      (lambda:self.run_mode(2))
        
    def run_mode(self,choice):
        self.rdm.run_mode = choice
        #print(self.rdm.run_mode)

    def start_read(self):
        global ReadFlag
        print('Reading inverter status...')
        while (ReadFlag):
            self.rdm.get_inverters_status(bus)
            self.tm1StatusBox.setText(self.rdm.TM1_status_sig)
            self.tm2StatusBox.setText(self.rdm.TM2_status_sig)
            self.rpmLCD.display(self.rdm.TM1_speed_sens)
            self.torqueLCD.display(self.rdm.TM1_torque_sens)
            
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
    

    def enable_RDM(self):
        print("Enable RDM...")
        global EnableFlag
        EnableFlag = True

    def start_transmit(self):
        print("Start CAN transmit...\n")
        global TransmitFlag
        global bus
        global torque_value
        global cycle_time
        global EnableFlag 

       
        # Send CAN continously
        while(TransmitFlag):
            if EnableFlag:
                self.rdm.enable(bus)
                EnableFlag = False
            self.rdm.update_CAN_msg()
            
            for msg in self.rdm.msg_list:
                bus.send(msg)                
            # Send messages every 10 ms    
            time.sleep(0.007)

    def stop_transmit(self):
        global TransmitFlag
        global EnableFlag
        global ReadFlag

        # change SSB text to START
        self.startStopBtn.setText('Start')
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.start_CAN_thread())

        # Set this flag to  disable RDM
        print ("Disable RDM...")
        EnableFlag = False
        # Set this flag to stop reading  inverter status
        print ("Stop reading status...")
        ReadFlag = False
        # Set this flag to stop the ongoing transmittion
        print ("Stop CAN transmit...")
        TransmitFlag = False
        self.rdm.disable(bus)
  


    def start_CAN_thread(self):
        print ("Start CAN thread...")
        global TransmitFlag
        TransmitFlag = True

        global ReadFlag
        ReadFlag = True

        # change SSB text to STOP
        self.startStopBtn.setText('Stop')
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.stop_transmit())


        # separate thread to prevent gui freezing. PASS HANDLE NOT FUNCTION CALL
        send_thread = threading.Thread(target=self.start_transmit, args=())
        send_thread.daemon = True
        send_thread.start()        

        read_thread = threading.Thread(target=self.start_read, args=())
        read_thread.daemon = True
        read_thread.start()        

def numberFromString(string):
    # this return a list of number from the string
    numbers = re.findall('\d+',string)
    # convert to integer
    numbers = [int(num) for num in numbers]
    # just need to access the first item
    return numbers[0]                

def initCAN():
    global bus
    can.rc['interface'] = 'socketcan'
    can.rc['bitrate'] = 500000
    can.rc['channel'] = 'can0'
    bus = Bus()
    bus.flush_tx_buffer()
	
def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    #form.showFullScreen()
    app.exec_()
	
if __name__ == '__main__':
    main()
