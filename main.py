""" Author: Khuong Nguyen, Vu Le
    2.0 RDM Application Script"""


from PyQt5.QtWidgets import QMainWindow, QApplication
#from PyQt5.QtGui import QIcon, QPixmap
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
torqueCmdBoxValues = ['0 nm', '10 nm','11 nm', '12 nm', '13 nm', '14 nm']


class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Add items to combo box
        global torqueCmdBoxValues
        self.torqueCmdBox.clear()
        self.torqueCmdBox.addItems(torqueCmdBoxValues)

            
        # Start CAN bus
        initCAN()
        # Create RDM object
        self.rdm = RDM()

        # Event handlers
        self.torqueCmdBox.currentIndexChanged.connect(lambda:self.update_torque_cmd())
        self.startStopBtn.clicked.connect            (lambda:self.start_CAN_thread())
        self.enableBtn.clicked.connect               (lambda:self.enable_RDM())
        self.torqueCmdMinus.clicked.connect          (lambda:self.minus_torque())
        self.torqueCmdPlus.clicked.connect           (lambda:self.plus_torque())

    def start_read(self):
        global ReadFlag
        print('Reading inverter status...')
        while (ReadFlag):
            self.rdm.get_inverters_status(bus)
            self.tm1StatusBox.setText(self.rdm.TM1_status_sig)
            self.tm2StatusBox.setText(self.rdm.TM2_status_sig)
            
    def minus_torque(self):
        global torque_value
        print('Torque command minus 1...')
        # Decrease torque command by 1 and ensure it is within (0,14)
        torque_value = limit(torque_value - 1, 0, 14)   
        self.rdm.set_torque(torque_value)
        # Update torque display
        self.torqueCmdBox_2.setText('{} nm'.format(torque_value))

    def plus_torque(self):
        global torque_value
        print('Torque command plus 1...')
        # Increase torque command by 1 and ensure it is within (0,14)
        torque_value = limit(torque_value + 1, 0, 14)   
        self.rdm.set_torque(torque_value)
        # Update torque display
        self.torqueCmdBox_2.setText('{} nm'.format(torque_value))    
    
    def update_torque_cmd(self):
        global torque_value
        # Check for change in torque command value (from dropdown menu)
        # and convert to integer
        torque_value = numberFromString(self.torqueCmdBox.currentText())
        self.rdm.set_torque(torque_value)

    def enable_RDM(self):
        print("Enable RDM...")
        global EnableFlag
        EnableFlag = True

    def start_transmit(self):
        print("Start CAN transmit...")
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
            #for msg in self.rdm.msg_list_tm1:
            #for msg in self.rdm.msg_list_tm2:
                bus.send(msg)                
            # Send messages every 10 ms    
            time.sleep(0.007)

    def stop_transmit(self):
        global TransmitFlag
        global EnableFlag
        global ReadFlag

        # change SSB text to START
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.start_CAN_thread())
        self.startStopBtn.setText('Start')
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
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.stop_transmit())
        self.startStopBtn.setText('Stop')

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
