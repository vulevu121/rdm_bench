""" Author: Khuong Nguyen, Vu Le
    2.0 RDM Application Script"""


from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys

from rdm_gui import *
from inv_control import *
import threading
import re


TransmitFlag = False
EnableFlag   = False                                                                                                                                   
ReadFlag     = False
bus = None
torque_value = 10
cycle_time = 0.01

# Add these options to torqueCmdBox


class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Add items to combo box
        global torque_value
        self.torqueCmdBox.setText('{} Nm'.format(torque_value))
        self.enableBtn.setEnabled(False)
        self.Both_radio_btn.setChecked(True)
        self.radio_btns = [self.Both_radio_btn, self.TM1_radio_btn, self.TM2_radio_btn]
        # Start CAN bus
        #initCAN()
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

        # Pop Up meassage box
        self.mode_msg_box = QMessageBox()
        self.mode_msg_box.setIcon(QMessageBox.Information)
        self.mode_msg_box.setText('RDM is running!')
        self.mode_msg_box.setInformativeText('Please Stop RDM and try again.')
        self.mode_msg_box.setWindowTitle("Run Mode Message")
        self.mode_msg_box.setStyleSheet('background-color: rgb(59, 56, 56)')
        self.mode_msg_box.setStandardButtons(QMessageBox.Close)        
        
           
    def run_mode(self,mode):
        global EnableFlag
        if EnableFlag != True:
            self.rdm.run_mode = mode
            print('Run Mode Changed')
        #else:
            #print('RDM is running. MODE can be changed after RDM STOP')
            #ret = self.mode_msg_box.exec_()
            
    def set_radio_btns_state(self, state = 'unlocked'):
        for btn in self.radio_btns:
            if state == 'locked':
                btn.setEnabled(False)
            elif state == 'unlocked':
                btn.setEnabled(True)

    def start_read(self):
        global ReadFlag
        print('Reading inverter status...')
        while (ReadFlag):
            try:
                self.rdm.get_inverters_status(bus)
                self.tm1StatusBox.setText(self.rdm.TM1_status_sig)
                self.tm2StatusBox.setText(self.rdm.TM2_status_sig)
                self.rpmLCD.display(self.rdm.TM1_speed_sens)
                self.torqueLCD.display(self.rdm.TM1_torque_sens)
            except:
                print('Unable to receive on CAN bus\n')
                break
            
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

        # change button text to Disable
        self.enableBtn.setText('Disable')
        self.enableBtn.clicked.disconnect()
        self.enableBtn.clicked.connect(lambda: self.disable_RDM())
        
        print("Mode buttons are locked")
        self.set_radio_btns_state('locked')

    def disable_RDM(self):
        print("Disable RDM...")
        global EnableFlag
        EnableFlag = False

        # change button text to Enable
        self.enableBtn.setText('Enable')
        self.enableBtn.clicked.disconnect()
        self.enableBtn.clicked.connect(lambda: self.enable_RDM())
        
        global TransmitFlag
        # stop send thread temporarily to send disable command
        TransmitFlag = False
        self.rdm.disable(bus)
        # resume send thread
        TransmitFlag = True

        # Unlock radio buttons
        print("Mode buttons are unlocked")
        self.set_radio_btns_state('unlocked')
        
    def start_transmit(self):
        print("Start CAN transmit...\n")
        global TransmitFlag
        global bus
        global torque_value
        global cycle_time
        global EnableFlag 

        # Unlock Enable Button
        self.enableBtn.setEnabled(True)
       
        # Send CAN continously
        while(TransmitFlag):
            try:
                if EnableFlag:
                    self.rdm.enable(bus)
                    EnableFlag = False
                self.rdm.update_CAN_msg()               
                for msg in self.rdm.msg_list:
                    bus.send(msg)                
                # Send messages every 10 ms    
                time.sleep(0.007)
            except:
                print('Unable to send on CAN bus\n')
                break
        
    def stop_transmit(self):
        global TransmitFlag
        global EnableFlag
        global ReadFlag

        # Set this flag to  disable RDM
        print ("Disable RDM...")
        EnableFlag = False

        # Set this flag to stop the ongoing transmittion
        print ("Stop CAN transmit...")
        TransmitFlag = False
        self.rdm.disable(bus)
        
        # Set this flag to stop reading  inverter status
        print ("Stop reading status...")
        ReadFlag = False


        # Wait for threads termination
        global send_thread
        global read_thread
        send_thread.join(1)
        read_thread.join(1)

        # reset GUI
        self.reset_gui()
        
##        # change SSB text to START
##        self.startStopBtn.setText('Start')
##        self.startStopBtn.clicked.disconnect()
##        self.startStopBtn.clicked.connect(lambda: self.start_CAN_thread())
##
##        # Lock Enable Button
##        self.enableBtn.setEnabled(False)
##
##        # clear text from status box
##        self.tm1StatusBox.clear()
##        self.tm2StatusBox.clear()
##        self.rpmLCD.display(0)
##        self.torqueLCD.display(0)
##        
##        # Unlock Run Mode radio buttons
##        self.set_radio_btns_state('unlocked')

    def reset_gui(self):
        # reset torque command box
        global torque_value
        self.torqueCmdBox.setText('{} Nm'.format(torque_value))

        # reset SSB 
        self.startStopBtn.setText('Start')
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.start_CAN_thread())


        # reset enable button
        self.enableBtn.setText('Enable')
        self.enableBtn.clicked.disconnect()
        self.enableBtn.clicked.connect(lambda: self.enable_RDM())
        self.enableBtn.setEnabled(False)

        # reset radio button
        self.Both_radio_btn.setChecked(True)
        self.run_mode(0)
        self.set_radio_btns_state('unlocked')

        # clear text from status boxes
        self.tm1StatusBox.clear()
        self.tm2StatusBox.clear()
        self.rpmLCD.display(0)
        self.torqueLCD.display(0)
        
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

        global send_thread
        global read_thread
        
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
    try:
        can.rc['interface'] = 'socketcan'
        can.rc['bitrate'] = 500000
        can.rc['channel'] = 'can0'
        bus = Bus()
        bus.flush_tx_buffer()
    except:
        print('No can0 device bus')
	
def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    #form.showFullScreen()
    app.exec_()
	
if __name__ == '__main__':
    main()
