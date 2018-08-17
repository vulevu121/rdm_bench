from PyQt5.QtWidgets import QMainWindow, QApplication
#from PyQt5.QtGui import QIcon, QPixmap
import sys

from rdm_gui import *
from inv_control import *



TransmitFlag = False


class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

            
        # Start CAN bus
        bus = initCAN()    
        self.rdm = RDM()
        self.startBtn.clicked.connect(lambda: self.start_CAN_thread())
        self.stopBtn.clicked.connect(lambda: self.stop_transmitt())
        
    def start_transmit(self):
        print("Start CAN transmit...")
        global TransmitFlag
        self.rdm.enable()
        self.rdm.set_torque(0)
        
        # Send CAN continously
        while(TransmitFlag):
            # Check for change in torque command value (from dropdown menu)
            #and convert to integer
            torque_value = int(self.torqueCmdBox.currentText())
            self.rdm.set_torque(torque_value)
            
            # Update before the next transmit
            self.rdm.update_CAN_msg()

            for msg in self.rdm.msg_list: 
                bus.send(msg)
                
            # Send messages every 10 ms    
            time.sleep(0.01)

    def stop_transmit(self):
        print ("Stop CAN transmit...")
        global TransmitFlag
        # Set this flag to stop the ongoing transmittion 
        TransmitFlag = False
        # Send msg 5 more times before complete stop
        self.rdm.disable()
        self.rdm.set_torque(0)
        self.rdm.update_CAN_msg()
        
        for i in range(5):          
            for msg in self.rdm.msg_list: 
                bus.send(msg)
                
            # Send messages every 10 ms    
            time.sleep(0.01)  
    


    def start_CAN_thread(self):
        print ("Start CAN thread...")
        global TransmitFlag
        TransmitFlag = True
        
        # separate thread to prevent gui freezing
        thread = threading.Thread(target=self.start_transmit())
        thread.daemon = True
        thread.start()        



def initCAN():
        can.rc['interface'] = 'socketcan'
        can.rc['bitrate'] = 500000
        can.rc['channel'] = 'can0'
        bus = Bus()
        bus.flush_tx_buffer()
        return bus
	
def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()
	
if __name__ == '__main__':
    main()
