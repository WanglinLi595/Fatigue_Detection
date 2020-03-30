# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_main_interface(object):
    def setupUi(self, main_interface):
        if main_interface.objectName():
            main_interface.setObjectName(u"main_interface")
        main_interface.resize(865, 671)
        self.centralwidget = QWidget(main_interface)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_display = QLabel(self.centralwidget)
        self.lb_display.setObjectName(u"lb_display")
        self.lb_display.setGeometry(QRect(9, 9, 62, 16))
        self.lb_display.setFrameShape(QFrame.Panel)
        self.lb_display.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(642, 301, 135, 69))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.le_cam_index = QLineEdit(self.widget)
        self.le_cam_index.setObjectName(u"le_cam_index")

        self.verticalLayout.addWidget(self.le_cam_index)

        self.btn_start = QPushButton(self.widget)
        self.btn_start.setObjectName(u"btn_start")

        self.verticalLayout.addWidget(self.btn_start)

        main_interface.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_interface)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 865, 23))
        main_interface.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_interface)
        self.statusbar.setObjectName(u"statusbar")
        main_interface.setStatusBar(self.statusbar)

        self.retranslateUi(main_interface)

        QMetaObject.connectSlotsByName(main_interface)
    # setupUi

    def retranslateUi(self, main_interface):
        main_interface.setWindowTitle(QCoreApplication.translate("main_interface", u"MainWindow", None))
        self.lb_display.setText(QCoreApplication.translate("main_interface", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("main_interface", u"\u6444\u50cf\u5934\u7d22\u5f15\uff1a", None))
        self.btn_start.setText(QCoreApplication.translate("main_interface", u"\u542f\u52a8", None))
    # retranslateUi

