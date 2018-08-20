from PyQt5.QtWidgets import QMainWindow, QApplication
#from PyQt5.QtGui import QIcon, QPixmap
import sys

from rdm_gui import *
from inv_control import *
import threading
import re


TransmitFlag = False
bus = None
torque_value = 0
cycle_time = 0.01

# Add these options to torqueCmdBox
torqueCmdBoxValues = ['0 nm', '10 nm', '50 nm', '100 nm']


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
        self.torqueCmdBox.currentIndexChanged.connect(lambda: self.update_torque_cmd())
        self.startBtn.clicked.connect(lambda: self.start_CAN_thread())
        self.stop_btn.clicked.connect(lambda: self.stop_transmit())

    def update_torque_cmd(self):
        global torque_value
        # Check for change in torque command value (from dropdown menu)
        # and convert to integer
        torque_value = numberFromString(self.torqueCmdBox.currentText())
        self.rdm.set_torque(torque_value)
        self.rdm.update_CAN_msg()

    def start_transmit(self):
        print("Start CAN transmit...")
        global TransmitFlag
        global bus
        global torque_value
        global cycle_time

       
        self.rdm.enable(bus)
        # Send CAN continously
        while(TransmitFlag):
            self.rdm.update_CAN_msg()
            #bus.send(self.rdm.TM2_torque_cmd_msg)
            for msg in self.rdm.msg_list: 
                bus.send(msg)                
            # Send messages every 10 ms    
            time.sleep(0.008)

    def stop_transmit(self):
        print ("Stop CAN transmit...")
        global TransmitFlag
        # Set this flag to stop the ongoing transmittion 
        TransmitFlag = False
        self.rdm.disable(bus)
  


    def start_CAN_thread(self):
        print ("Start CAN thread...")
        global TransmitFlag
        TransmitFlag = True
        
        # separate thread to prevent gui freezing. PASS HANDLE NOT FUNCTION CALL
        thread = threading.Thread(target=self.start_transmit, args=())
        thread.daemon = True
        thread.start()        


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
    app.exec_()
	
if __name__ == '__main__':
    main()
