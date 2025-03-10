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
        MainWindow.resize(799, 500)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: rgb(218, 218, 218);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QMessageBox{\n"
"    color: rgb(218, 218, 218);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
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
"    background-color: transparent;\n"
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
"}\n"
"\n"
"QLabel#label_27{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit#veh_num_label{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    alignment: AlignHCenter;\n"
"}\n"
"\n"
"QLineEdit#op_veh_num_label{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    alignment: AlignHCenter;\n"
"}\n"
"\n"
"QLineEdit#op_save_file_statusl{\n"
"    alignment: AlignHCenter;\n"
"}\n"
"QLineEdit#op_save_file_statusl{\n"
"    alignment: AlignHCenter;\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit#vin_num_box{\n"
"    alignment: AlignHCenter;\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"QGroupBox#number_pad QPushButton{\n"
"    alignment: AlignHCenter;\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.RDM_page = QtWidgets.QWidget()
        self.RDM_page.setObjectName("RDM_page")
        self.groupBox_3 = QtWidgets.QGroupBox(self.RDM_page)
        self.groupBox_3.setGeometry(QtCore.QRect(37, 330, 351, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 25, 331, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
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
        self.veh_num_label = QtWidgets.QLineEdit(self.layoutWidget)
        self.veh_num_label.setMinimumSize(QtCore.QSize(0, 0))
        self.veh_num_label.setMaximumSize(QtCore.QSize(80, 45))
        self.veh_num_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.veh_num_label.setText("")
        self.veh_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.veh_num_label.setObjectName("veh_num_label")
        self.horizontalLayout.addWidget(self.veh_num_label)
        self.veh_num_down = QtWidgets.QPushButton(self.layoutWidget)
        self.veh_num_down.setMinimumSize(QtCore.QSize(45, 0))
        self.veh_num_down.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.veh_num_down.setFont(font)
        self.veh_num_down.setDefault(False)
        self.veh_num_down.setFlat(False)
        self.veh_num_down.setObjectName("veh_num_down")
        self.horizontalLayout.addWidget(self.veh_num_down)
        self.veh_num_up = QtWidgets.QPushButton(self.layoutWidget)
        self.veh_num_up.setMinimumSize(QtCore.QSize(45, 0))
        self.veh_num_up.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.veh_num_up.setFont(font)
        self.veh_num_up.setDefault(False)
        self.veh_num_up.setFlat(False)
        self.veh_num_up.setObjectName("veh_num_up")
        self.horizontalLayout.addWidget(self.veh_num_up)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.veh_num_save_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.veh_num_save_btn.setMinimumSize(QtCore.QSize(100, 0))
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
        self.horizontalLayout_5.addWidget(self.veh_num_save_btn)
        self.save_file_status = QtWidgets.QLineEdit(self.groupBox_3)
        self.save_file_status.setGeometry(QtCore.QRect(10, 80, 331, 41))
        self.save_file_status.setText("")
        self.save_file_status.setAlignment(QtCore.Qt.AlignCenter)
        self.save_file_status.setObjectName("save_file_status")
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
        self.label_4 = QtWidgets.QLabel(self.RDM_page)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.label_4.setObjectName("label_4")
        self.bgLabel = QtWidgets.QLabel(self.RDM_page)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgLabel.setMouseTracking(True)
        self.bgLabel.setObjectName("bgLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.RDM_page)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 70, 361, 391))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(12, 27, 331, 351))
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
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.tm1_temp_LCD = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.tm1_temp_LCD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tm1_temp_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tm1_temp_LCD.setLineWidth(1)
        self.tm1_temp_LCD.setSmallDecimalPoint(False)
        self.tm1_temp_LCD.setDigitCount(15)
        self.tm1_temp_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.tm1_temp_LCD.setObjectName("tm1_temp_LCD")
        self.gridLayout.addWidget(self.tm1_temp_LCD, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.tm1_motor_rpm_LCD = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.tm1_motor_rpm_LCD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tm1_motor_rpm_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tm1_motor_rpm_LCD.setLineWidth(1)
        self.tm1_motor_rpm_LCD.setSmallDecimalPoint(False)
        self.tm1_motor_rpm_LCD.setDigitCount(15)
        self.tm1_motor_rpm_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.tm1_motor_rpm_LCD.setObjectName("tm1_motor_rpm_LCD")
        self.gridLayout.addWidget(self.tm1_motor_rpm_LCD, 2, 1, 1, 1)
        self.tm2Label = QtWidgets.QLabel(self.layoutWidget1)
        self.tm2Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tm2Label.setObjectName("tm2Label")
        self.gridLayout.addWidget(self.tm2Label, 3, 0, 1, 1)
        self.tm2StatusBox = QtWidgets.QLineEdit(self.layoutWidget1)
        self.tm2StatusBox.setMouseTracking(False)
        self.tm2StatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.tm2StatusBox.setText("")
        self.tm2StatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.tm2StatusBox.setReadOnly(True)
        self.tm2StatusBox.setObjectName("tm2StatusBox")
        self.gridLayout.addWidget(self.tm2StatusBox, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.tm2_temp_LCD = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.tm2_temp_LCD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tm2_temp_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tm2_temp_LCD.setLineWidth(1)
        self.tm2_temp_LCD.setDigitCount(15)
        self.tm2_temp_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.tm2_temp_LCD.setObjectName("tm2_temp_LCD")
        self.gridLayout.addWidget(self.tm2_temp_LCD, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.tm2_motor_rpm_LCD = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.tm2_motor_rpm_LCD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tm2_motor_rpm_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tm2_motor_rpm_LCD.setLineWidth(1)
        self.tm2_motor_rpm_LCD.setSmallDecimalPoint(False)
        self.tm2_motor_rpm_LCD.setDigitCount(15)
        self.tm2_motor_rpm_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.tm2_motor_rpm_LCD.setObjectName("tm2_motor_rpm_LCD")
        self.gridLayout.addWidget(self.tm2_motor_rpm_LCD, 5, 1, 1, 1)
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
        self.inverterGroupdBox = QtWidgets.QGroupBox(self.RDM_page)
        self.inverterGroupdBox.setGeometry(QtCore.QRect(37, 170, 351, 71))
        self.inverterGroupdBox.setObjectName("inverterGroupdBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.inverterGroupdBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 25, 331, 34))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TM1_radio_btn = QtWidgets.QRadioButton(self.layoutWidget2)
        self.TM1_radio_btn.setEnabled(True)
        self.TM1_radio_btn.setObjectName("TM1_radio_btn")
        self.horizontalLayout_2.addWidget(self.TM1_radio_btn)
        self.TM2_radio_btn = QtWidgets.QRadioButton(self.layoutWidget2)
        self.TM2_radio_btn.setEnabled(True)
        self.TM2_radio_btn.setObjectName("TM2_radio_btn")
        self.horizontalLayout_2.addWidget(self.TM2_radio_btn)
        self.Both_radio_btn = QtWidgets.QRadioButton(self.layoutWidget2)
        self.Both_radio_btn.setEnabled(True)
        self.Both_radio_btn.setObjectName("Both_radio_btn")
        self.horizontalLayout_2.addWidget(self.Both_radio_btn)
        self.TorqueGroupdBox = QtWidgets.QGroupBox(self.RDM_page)
        self.TorqueGroupdBox.setGeometry(QtCore.QRect(37, 240, 351, 81))
        self.TorqueGroupdBox.setObjectName("TorqueGroupdBox")
        self.layoutWidget3 = QtWidgets.QWidget(self.TorqueGroupdBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(15, 23, 321, 47))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.torqueCmdMinus = QtWidgets.QPushButton(self.layoutWidget3)
        self.torqueCmdMinus.setMinimumSize(QtCore.QSize(50, 45))
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
        self.horizontalLayout_4.addWidget(self.torqueCmdMinus)
        self.torqueCmdBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.torqueCmdBox.setMinimumSize(QtCore.QSize(45, 45))
        self.torqueCmdBox.setText("")
        self.torqueCmdBox.setAlignment(QtCore.Qt.AlignCenter)
        self.torqueCmdBox.setObjectName("torqueCmdBox")
        self.horizontalLayout_4.addWidget(self.torqueCmdBox)
        self.torqueCmdPlus = QtWidgets.QPushButton(self.layoutWidget3)
        self.torqueCmdPlus.setMinimumSize(QtCore.QSize(50, 45))
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
        self.horizontalLayout_4.addWidget(self.torqueCmdPlus)
        self.groupBox_5 = QtWidgets.QGroupBox(self.RDM_page)
        self.groupBox_5.setGeometry(QtCore.QRect(37, 69, 351, 91))
        self.groupBox_5.setObjectName("groupBox_5")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget4.setGeometry(QtCore.QRect(11, 30, 331, 44))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.startStopBtn = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startStopBtn.setFont(font)
        self.startStopBtn.setStyleSheet("")
        self.startStopBtn.setObjectName("startStopBtn")
        self.horizontalLayout_6.addWidget(self.startStopBtn)
        self.enableBtn = QtWidgets.QPushButton(self.layoutWidget4)
        self.enableBtn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.enableBtn.setFont(font)
        self.enableBtn.setStyleSheet("")
        self.enableBtn.setObjectName("enableBtn")
        self.horizontalLayout_6.addWidget(self.enableBtn)
        self.bgLabel.raise_()
        self.groupBox_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.groupBox_2.raise_()
        self.epbBtn.raise_()
        self.menuBtn.raise_()
        self.inverterGroupdBox.raise_()
        self.TorqueGroupdBox.raise_()
        self.groupBox_5.raise_()
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
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 36, 641, 251))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LtActrStateLabel = QtWidgets.QLabel(self.layoutWidget5)
        self.LtActrStateLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LtActrStateLabel.setObjectName("LtActrStateLabel")
        self.gridLayout_3.addWidget(self.LtActrStateLabel, 0, 0, 1, 1)
        self.LtActrStateStatusBox = QtWidgets.QLineEdit(self.layoutWidget5)
        self.LtActrStateStatusBox.setMouseTracking(False)
        self.LtActrStateStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.LtActrStateStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.LtActrStateStatusBox.setReadOnly(True)
        self.LtActrStateStatusBox.setObjectName("LtActrStateStatusBox")
        self.gridLayout_3.addWidget(self.LtActrStateStatusBox, 0, 1, 1, 1)
        self.EpbSwLabel = QtWidgets.QLabel(self.layoutWidget5)
        self.EpbSwLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.EpbSwLabel.setObjectName("EpbSwLabel")
        self.gridLayout_3.addWidget(self.EpbSwLabel, 0, 2, 1, 1)
        self.EpbSwStatusBox = QtWidgets.QLineEdit(self.layoutWidget5)
        self.EpbSwStatusBox.setMouseTracking(False)
        self.EpbSwStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.EpbSwStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.EpbSwStatusBox.setReadOnly(True)
        self.EpbSwStatusBox.setObjectName("EpbSwStatusBox")
        self.gridLayout_3.addWidget(self.EpbSwStatusBox, 0, 3, 1, 1)
        self.RtActrStateLabel = QtWidgets.QLabel(self.layoutWidget5)
        self.RtActrStateLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RtActrStateLabel.setObjectName("RtActrStateLabel")
        self.gridLayout_3.addWidget(self.RtActrStateLabel, 1, 0, 1, 1)
        self.RtActrStateStatusBox = QtWidgets.QLineEdit(self.layoutWidget5)
        self.RtActrStateStatusBox.setMouseTracking(False)
        self.RtActrStateStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.RtActrStateStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.RtActrStateStatusBox.setReadOnly(True)
        self.RtActrStateStatusBox.setObjectName("RtActrStateStatusBox")
        self.gridLayout_3.addWidget(self.RtActrStateStatusBox, 1, 1, 1, 1)
        self.EpbFaultLabel = QtWidgets.QLabel(self.layoutWidget5)
        self.EpbFaultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.EpbFaultLabel.setObjectName("EpbFaultLabel")
        self.gridLayout_3.addWidget(self.EpbFaultLabel, 1, 2, 1, 1)
        self.EpbFaultStatusBox = QtWidgets.QLineEdit(self.layoutWidget5)
        self.EpbFaultStatusBox.setMouseTracking(False)
        self.EpbFaultStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.EpbFaultStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.EpbFaultStatusBox.setReadOnly(True)
        self.EpbFaultStatusBox.setObjectName("EpbFaultStatusBox")
        self.gridLayout_3.addWidget(self.EpbFaultStatusBox, 1, 3, 1, 1)
        self.LtActrFaultLabel = QtWidgets.QLabel(self.layoutWidget5)
        self.LtActrFaultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LtActrFaultLabel.setObjectName("LtActrFaultLabel")
        self.gridLayout_3.addWidget(self.LtActrFaultLabel, 2, 0, 1, 1)
        self.LtActrFaultStatusBox = QtWidgets.QLineEdit(self.layoutWidget5)
        self.LtActrFaultStatusBox.setMouseTracking(False)
        self.LtActrFaultStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.LtActrFaultStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.LtActrFaultStatusBox.setReadOnly(True)
        self.LtActrFaultStatusBox.setObjectName("LtActrFaultStatusBox")
        self.gridLayout_3.addWidget(self.LtActrFaultStatusBox, 2, 1, 1, 1)
        self.PGearLabel = QtWidgets.QLabel(self.layoutWidget5)
        self.PGearLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PGearLabel.setObjectName("PGearLabel")
        self.gridLayout_3.addWidget(self.PGearLabel, 2, 2, 1, 1)
        self.PGearStatusBox = QtWidgets.QLineEdit(self.layoutWidget5)
        self.PGearStatusBox.setMouseTracking(False)
        self.PGearStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.PGearStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PGearStatusBox.setReadOnly(True)
        self.PGearStatusBox.setObjectName("PGearStatusBox")
        self.gridLayout_3.addWidget(self.PGearStatusBox, 2, 3, 1, 1)
        self.RtActrFaultLabel = QtWidgets.QLabel(self.layoutWidget5)
        self.RtActrFaultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RtActrFaultLabel.setObjectName("RtActrFaultLabel")
        self.gridLayout_3.addWidget(self.RtActrFaultLabel, 3, 0, 1, 1)
        self.RtActrFaultStatusBox = QtWidgets.QLineEdit(self.layoutWidget5)
        self.RtActrFaultStatusBox.setMouseTracking(False)
        self.RtActrFaultStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.RtActrFaultStatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.RtActrFaultStatusBox.setReadOnly(True)
        self.RtActrFaultStatusBox.setObjectName("RtActrFaultStatusBox")
        self.gridLayout_3.addWidget(self.RtActrFaultStatusBox, 3, 1, 1, 1)
        self.PBrakeLabel = QtWidgets.QLabel(self.layoutWidget5)
        self.PBrakeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PBrakeLabel.setObjectName("PBrakeLabel")
        self.gridLayout_3.addWidget(self.PBrakeLabel, 3, 2, 1, 1)
        self.PBrakeStatusBox = QtWidgets.QLineEdit(self.layoutWidget5)
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
        self.label_8.setGeometry(QtCore.QRect(0, 50, 800, 70))
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
        self.Operator_page = QtWidgets.QWidget()
        self.Operator_page.setObjectName("Operator_page")
        self.bgLabel_6 = QtWidgets.QLabel(self.Operator_page)
        self.bgLabel_6.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgLabel_6.setMouseTracking(True)
        self.bgLabel_6.setObjectName("bgLabel_6")
        self.groupBox_16 = QtWidgets.QGroupBox(self.Operator_page)
        self.groupBox_16.setGeometry(QtCore.QRect(380, 90, 401, 321))
        self.groupBox_16.setObjectName("groupBox_16")
        self.layoutWidget_19 = QtWidgets.QWidget(self.groupBox_16)
        self.layoutWidget_19.setGeometry(QtCore.QRect(10, 20, 381, 291))
        self.layoutWidget_19.setObjectName("layoutWidget_19")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget_19)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.op_tm1StatusBox = QtWidgets.QLineEdit(self.layoutWidget_19)
        self.op_tm1StatusBox.setMouseTracking(False)
        self.op_tm1StatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.op_tm1StatusBox.setText("")
        self.op_tm1StatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.op_tm1StatusBox.setReadOnly(True)
        self.op_tm1StatusBox.setObjectName("op_tm1StatusBox")
        self.gridLayout_7.addWidget(self.op_tm1StatusBox, 0, 1, 1, 1)
        self.op_tm1_motor_rpm_LCD = QtWidgets.QLCDNumber(self.layoutWidget_19)
        self.op_tm1_motor_rpm_LCD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.op_tm1_motor_rpm_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.op_tm1_motor_rpm_LCD.setLineWidth(1)
        self.op_tm1_motor_rpm_LCD.setSmallDecimalPoint(False)
        self.op_tm1_motor_rpm_LCD.setDigitCount(15)
        self.op_tm1_motor_rpm_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.op_tm1_motor_rpm_LCD.setObjectName("op_tm1_motor_rpm_LCD")
        self.gridLayout_7.addWidget(self.op_tm1_motor_rpm_LCD, 2, 1, 1, 1)
        self.tm2Label_5 = QtWidgets.QLabel(self.layoutWidget_19)
        self.tm2Label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.tm2Label_5.setObjectName("tm2Label_5")
        self.gridLayout_7.addWidget(self.tm2Label_5, 3, 0, 1, 1)
        self.op_tm1_inv_temp_LCD = QtWidgets.QLCDNumber(self.layoutWidget_19)
        self.op_tm1_inv_temp_LCD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.op_tm1_inv_temp_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.op_tm1_inv_temp_LCD.setLineWidth(1)
        self.op_tm1_inv_temp_LCD.setSmallDecimalPoint(False)
        self.op_tm1_inv_temp_LCD.setDigitCount(15)
        self.op_tm1_inv_temp_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.op_tm1_inv_temp_LCD.setObjectName("op_tm1_inv_temp_LCD")
        self.gridLayout_7.addWidget(self.op_tm1_inv_temp_LCD, 1, 1, 1, 1)
        self.op_tm2_inv_temp_LCD = QtWidgets.QLCDNumber(self.layoutWidget_19)
        self.op_tm2_inv_temp_LCD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.op_tm2_inv_temp_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.op_tm2_inv_temp_LCD.setLineWidth(1)
        self.op_tm2_inv_temp_LCD.setDigitCount(15)
        self.op_tm2_inv_temp_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.op_tm2_inv_temp_LCD.setObjectName("op_tm2_inv_temp_LCD")
        self.gridLayout_7.addWidget(self.op_tm2_inv_temp_LCD, 4, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_19)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_7.addWidget(self.label_29, 2, 0, 1, 1)
        self.op_tm2StatusBox = QtWidgets.QLineEdit(self.layoutWidget_19)
        self.op_tm2StatusBox.setMouseTracking(False)
        self.op_tm2StatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.op_tm2StatusBox.setText("")
        self.op_tm2StatusBox.setAlignment(QtCore.Qt.AlignCenter)
        self.op_tm2StatusBox.setReadOnly(True)
        self.op_tm2StatusBox.setObjectName("op_tm2StatusBox")
        self.gridLayout_7.addWidget(self.op_tm2StatusBox, 3, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_19)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_7.addWidget(self.label_31, 5, 0, 1, 1)
        self.op_tm2_motor_rpm_LCD = QtWidgets.QLCDNumber(self.layoutWidget_19)
        self.op_tm2_motor_rpm_LCD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.op_tm2_motor_rpm_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.op_tm2_motor_rpm_LCD.setLineWidth(1)
        self.op_tm2_motor_rpm_LCD.setDigitCount(15)
        self.op_tm2_motor_rpm_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.op_tm2_motor_rpm_LCD.setObjectName("op_tm2_motor_rpm_LCD")
        self.gridLayout_7.addWidget(self.op_tm2_motor_rpm_LCD, 5, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_19)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_7.addWidget(self.label_30, 4, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_19)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_7.addWidget(self.label_28, 1, 0, 1, 1)
        self.tm1Label_5 = QtWidgets.QLabel(self.layoutWidget_19)
        self.tm1Label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.tm1Label_5.setObjectName("tm1Label_5")
        self.gridLayout_7.addWidget(self.tm1Label_5, 0, 0, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.Operator_page)
        self.groupBox_14.setGeometry(QtCore.QRect(30, 90, 331, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setObjectName("groupBox_14")
        self.layoutWidget_17 = QtWidgets.QWidget(self.groupBox_14)
        self.layoutWidget_17.setGeometry(QtCore.QRect(13, 30, 291, 37))
        self.layoutWidget_17.setObjectName("layoutWidget_17")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.layoutWidget_17)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_17)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_20.addWidget(self.label_14)
        self.test_result_label = QtWidgets.QLabel(self.layoutWidget_17)
        self.test_result_label.setText("")
        self.test_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.test_result_label.setObjectName("test_result_label")
        self.horizontalLayout_20.addWidget(self.test_result_label)
        self.LED = QtWidgets.QLabel(self.layoutWidget_17)
        self.LED.setMaximumSize(QtCore.QSize(100, 16777215))
        self.LED.setStyleSheet("QLabel#LED_1 {\n"
"    image: url(:/LED/LED_1_M.png);\n"
"}\n"
"")
        self.LED.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LED.setObjectName("LED")
        self.horizontalLayout_20.addWidget(self.LED)
        self.groupBox_15 = QtWidgets.QGroupBox(self.Operator_page)
        self.groupBox_15.setGeometry(QtCore.QRect(30, 190, 331, 141))
        self.groupBox_15.setObjectName("groupBox_15")
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox_15)
        self.layoutWidget6.setGeometry(QtCore.QRect(12, 27, 311, 44))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.op_veh_num_label = QtWidgets.QLineEdit(self.layoutWidget6)
        self.op_veh_num_label.setEnabled(True)
        self.op_veh_num_label.setMinimumSize(QtCore.QSize(150, 0))
        self.op_veh_num_label.setMaximumSize(QtCore.QSize(80, 45))
        self.op_veh_num_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.op_veh_num_label.setText("")
        self.op_veh_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.op_veh_num_label.setReadOnly(True)
        self.op_veh_num_label.setObjectName("op_veh_num_label")
        self.horizontalLayout_7.addWidget(self.op_veh_num_label)
        self.op_keypad_btn = QtWidgets.QPushButton(self.layoutWidget6)
        self.op_keypad_btn.setMinimumSize(QtCore.QSize(45, 0))
        self.op_keypad_btn.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.op_keypad_btn.setFont(font)
        self.op_keypad_btn.setDefault(False)
        self.op_keypad_btn.setFlat(False)
        self.op_keypad_btn.setObjectName("op_keypad_btn")
        self.horizontalLayout_7.addWidget(self.op_keypad_btn)
        self.op_veh_num_save_btn = QtWidgets.QPushButton(self.layoutWidget6)
        self.op_veh_num_save_btn.setMinimumSize(QtCore.QSize(90, 0))
        self.op_veh_num_save_btn.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.op_veh_num_save_btn.setFont(font)
        self.op_veh_num_save_btn.setDefault(False)
        self.op_veh_num_save_btn.setFlat(False)
        self.op_veh_num_save_btn.setObjectName("op_veh_num_save_btn")
        self.horizontalLayout_7.addWidget(self.op_veh_num_save_btn)
        self.op_save_file_status = QtWidgets.QLineEdit(self.groupBox_15)
        self.op_save_file_status.setEnabled(True)
        self.op_save_file_status.setGeometry(QtCore.QRect(11, 79, 311, 51))
        self.op_save_file_status.setText("")
        self.op_save_file_status.setAlignment(QtCore.Qt.AlignCenter)
        self.op_save_file_status.setReadOnly(True)
        self.op_save_file_status.setObjectName("op_save_file_status")
        self.auto_test_btn = QtWidgets.QPushButton(self.Operator_page)
        self.auto_test_btn.setGeometry(QtCore.QRect(30, 360, 331, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.auto_test_btn.setFont(font)
        self.auto_test_btn.setStyleSheet("")
        self.auto_test_btn.setObjectName("auto_test_btn")
        self.op_epbBtn = QtWidgets.QPushButton(self.Operator_page)
        self.op_epbBtn.setGeometry(QtCore.QRect(740, 6, 40, 40))
        self.op_epbBtn.setStyleSheet("QPushButton {\n"
"    border-image: url(:/epb_graphics/graphics/epb_normal.png);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/epb_graphics/graphics/epb_pressed.png);\n"
"}")
        self.op_epbBtn.setText("")
        self.op_epbBtn.setIconSize(QtCore.QSize(50, 50))
        self.op_epbBtn.setFlat(True)
        self.op_epbBtn.setObjectName("op_epbBtn")
        self.label_10 = QtWidgets.QLabel(self.Operator_page)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 800, 81))
        self.label_10.setObjectName("label_10")
        self.progressBar = QtWidgets.QProgressBar(self.Operator_page)
        self.progressBar.setGeometry(QtCore.QRect(30, 430, 741, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(self.Operator_page)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.label_6.setObjectName("label_6")
        self.bgLabel_6.raise_()
        self.label_10.raise_()
        self.label_6.raise_()
        self.groupBox_16.raise_()
        self.groupBox_14.raise_()
        self.groupBox_15.raise_()
        self.auto_test_btn.raise_()
        self.progressBar.raise_()
        self.op_epbBtn.raise_()
        self.stackedWidget.addWidget(self.Operator_page)
        self.VIN_num_page = QtWidgets.QWidget()
        self.VIN_num_page.setObjectName("VIN_num_page")
        self.bgLabel_8 = QtWidgets.QLabel(self.VIN_num_page)
        self.bgLabel_8.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgLabel_8.setMouseTracking(True)
        self.bgLabel_8.setObjectName("bgLabel_8")
        self.number_pad = QtWidgets.QGroupBox(self.VIN_num_page)
        self.number_pad.setGeometry(QtCore.QRect(240, 60, 331, 341))
        self.number_pad.setTitle("")
        self.number_pad.setObjectName("number_pad")
        self.vin_num_box = QtWidgets.QLineEdit(self.number_pad)
        self.vin_num_box.setGeometry(QtCore.QRect(20, 20, 291, 51))
        self.vin_num_box.setText("")
        self.vin_num_box.setAlignment(QtCore.Qt.AlignCenter)
        self.vin_num_box.setReadOnly(True)
        self.vin_num_box.setObjectName("vin_num_box")
        self.layoutWidget7 = QtWidgets.QWidget(self.number_pad)
        self.layoutWidget7.setGeometry(QtCore.QRect(20, 70, 291, 271))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget7)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_0 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout_4.addWidget(self.btn_0, 3, 1, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_4.addWidget(self.btn_8, 2, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_4.addWidget(self.btn_9, 2, 2, 1, 1)
        self.btn_DEL = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_DEL.setObjectName("btn_DEL")
        self.gridLayout_4.addWidget(self.btn_DEL, 3, 0, 1, 1)
        self.btn_OK = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_OK.setObjectName("btn_OK")
        self.gridLayout_4.addWidget(self.btn_OK, 3, 2, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_4.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_4.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_4.addWidget(self.btn_3, 0, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_4.addWidget(self.btn_2, 0, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_4.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_4.addWidget(self.btn_7, 2, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_4.addWidget(self.btn_1, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.VIN_num_page)
        self.Assign_ID_page = QtWidgets.QWidget()
        self.Assign_ID_page.setObjectName("Assign_ID_page")
        self.label_7 = QtWidgets.QLabel(self.Assign_ID_page)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.label_7.setObjectName("label_7")
        self.bgLabel_7 = QtWidgets.QLabel(self.Assign_ID_page)
        self.bgLabel_7.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgLabel_7.setMouseTracking(True)
        self.bgLabel_7.setObjectName("bgLabel_7")
        self.label_11 = QtWidgets.QLabel(self.Assign_ID_page)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 800, 81))
        self.label_11.setObjectName("label_11")
        self.groupBox_17 = QtWidgets.QGroupBox(self.Assign_ID_page)
        self.groupBox_17.setGeometry(QtCore.QRect(80, 120, 651, 321))
        self.groupBox_17.setTitle("")
        self.groupBox_17.setObjectName("groupBox_17")
        self.layoutWidget8 = QtWidgets.QWidget(self.groupBox_17)
        self.layoutWidget8.setGeometry(QtCore.QRect(12, 22, 631, 281))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget8)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_32 = QtWidgets.QLabel(self.layoutWidget8)
        self.label_32.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 0, 0, 1, 1)
        self.ID_to_assign = QtWidgets.QLineEdit(self.layoutWidget8)
        self.ID_to_assign.setMinimumSize(QtCore.QSize(0, 0))
        self.ID_to_assign.setMaximumSize(QtCore.QSize(500, 500))
        self.ID_to_assign.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ID_to_assign.setText("")
        self.ID_to_assign.setAlignment(QtCore.Qt.AlignCenter)
        self.ID_to_assign.setObjectName("ID_to_assign")
        self.gridLayout_2.addWidget(self.ID_to_assign, 0, 1, 1, 1)
        self.ID_down_btn = QtWidgets.QPushButton(self.layoutWidget8)
        self.ID_down_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.ID_down_btn.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ID_down_btn.setFont(font)
        self.ID_down_btn.setDefault(False)
        self.ID_down_btn.setFlat(False)
        self.ID_down_btn.setObjectName("ID_down_btn")
        self.gridLayout_2.addWidget(self.ID_down_btn, 0, 2, 1, 1)
        self.ID_up_btn = QtWidgets.QPushButton(self.layoutWidget8)
        self.ID_up_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.ID_up_btn.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ID_up_btn.setFont(font)
        self.ID_up_btn.setDefault(False)
        self.ID_up_btn.setFlat(False)
        self.ID_up_btn.setObjectName("ID_up_btn")
        self.gridLayout_2.addWidget(self.ID_up_btn, 0, 3, 1, 1)
        self.OK_btn = QtWidgets.QPushButton(self.layoutWidget8)
        self.OK_btn.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OK_btn.setFont(font)
        self.OK_btn.setDefault(False)
        self.OK_btn.setFlat(False)
        self.OK_btn.setObjectName("OK_btn")
        self.gridLayout_2.addWidget(self.OK_btn, 0, 4, 1, 1)
        self.status_box = QtWidgets.QLineEdit(self.layoutWidget8)
        self.status_box.setMinimumSize(QtCore.QSize(0, 0))
        self.status_box.setMaximumSize(QtCore.QSize(700, 500))
        self.status_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_box.setText("")
        self.status_box.setAlignment(QtCore.Qt.AlignCenter)
        self.status_box.setObjectName("status_box")
        self.gridLayout_2.addWidget(self.status_box, 1, 0, 1, 5)
        self.shut_down_btn = QtWidgets.QPushButton(self.Assign_ID_page)
        self.shut_down_btn.setGeometry(QtCore.QRect(640, 10, 150, 42))
        self.shut_down_btn.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.shut_down_btn.setFont(font)
        self.shut_down_btn.setDefault(False)
        self.shut_down_btn.setFlat(False)
        self.shut_down_btn.setObjectName("shut_down_btn")
        self.bgLabel_7.raise_()
        self.label_11.raise_()
        self.label_7.raise_()
        self.groupBox_17.raise_()
        self.shut_down_btn.raise_()
        self.stackedWidget.addWidget(self.Assign_ID_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Vehicle in Test"))
        self.label_5.setText(_translate("MainWindow", "PV"))
        self.veh_num_down.setText(_translate("MainWindow", "<"))
        self.veh_num_up.setText(_translate("MainWindow", ">"))
        self.veh_num_save_btn.setText(_translate("MainWindow", "SAVE"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">RDM Bench</span></p></body></html>"))
        self.bgLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status"))
        self.tm1Label.setText(_translate("MainWindow", "TM1 Status"))
        self.label.setText(_translate("MainWindow", "TM1 Temp"))
        self.label_13.setText(_translate("MainWindow", "TM1 RPM"))
        self.tm2Label.setText(_translate("MainWindow", "TM2 Status"))
        self.label_2.setText(_translate("MainWindow", "TM2 Inv Temp"))
        self.label_12.setText(_translate("MainWindow", "TM2 RPM"))
        self.inverterGroupdBox.setTitle(_translate("MainWindow", "Inverter Set"))
        self.TM1_radio_btn.setText(_translate("MainWindow", "TM1 Only"))
        self.TM2_radio_btn.setText(_translate("MainWindow", "TM2 Only"))
        self.Both_radio_btn.setText(_translate("MainWindow", "Both"))
        self.TorqueGroupdBox.setTitle(_translate("MainWindow", "Torque Control"))
        self.torqueCmdMinus.setText(_translate("MainWindow", "-"))
        self.torqueCmdPlus.setText(_translate("MainWindow", "+"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Control"))
        self.startStopBtn.setText(_translate("MainWindow", "Start"))
        self.enableBtn.setText(_translate("MainWindow", "Enable"))
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
        self.bgLabel_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Status"))
        self.tm2Label_5.setText(_translate("MainWindow", "TM2 Status"))
        self.label_29.setText(_translate("MainWindow", "TM1 Motor RPM"))
        self.label_31.setText(_translate("MainWindow", "TM2 Motor RPM"))
        self.label_30.setText(_translate("MainWindow", "TM2 Inv Temp"))
        self.label_28.setText(_translate("MainWindow", "TM1 Inv Temp"))
        self.tm1Label_5.setText(_translate("MainWindow", "TM1 Status"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Test Profiles:"))
        self.label_14.setText(_translate("MainWindow", "  TEST RESULT:"))
        self.LED.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/LED/graphics/grey_led.png\"/></p></body></html>"))
        self.groupBox_15.setTitle(_translate("MainWindow", "VIN"))
        self.op_keypad_btn.setText(_translate("MainWindow", "..."))
        self.op_veh_num_save_btn.setText(_translate("MainWindow", "SAVE"))
        self.auto_test_btn.setText(_translate("MainWindow", "Auto Test"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">RDM Bench</span></p></body></html>"))
        self.bgLabel_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_DEL.setText(_translate("MainWindow", "DEL"))
        self.btn_OK.setText(_translate("MainWindow", "OK"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Assign Inverter ID</p></body></html>"))
        self.bgLabel_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "Choose ID to assign:"))
        self.ID_down_btn.setText(_translate("MainWindow", "<"))
        self.ID_up_btn.setText(_translate("MainWindow", ">"))
        self.OK_btn.setText(_translate("MainWindow", "OK"))
        self.shut_down_btn.setText(_translate("MainWindow", "Shut down"))

import rdm_graphics_rc
