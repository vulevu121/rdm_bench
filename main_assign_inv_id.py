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

inverters = ['TM1','TM2','GEN']
id_index  = 0 



#logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)


class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        
        # Create RDM object
        self.rdm = RDM()
        self.ID_to_assign.setText(inverters[id_index])
        self.ID_down_btn.clicked.connect      (lambda:self.ID_up())
        self.ID_up_btn.clicked.connect        (lambda:self.ID_down())
        self.OK_btn.clicked.connect           (lambda:self.ID_assign_cmd())
        

        # Default page
        self.change_page('Assign ID page')
   
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

    def ID_up(self): 
        self.status_box.clear()
        global id_index
        id_index = (id_index + 1) % len(inverters)
        self.ID_to_assign.setText(inverters[id_index])



    def ID_down(self):
        self.status_box.clear()
        global id_index
        id_index = (id_index - 1) % len(inverters)
        self.ID_to_assign.setText(inverters[id_index])

    def ID_assign_cmd(self):
        global id_index
        result = self.rdm.assign_id(bus, inverters[id_index])
        self.status_box.setText(result)

    def msgBtn(self):
        ret = self.CAN_adapter_msg.exec_()

    def change_page(self,target = 'EPB page'):
        pages = {'EPB page': self.EPB_page, 'RDM page': self.RDM_page,'Operator page': self.Operator_page, 'Assign ID page': self.Assign_ID_page}
        self.stackedWidget.setCurrentWidget(pages[target])


                                  
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

def main():

    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    #form.showFullScreen()   



    ## Start App ##
    app.exec_()
	
if __name__ == '__main__':
    main()
