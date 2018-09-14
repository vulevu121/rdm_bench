# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color:rgb(59, 56, 56);\n"
"    color: rgb(218, 218, 218);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(190, 110, 93, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet("background-color: rgb(118, 118, 113);")
        self.start_btn.setObjectName("start_btn")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(370, 320, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.epb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.epb_btn.setGeometry(QtCore.QRect(660, 10, 131, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/epb_normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.epb_btn.setIcon(icon)
        self.epb_btn.setIconSize(QtCore.QSize(50, 50))
        self.epb_btn.setFlat(True)
        self.epb_btn.setObjectName("epb_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(190, 420, 93, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stop_btn.setFont(font)
        self.stop_btn.setObjectName("stop_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 320, 181, 31))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 151, 491))
        self.frame.setStyleSheet("background-color: rgb(50, 45, 45);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.menu_btn = QtWidgets.QPushButton(self.frame)
        self.menu_btn.setGeometry(QtCore.QRect(10, 10, 131, 71))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("graphics/menu_normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon1)
        self.menu_btn.setIconSize(QtCore.QSize(50, 50))
        self.menu_btn.setFlat(True)
        self.menu_btn.setObjectName("menu_btn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(180, 170, 591, 121))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 70, 331, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 331, 31))
        self.radioButton.setObjectName("radioButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(190, 370, 581, 23))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setObjectName("progressBar")
        self.groupBox.raise_()
        self.frame.raise_()
        self.start_btn.raise_()
        self.comboBox.raise_()
        self.epb_btn.raise_()
        self.stop_btn.raise_()
        self.label.raise_()
        self.progressBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.comboBox.setItemText(0, _translate("MainWindow", "10 nm"))
        self.comboBox.setItemText(1, _translate("MainWindow", "50 nm"))
        self.comboBox.setItemText(2, _translate("MainWindow", "100 nm"))
        self.epb_btn.setText(_translate("MainWindow", "EPB"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Torque Command:"))
        self.menu_btn.setText(_translate("MainWindow", "Menu"))
        self.groupBox.setTitle(_translate("MainWindow", "Test Profiles:"))
        self.radioButton_2.setText(_translate("MainWindow", "RDM Test #2"))
        self.radioButton.setText(_translate("MainWindow", "RDM Test #1"))

