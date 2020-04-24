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
        main_interface.resize(865, 671)
        self.centralwidget = QtWidgets.QWidget(main_interface)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_display = QtWidgets.QLabel(self.centralwidget)
        self.lb_display.setFrameShape(QtWidgets.QFrame.Panel)
        self.lb_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lb_display.setObjectName("lb_display")
        self.horizontalLayout.addWidget(self.lb_display)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.le_cam_index = QtWidgets.QLineEdit(self.centralwidget)
        self.le_cam_index.setObjectName("le_cam_index")
        self.verticalLayout.addWidget(self.le_cam_index)
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn_start.setCheckable(True)
        self.btn_start.setFlat(False)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout.addWidget(self.btn_start)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 1)
        main_interface.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_interface)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 865, 23))
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
        self.lb_display.setText(_translate("main_interface", "TextLabel"))
        self.label.setText(_translate("main_interface", "摄像头索引："))
        self.btn_start.setText(_translate("main_interface", "启动"))

