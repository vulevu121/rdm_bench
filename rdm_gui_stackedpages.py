# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rdm_gui_stackedpages.ui'
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
"QStackedWidget{\n"
"    background-color: red;\n"
"    color: rgb(218, 218, 218);\n"
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
"QPushButton {\n"
"               background-color: rgb(59, 56, 56, 80);\n"
"               height: 40px;\n"
"               padding: 0px 5px 0px 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"               background-color: transparent;\n"
"               border: 1px solid gray;\n"
"               border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"               border: 1px solid gray;\n"
"               border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"               background-color: gray;\n"
"               color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"               border: 1px solid white;\n"
"               border-radius: 5px;\n"
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
"}\n"
"QSpinBox {\n"
"    color: rgb(218, 218, 218);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"   color: black\n"
"}\n"
"QRadioButton::indicator {\n"
"width: 32px;\n"
"height: 32px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QRadioButton::indicator:unchecked:pressed {\n"
"image: url(:/checkbox/graphics/checkbox_unchecked.png);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked, QRadioButton::indicator:checked:pressed, QRadioButton::indicator:checked:hover {\n"
"image: url(:/checkbox/graphics/checkbox_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"image: url(:/checkbox/graphics/checkbox_hover.png);\n"
"}\n"
"\n"
"QLabel#label_5{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.RDM_page = QtWidgets.QWidget()
        self.RDM_page.setObjectName("RDM_page")
        self.groupBox = QtWidgets.QGroupBox(self.RDM_page)
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
        self.groupBox_3 = QtWidgets.QGroupBox(self.RDM_page)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 326, 361, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.veh_num_save_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.veh_num_save_btn.setGeometry(QtCore.QRect(248, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.veh_num_save_btn.setFont(font)
        self.veh_num_save_btn.setDefault(False)
        self.veh_num_save_btn.setFlat(False)
        self.veh_num_save_btn.setObjectName("veh_num_save_btn")
        self.vehicle_number = QtWidgets.QSpinBox(self.groupBox_3)
        self.vehicle_number.setGeometry(QtCore.QRect(20, 90, 43, 25))
        self.vehicle_number.setObjectName("vehicle_number")
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(18, 20, 331, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 45))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.veh_num_minus = QtWidgets.QPushButton(self.widget)
        self.veh_num_minus.setMinimumSize(QtCore.QSize(45, 0))
        self.veh_num_minus.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.veh_num_minus.setFont(font)
        self.veh_num_minus.setDefault(False)
        self.veh_num_minus.setFlat(False)
        self.veh_num_minus.setObjectName("veh_num_minus")
        self.horizontalLayout.addWidget(self.veh_num_minus)
        self.veh_num_plus = QtWidgets.QPushButton(self.widget)
        self.veh_num_plus.setMinimumSize(QtCore.QSize(45, 0))
        self.veh_num_plus.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.veh_num_plus.setFont(font)
        self.veh_num_plus.setDefault(False)
        self.veh_num_plus.setFlat(False)
        self.veh_num_plus.setObjectName("veh_num_plus")
        self.horizontalLayout.addWidget(self.veh_num_plus)
        self.startStopBtn = QtWidgets.QPushButton(self.RDM_page)
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
        self.menuBtn = QtWidgets.QPushButton(self.RDM_page)
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
        self.label_3 = QtWidgets.QLabel(self.RDM_page)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 800, 81))
        self.label_3.setObjectName("label_3")
        self.torqueCmdBox = QtWidgets.QLineEdit(self.RDM_page)
        self.torqueCmdBox.setGeometry(QtCore.QRect(150, 410, 121, 60))
        self.torqueCmdBox.setText("")
        self.torqueCmdBox.setAlignment(QtCore.Qt.AlignCenter)
        self.torqueCmdBox.setObjectName("torqueCmdBox")
        self.torqueCmdPlus = QtWidgets.QPushButton(self.RDM_page)
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
        self.enableBtn = QtWidgets.QPushButton(self.RDM_page)
        self.enableBtn.setEnabled(True)
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
        self.label_4 = QtWidgets.QLabel(self.RDM_page)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.label_4.setObjectName("label_4")
        self.inverterGroupdBox = QtWidgets.QGroupBox(self.RDM_page)
        self.inverterGroupdBox.setGeometry(QtCore.QRect(70, 280, 281, 111))
        self.inverterGroupdBox.setObjectName("inverterGroupdBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.inverterGroupdBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 265, 73))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TM1_radio_btn = QtWidgets.QRadioButton(self.layoutWidget1)
        self.TM1_radio_btn.setEnabled(False)
        self.TM1_radio_btn.setObjectName("TM1_radio_btn")
        self.gridLayout_2.addWidget(self.TM1_radio_btn, 0, 0, 1, 1)
        self.Both_radio_btn = QtWidgets.QRadioButton(self.layoutWidget1)
        self.Both_radio_btn.setEnabled(True)
        self.Both_radio_btn.setObjectName("Both_radio_btn")
        self.gridLayout_2.addWidget(self.Both_radio_btn, 0, 1, 1, 1)
        self.TM2_radio_btn = QtWidgets.QRadioButton(self.layoutWidget1)
        self.TM2_radio_btn.setEnabled(False)
        self.TM2_radio_btn.setObjectName("TM2_radio_btn")
        self.gridLayout_2.addWidget(self.TM2_radio_btn, 1, 0, 1, 1)
        self.torqueCmdMinus = QtWidgets.QPushButton(self.RDM_page)
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
        self.bgLabel = QtWidgets.QLabel(self.RDM_page)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgLabel.setMouseTracking(True)
        self.bgLabel.setObjectName("bgLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.RDM_page)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 100, 361, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(21, 31, 331, 172))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.torqueLCD = QtWidgets.QLCDNumber(self.layoutWidget2)
        self.torqueLCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.torqueLCD.setLineWidth(1)
        self.torqueLCD.setDigitCount(15)
        self.torqueLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.torqueLCD.setObjectName("torqueLCD")
        self.gridLayout.addWidget(self.torqueLCD, 3, 1, 1, 1)
        self.tm1StatusBox = QtWidgets.QLineEdit(self.layoutWidget2)
        self.tm1StatusBox.setMouseTracking(False)
        self.tm1StatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.tm1StatusBox.setText("")
        self.tm1StatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.tm1StatusBox.setReadOnly(True)
        self.tm1StatusBox.setObjectName("tm1StatusBox")
        self.gridLayout.addWidget(self.tm1StatusBox, 0, 1, 1, 1)
        self.rpmLCD = QtWidgets.QLCDNumber(self.layoutWidget2)
        self.rpmLCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rpmLCD.setLineWidth(1)
        self.rpmLCD.setSmallDecimalPoint(False)
        self.rpmLCD.setDigitCount(15)
        self.rpmLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.rpmLCD.setObjectName("rpmLCD")
        self.gridLayout.addWidget(self.rpmLCD, 2, 1, 1, 1)
        self.tm2StatusBox = QtWidgets.QLineEdit(self.layoutWidget2)
        self.tm2StatusBox.setMouseTracking(False)
        self.tm2StatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.tm2StatusBox.setText("")
        self.tm2StatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.tm2StatusBox.setReadOnly(True)
        self.tm2StatusBox.setObjectName("tm2StatusBox")
        self.gridLayout.addWidget(self.tm2StatusBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.tm2Label = QtWidgets.QLabel(self.layoutWidget2)
        self.tm2Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tm2Label.setObjectName("tm2Label")
        self.gridLayout.addWidget(self.tm2Label, 1, 0, 1, 1)
        self.tm1Label = QtWidgets.QLabel(self.layoutWidget2)
        self.tm1Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tm1Label.setObjectName("tm1Label")
        self.gridLayout.addWidget(self.tm1Label, 0, 0, 1, 1)
        self.epbBtn = QtWidgets.QPushButton(self.RDM_page)
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
        self.bgLabel.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.startStopBtn.raise_()
        self.label_3.raise_()
        self.torqueCmdBox.raise_()
        self.torqueCmdPlus.raise_()
        self.enableBtn.raise_()
        self.label_4.raise_()
        self.inverterGroupdBox.raise_()
        self.torqueCmdMinus.raise_()
        self.groupBox_2.raise_()
        self.epbBtn.raise_()
        self.menuBtn.raise_()
        self.stackedWidget.addWidget(self.RDM_page)
        self.EPB_page = QtWidgets.QWidget()
        self.EPB_page.setObjectName("EPB_page")
        self.bgLabel_2 = QtWidgets.QLabel(self.EPB_page)
        self.bgLabel_2.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgLabel_2.setMouseTracking(True)
        self.bgLabel_2.setObjectName("bgLabel_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.EPB_page)
        self.groupBox_4.setGeometry(QtCore.QRect(70, 149, 671, 311))
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 36, 641, 251))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LtActrStateLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.LtActrStateLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LtActrStateLabel.setObjectName("LtActrStateLabel")
        self.gridLayout_3.addWidget(self.LtActrStateLabel, 0, 0, 1, 1)
        self.LtActrStateStatusBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.LtActrStateStatusBox.setMouseTracking(False)
        self.LtActrStateStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.LtActrStateStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.LtActrStateStatusBox.setReadOnly(True)
        self.LtActrStateStatusBox.setObjectName("LtActrStateStatusBox")
        self.gridLayout_3.addWidget(self.LtActrStateStatusBox, 0, 1, 1, 1)
        self.EpbSwLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.EpbSwLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.EpbSwLabel.setObjectName("EpbSwLabel")
        self.gridLayout_3.addWidget(self.EpbSwLabel, 0, 2, 1, 1)
        self.EpbSwStatusBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.EpbSwStatusBox.setMouseTracking(False)
        self.EpbSwStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.EpbSwStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.EpbSwStatusBox.setReadOnly(True)
        self.EpbSwStatusBox.setObjectName("EpbSwStatusBox")
        self.gridLayout_3.addWidget(self.EpbSwStatusBox, 0, 3, 1, 1)
        self.RtActrStateLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.RtActrStateLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RtActrStateLabel.setObjectName("RtActrStateLabel")
        self.gridLayout_3.addWidget(self.RtActrStateLabel, 1, 0, 1, 1)
        self.RtActrStateStatusBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.RtActrStateStatusBox.setMouseTracking(False)
        self.RtActrStateStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.RtActrStateStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.RtActrStateStatusBox.setReadOnly(True)
        self.RtActrStateStatusBox.setObjectName("RtActrStateStatusBox")
        self.gridLayout_3.addWidget(self.RtActrStateStatusBox, 1, 1, 1, 1)
        self.EpbFaultLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.EpbFaultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.EpbFaultLabel.setObjectName("EpbFaultLabel")
        self.gridLayout_3.addWidget(self.EpbFaultLabel, 1, 2, 1, 1)
        self.EpbFaultStatusBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.EpbFaultStatusBox.setMouseTracking(False)
        self.EpbFaultStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.EpbFaultStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.EpbFaultStatusBox.setReadOnly(True)
        self.EpbFaultStatusBox.setObjectName("EpbFaultStatusBox")
        self.gridLayout_3.addWidget(self.EpbFaultStatusBox, 1, 3, 1, 1)
        self.LtActrFaultLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.LtActrFaultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LtActrFaultLabel.setObjectName("LtActrFaultLabel")
        self.gridLayout_3.addWidget(self.LtActrFaultLabel, 2, 0, 1, 1)
        self.LtActrFaultStatusBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.LtActrFaultStatusBox.setMouseTracking(False)
        self.LtActrFaultStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.LtActrFaultStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.LtActrFaultStatusBox.setReadOnly(True)
        self.LtActrFaultStatusBox.setObjectName("LtActrFaultStatusBox")
        self.gridLayout_3.addWidget(self.LtActrFaultStatusBox, 2, 1, 1, 1)
        self.PGearLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.PGearLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PGearLabel.setObjectName("PGearLabel")
        self.gridLayout_3.addWidget(self.PGearLabel, 2, 2, 1, 1)
        self.PGearStatusBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.PGearStatusBox.setMouseTracking(False)
        self.PGearStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.PGearStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PGearStatusBox.setReadOnly(True)
        self.PGearStatusBox.setObjectName("PGearStatusBox")
        self.gridLayout_3.addWidget(self.PGearStatusBox, 2, 3, 1, 1)
        self.RtActrFaultLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.RtActrFaultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RtActrFaultLabel.setObjectName("RtActrFaultLabel")
        self.gridLayout_3.addWidget(self.RtActrFaultLabel, 3, 0, 1, 1)
        self.RtActrFaultStatusBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.RtActrFaultStatusBox.setMouseTracking(False)
        self.RtActrFaultStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.RtActrFaultStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.RtActrFaultStatusBox.setReadOnly(True)
        self.RtActrFaultStatusBox.setObjectName("RtActrFaultStatusBox")
        self.gridLayout_3.addWidget(self.RtActrFaultStatusBox, 3, 1, 1, 1)
        self.PBrakeLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.PBrakeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PBrakeLabel.setObjectName("PBrakeLabel")
        self.gridLayout_3.addWidget(self.PBrakeLabel, 3, 2, 1, 1)
        self.PBrakeStatusBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.PBrakeStatusBox.setMouseTracking(False)
        self.PBrakeStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.PBrakeStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PBrakeStatusBox.setReadOnly(True)
        self.PBrakeStatusBox.setObjectName("PBrakeStatusBox")
        self.gridLayout_3.addWidget(self.PBrakeStatusBox, 3, 3, 1, 1)
        self.EPB_startStopBtn = QtWidgets.QPushButton(self.EPB_page)
        self.EPB_startStopBtn.setGeometry(QtCore.QRect(70, 90, 93, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.EPB_startStopBtn.setFont(font)
        self.EPB_startStopBtn.setStyleSheet("")
        self.EPB_startStopBtn.setObjectName("EPB_startStopBtn")
        self.rdmBtn = QtWidgets.QPushButton(self.EPB_page)
        self.rdmBtn.setGeometry(QtCore.QRect(20, 6, 40, 40))
        self.rdmBtn.setMouseTracking(False)
        self.rdmBtn.setStyleSheet("QPushButton {\n"
"    border-image: url(:/rdm_graphics/graphics/rdm_normal.png);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/rdm_graphics/graphics/rdm_pressed.png);\n"
"}")
        self.rdmBtn.setText("")
        self.rdmBtn.setIconSize(QtCore.QSize(50, 50))
        self.rdmBtn.setCheckable(False)
        self.rdmBtn.setDefault(True)
        self.rdmBtn.setFlat(True)
        self.rdmBtn.setObjectName("rdmBtn")
        self.label_8 = QtWidgets.QLabel(self.EPB_page)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.EPB_page)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 800, 81))
        self.label_9.setObjectName("label_9")
        self.bgLabel_2.raise_()
        self.label_9.raise_()
        self.groupBox_4.raise_()
        self.EPB_startStopBtn.raise_()
        self.label_8.raise_()
        self.rdmBtn.raise_()
        self.stackedWidget.addWidget(self.EPB_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Test Profiles:"))
        self.radioButton_1.setText(_translate("MainWindow", "RDM Test #1"))
        self.radioButton_2.setText(_translate("MainWindow", "RDM Test #2"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Vehicle in Test"))
        self.veh_num_save_btn.setText(_translate("MainWindow", "SAVE"))
        self.label_5.setText(_translate("MainWindow", "PV"))
        self.veh_num_minus.setText(_translate("MainWindow", "<"))
        self.veh_num_plus.setText(_translate("MainWindow", ">"))
        self.startStopBtn.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))
        self.torqueCmdPlus.setText(_translate("MainWindow", "+"))
        self.enableBtn.setText(_translate("MainWindow", "Enable"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">RDM Bench</span></p></body></html>"))
        self.inverterGroupdBox.setTitle(_translate("MainWindow", "Inverter Set"))
        self.TM1_radio_btn.setText(_translate("MainWindow", "TM1 Only"))
        self.Both_radio_btn.setText(_translate("MainWindow", "Both"))
        self.TM2_radio_btn.setText(_translate("MainWindow", "TM2 Only"))
        self.torqueCmdMinus.setText(_translate("MainWindow", "-"))
        self.bgLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "RPM"))
        self.label_2.setText(_translate("MainWindow", "Torque"))
        self.tm2Label.setText(_translate("MainWindow", "TM2 Status"))
        self.tm1Label.setText(_translate("MainWindow", "TM1 Status"))
        self.bgLabel_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "EPB Status"))
        self.LtActrStateLabel.setText(_translate("MainWindow", "LT_ACTR_STATE"))
        self.LtActrStateStatusBox.setText(_translate("MainWindow", "releasing"))
        self.EpbSwLabel.setText(_translate("MainWindow", "EPB_SW_STATE"))
        self.EpbSwStatusBox.setText(_translate("MainWindow", "releasing"))
        self.RtActrStateLabel.setText(_translate("MainWindow", "RT_ACTR_STATE"))
        self.RtActrStateStatusBox.setText(_translate("MainWindow", "releasing"))
        self.EpbFaultLabel.setText(_translate("MainWindow", "EPB_FAULT"))
        self.EpbFaultStatusBox.setText(_translate("MainWindow", "releasing"))
        self.LtActrFaultLabel.setText(_translate("MainWindow", "LT_ACTR_FAULT"))
        self.LtActrFaultStatusBox.setText(_translate("MainWindow", "releasing"))
        self.PGearLabel.setText(_translate("MainWindow", "PGEAR"))
        self.PGearStatusBox.setText(_translate("MainWindow", "releasing"))
        self.RtActrFaultLabel.setText(_translate("MainWindow", "RT_ACTR_FAULT"))
        self.RtActrFaultStatusBox.setText(_translate("MainWindow", "releasing"))
        self.PBrakeLabel.setText(_translate("MainWindow", "PBRAKE"))
        self.PBrakeStatusBox.setText(_translate("MainWindow", "releasing"))
        self.EPB_startStopBtn.setText(_translate("MainWindow", "Start"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">EPB Bench</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))

import rdm_graphics_rc
