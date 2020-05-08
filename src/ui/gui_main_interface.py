# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Fatigue_Detection\src\ui\main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_interface(object):
    def setupUi(self, main_interface):
        main_interface.setObjectName("main_interface")
        main_interface.resize(1135, 887)
        self.centralwidget = QtWidgets.QWidget(main_interface)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_display = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.lb_display.setFont(font)
        self.lb_display.setAutoFillBackground(False)
        self.lb_display.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lb_display.setFrameShape(QtWidgets.QFrame.Panel)
        self.lb_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lb_display.setText("")
        self.lb_display.setScaledContents(False)
        self.lb_display.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_display.setObjectName("lb_display")
        self.horizontalLayout.addWidget(self.lb_display)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lb_fatigue_detection = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.lb_fatigue_detection.setFont(font)
        self.lb_fatigue_detection.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lb_fatigue_detection.setFrameShape(QtWidgets.QFrame.Panel)
        self.lb_fatigue_detection.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_fatigue_detection.setObjectName("lb_fatigue_detection")
        self.verticalLayout_2.addWidget(self.lb_fatigue_detection)
        self.verticalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.lb_facial_number = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.lb_facial_number.setFont(font)
        self.lb_facial_number.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lb_facial_number.setFrameShape(QtWidgets.QFrame.Panel)
        self.lb_facial_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_facial_number.setObjectName("lb_facial_number")
        self.verticalLayout_4.addWidget(self.lb_facial_number)
        self.verticalLayout_11.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.lb_left_eye_figure = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.lb_left_eye_figure.setFont(font)
        self.lb_left_eye_figure.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lb_left_eye_figure.setFrameShape(QtWidgets.QFrame.Panel)
        self.lb_left_eye_figure.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_left_eye_figure.setObjectName("lb_left_eye_figure")
        self.verticalLayout_5.addWidget(self.lb_left_eye_figure)
        self.verticalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.lb_right_eye_figure = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.lb_right_eye_figure.setFont(font)
        self.lb_right_eye_figure.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lb_right_eye_figure.setFrameShape(QtWidgets.QFrame.Panel)
        self.lb_right_eye_figure.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_right_eye_figure.setObjectName("lb_right_eye_figure")
        self.verticalLayout_10.addWidget(self.lb_right_eye_figure)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.le_eye_threshold = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.le_eye_threshold.setFont(font)
        self.le_eye_threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.le_eye_threshold.setObjectName("le_eye_threshold")
        self.verticalLayout_11.addWidget(self.le_eye_threshold)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.cmb_cap_index = QtWidgets.QComboBox(self.groupBox_2)
        self.cmb_cap_index.setEnabled(True)
        self.cmb_cap_index.setObjectName("cmb_cap_index")
        self.cmb_cap_index.addItem("")
        self.cmb_cap_index.addItem("")
        self.cmb_cap_index.addItem("")
        self.cmb_cap_index.addItem("")
        self.cmb_cap_index.addItem("")
        self.cmb_cap_index.addItem("")
        self.horizontalLayout_3.addWidget(self.cmb_cap_index)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.btn_start = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn_start.setCheckable(True)
        self.btn_start.setFlat(False)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout_11.addWidget(self.btn_start)
        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 1)
        self.verticalLayout_11.setStretch(2, 1)
        self.verticalLayout_11.setStretch(3, 1)
        self.verticalLayout_11.setStretch(6, 2)
        self.verticalLayout_11.setStretch(7, 1)
        self.verticalLayout_11.setStretch(8, 1)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.verticalLayout_7.setStretch(0, 6)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(0, 7)
        self.verticalLayout_3.setStretch(1, 3)
        main_interface.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_interface)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1135, 23))
        self.menubar.setObjectName("menubar")
        main_interface.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_interface)
        self.statusbar.setObjectName("statusbar")
        main_interface.setStatusBar(self.statusbar)

        self.retranslateUi(main_interface)
        QtCore.QMetaObject.connectSlotsByName(main_interface)

    def retranslateUi(self, main_interface):
        _translate = QtCore.QCoreApplication.translate
        main_interface.setWindowTitle(_translate("main_interface", "MainWindow"))
        self.label_2.setText(_translate("main_interface", "疲劳状态："))
        self.lb_fatigue_detection.setText(_translate("main_interface", "未开始检测"))
        self.label_3.setText(_translate("main_interface", "人脸检测数"))
        self.lb_facial_number.setText(_translate("main_interface", "未开始检测"))
        self.label_4.setText(_translate("main_interface", "左眼计算值："))
        self.lb_left_eye_figure.setText(_translate("main_interface", "未开始检测"))
        self.label_11.setText(_translate("main_interface", "左眼计算值："))
        self.lb_right_eye_figure.setText(_translate("main_interface", "未开始检测"))
        self.label_5.setText(_translate("main_interface", "睁闭眼阈值设置："))
        self.le_eye_threshold.setText(_translate("main_interface", "0.3"))
        self.label.setText(_translate("main_interface", "摄像头索引："))
        self.cmb_cap_index.setItemText(0, _translate("main_interface", "0"))
        self.cmb_cap_index.setItemText(1, _translate("main_interface", "1"))
        self.cmb_cap_index.setItemText(2, _translate("main_interface", "2"))
        self.cmb_cap_index.setItemText(3, _translate("main_interface", "3"))
        self.cmb_cap_index.setItemText(4, _translate("main_interface", "4"))
        self.cmb_cap_index.setItemText(5, _translate("main_interface", "5"))
        self.btn_start.setText(_translate("main_interface", "启动"))

