# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rdm_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 503)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: rgb(218, 218, 218);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(118, 118, 113);\n"
"    height: 40px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(59, 56, 56);\n"
"    color: rgb(100, 95, 95);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0px 10px 0px 10px;\n"
"    left: 10px;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background: black;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane {\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(59, 56, 56);\n"
"    border: 1px solid gray;\n"
"    padding: 10px;\n"
"    min-width: 150px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 rgb(59, 56, 56), stop: 0.4 rgb(100, 95, 95),\n"
"                                stop: 0.5 rgb(80, 75, 75), stop: 1.0 rgb(59, 56, 56));\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton {\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(59, 56, 56);\n"
"    selection-background-color: lightgray;\n"
"\n"
"}\n"
"\n"
"QProgressBar{\n"
"    background-color: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLCDNumber {\n"
"    border:1px solid gray;\n"
"    border-radius: 5px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startStopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startStopBtn.setGeometry(QtCore.QRect(70, 90, 93, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startStopBtn.setFont(font)
        self.startStopBtn.setStyleSheet("")
        self.startStopBtn.setObjectName("startStopBtn")
        self.epbBtn = QtWidgets.QPushButton(self.centralwidget)
        self.epbBtn.setGeometry(QtCore.QRect(740, 6, 40, 40))
        self.epbBtn.setStyleSheet("QPushButton {\n"
"    border-image: url(:/epb_graphics/graphics/epb_normal.png);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/epb_graphics/graphics/epb_pressed.png);\n"
"}")
        self.epbBtn.setText("")
        self.epbBtn.setIconSize(QtCore.QSize(50, 50))
        self.epbBtn.setFlat(True)
        self.epbBtn.setObjectName("epbBtn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 140, 281, 121))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 261, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 800, 81))
        self.label_3.setObjectName("label_3")
        self.menuBtn = QtWidgets.QPushButton(self.centralwidget)
        self.menuBtn.setGeometry(QtCore.QRect(20, 6, 40, 40))
        self.menuBtn.setMouseTracking(False)
        self.menuBtn.setStyleSheet("QPushButton {\n"
"    border-image: url(:/menu_graphics/graphics/menu_normal.png);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/menu_graphics/graphics/menu_pressed.png);\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"}")
        self.menuBtn.setText("")
        self.menuBtn.setIconSize(QtCore.QSize(50, 50))
        self.menuBtn.setCheckable(False)
        self.menuBtn.setDefault(True)
        self.menuBtn.setFlat(True)
        self.menuBtn.setObjectName("menuBtn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.label_4.setObjectName("label_4")
        self.enableBtn = QtWidgets.QPushButton(self.centralwidget)
        self.enableBtn.setEnabled(False)
        self.enableBtn.setGeometry(QtCore.QRect(180, 90, 93, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.enableBtn.setFont(font)
        self.enableBtn.setStyleSheet("")
        self.enableBtn.setObjectName("enableBtn")
        self.torqueCmdPlus = QtWidgets.QPushButton(self.centralwidget)
        self.torqueCmdPlus.setGeometry(QtCore.QRect(290, 410, 60, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.torqueCmdPlus.setFont(font)
        self.torqueCmdPlus.setStyleSheet("QPushButton {\n"
"    font: 30pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.torqueCmdPlus.setFlat(False)
        self.torqueCmdPlus.setObjectName("torqueCmdPlus")
        self.torqueCmdMinus = QtWidgets.QPushButton(self.centralwidget)
        self.torqueCmdMinus.setGeometry(QtCore.QRect(70, 410, 60, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.torqueCmdMinus.setFont(font)
        self.torqueCmdMinus.setStyleSheet("QPushButton {\n"
"    font: 30pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.torqueCmdMinus.setObjectName("torqueCmdMinus")
        self.torqueCmdBox = QtWidgets.QLineEdit(self.centralwidget)
        self.torqueCmdBox.setGeometry(QtCore.QRect(150, 410, 121, 60))
        self.torqueCmdBox.setText("")
        self.torqueCmdBox.setAlignment(QtCore.Qt.AlignCenter)
        self.torqueCmdBox.setObjectName("torqueCmdBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 100, 361, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(21, 31, 331, 171))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tm1Label = QtWidgets.QLabel(self.layoutWidget1)
        self.tm1Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tm1Label.setObjectName("tm1Label")
        self.gridLayout.addWidget(self.tm1Label, 0, 0, 1, 1)
        self.tm1StatusBox = QtWidgets.QLineEdit(self.layoutWidget1)
        self.tm1StatusBox.setMouseTracking(False)
        self.tm1StatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.tm1StatusBox.setText("")
        self.tm1StatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.tm1StatusBox.setReadOnly(True)
        self.tm1StatusBox.setObjectName("tm1StatusBox")
        self.gridLayout.addWidget(self.tm1StatusBox, 0, 1, 1, 1)
        self.tm2Label = QtWidgets.QLabel(self.layoutWidget1)
        self.tm2Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tm2Label.setObjectName("tm2Label")
        self.gridLayout.addWidget(self.tm2Label, 1, 0, 1, 1)
        self.tm2StatusBox = QtWidgets.QLineEdit(self.layoutWidget1)
        self.tm2StatusBox.setMouseTracking(False)
        self.tm2StatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.tm2StatusBox.setText("")
        self.tm2StatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.tm2StatusBox.setReadOnly(True)
        self.tm2StatusBox.setObjectName("tm2StatusBox")
        self.gridLayout.addWidget(self.tm2StatusBox, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.rpmLCD = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.rpmLCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rpmLCD.setLineWidth(1)
        self.rpmLCD.setSmallDecimalPoint(False)
        self.rpmLCD.setDigitCount(15)
        self.rpmLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.rpmLCD.setObjectName("rpmLCD")
        self.gridLayout.addWidget(self.rpmLCD, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.torqueLCD = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.torqueLCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.torqueLCD.setLineWidth(1)
        self.torqueLCD.setDigitCount(15)
        self.torqueLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.torqueLCD.setObjectName("torqueLCD")
        self.gridLayout.addWidget(self.torqueLCD, 3, 1, 1, 1)
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgLabel.setMouseTracking(True)
        self.bgLabel.setObjectName("bgLabel")
        self.inverterGroupdBox = QtWidgets.QGroupBox(self.centralwidget)
        self.inverterGroupdBox.setGeometry(QtCore.QRect(70, 280, 281, 111))
        self.inverterGroupdBox.setObjectName("inverterGroupdBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.inverterGroupdBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 265, 69))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TM1_radio_btn = QtWidgets.QRadioButton(self.layoutWidget2)
        self.TM1_radio_btn.setObjectName("TM1_radio_btn")
        self.gridLayout_2.addWidget(self.TM1_radio_btn, 0, 0, 1, 1)
        self.Both_radio_btn = QtWidgets.QRadioButton(self.layoutWidget2)
        self.Both_radio_btn.setObjectName("Both_radio_btn")
        self.gridLayout_2.addWidget(self.Both_radio_btn, 0, 1, 1, 1)
        self.TM2_radio_btn = QtWidgets.QRadioButton(self.layoutWidget2)
        self.TM2_radio_btn.setObjectName("TM2_radio_btn")
        self.gridLayout_2.addWidget(self.TM2_radio_btn, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 340, 361, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 30, 71, 27))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.vehicle_number = QtWidgets.QSpinBox(self.layoutWidget3)
        self.vehicle_number.setObjectName("vehicle_number")
        self.horizontalLayout.addWidget(self.vehicle_number)
        self.bgLabel.raise_()
        self.label_3.raise_()
        self.groupBox.raise_()
        self.startStopBtn.raise_()
        self.label_4.raise_()
        self.menuBtn.raise_()
        self.epbBtn.raise_()
        self.enableBtn.raise_()
        self.torqueCmdPlus.raise_()
        self.torqueCmdMinus.raise_()
        self.torqueCmdBox.raise_()
        self.groupBox_2.raise_()
        self.inverterGroupdBox.raise_()
        self.groupBox_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startStopBtn.setText(_translate("MainWindow", "Start"))
        self.groupBox.setTitle(_translate("MainWindow", "Test Profiles:"))
        self.radioButton_1.setText(_translate("MainWindow", "RDM Test #1"))
        self.radioButton_2.setText(_translate("MainWindow", "RDM Test #2"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">RDM Bench</span></p></body></html>"))
        self.enableBtn.setText(_translate("MainWindow", "Enable"))
        self.torqueCmdPlus.setText(_translate("MainWindow", "+"))
        self.torqueCmdMinus.setText(_translate("MainWindow", "-"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status"))
        self.tm1Label.setText(_translate("MainWindow", "TM1 Status"))
        self.tm2Label.setText(_translate("MainWindow", "TM2 Status"))
        self.label.setText(_translate("MainWindow", "RPM"))
        self.label_2.setText(_translate("MainWindow", "Torque"))
        self.bgLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.inverterGroupdBox.setTitle(_translate("MainWindow", "Inverter Set"))
        self.TM1_radio_btn.setText(_translate("MainWindow", "TM1 Only"))
        self.Both_radio_btn.setText(_translate("MainWindow", "Both"))
        self.TM2_radio_btn.setText(_translate("MainWindow", "TM2 Only"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Vehicle in Test"))
        self.label_5.setText(_translate("MainWindow", "PV"))

import rdm_graphics_rc
