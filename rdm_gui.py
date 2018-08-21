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
        MainWindow.resize(800, 480)
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
"    background-color: rgb(59, 56, 56);\n"
"    height: 40px;\n"
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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(70, 90, 93, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startBtn.setFont(font)
        self.startBtn.setStyleSheet("background-color: rgb(118, 118, 113);")
        self.startBtn.setObjectName("startBtn")
        self.torqueCmdBox = QtWidgets.QComboBox(self.centralwidget)
        self.torqueCmdBox.setGeometry(QtCore.QRect(220, 290, 111, 30))
        self.torqueCmdBox.setObjectName("torqueCmdBox")
        self.torqueCmdBox.addItem("")
        self.torqueCmdBox.addItem("")
        self.torqueCmdBox.addItem("")
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
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(70, 390, 93, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stop_btn.setFont(font)
        self.stop_btn.setObjectName("stop_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 290, 137, 30))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 150, 661, 121))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 70, 331, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_1.setGeometry(QtCore.QRect(10, 30, 331, 31))
        self.radioButton_1.setObjectName("radioButton_1")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(70, 340, 581, 23))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 800, 79))
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
        self.enableBtn.setGeometry(QtCore.QRect(180, 90, 93, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.enableBtn.setFont(font)
        self.enableBtn.setStyleSheet("background-color: rgb(118, 118, 113);")
        self.enableBtn.setObjectName("enableBtn")
        self.label_2.raise_()
        self.label_3.raise_()
        self.groupBox.raise_()
        self.startBtn.raise_()
        self.torqueCmdBox.raise_()
        self.stop_btn.raise_()
        self.label.raise_()
        self.progressBar.raise_()
        self.label_4.raise_()
        self.menuBtn.raise_()
        self.epbBtn.raise_()
        self.enableBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.torqueCmdBox.setItemText(0, _translate("MainWindow", "10 nm"))
        self.torqueCmdBox.setItemText(1, _translate("MainWindow", "50 nm"))
        self.torqueCmdBox.setItemText(2, _translate("MainWindow", "100 nm"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Torque Command:"))
        self.groupBox.setTitle(_translate("MainWindow", "Test Profiles:"))
        self.radioButton_2.setText(_translate("MainWindow", "RDM Test #2"))
        self.radioButton_1.setText(_translate("MainWindow", "RDM Test #1"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">RDM Bench</span></p></body></html>"))
        self.enableBtn.setText(_translate("MainWindow", "Enable"))

import rdm_graphics_rc
