#!/usr/bin/env python
# coding=utf-8
'''
@描述: 
@版本: V1_0
@作者: LiWanglin
@创建时间: Do not edit
@最后编辑人: LiWanglin
@最后编辑时间: Do not Edit
'''

from PyQt5.QtWidgets import  QMainWindow, QMessageBox
from PyQt5.QtCore import  QTimer, pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
from ui.gui_main_interface import Ui_main_interface
import cv2
from get_data.get_data import GetData

class MainInterface(QMainWindow):
    '''主界面类，用来组织所有的功能
        
    @属性说明: 
    # TODO

    @方法说明: 
    # TODO
    '''   

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_main_interface()
        self.ui.setupUi(self)

        self.time = QTimer()
        
        self._connect_slot()

    def _connect_slot(self):
        self.ui.btn_start.clicked.connect(self._display)
        self.time.timeout.connect(self.test)

    @pyqtSlot(bool)
    def _display(self, checked):
        self.facial_data = GetData()
        self.time.start(1000)
        if(checked==False):
            self.time.stop()

    def test(self):
        frame = self.facial_data.get_frame()
        facial_keypoints = self.facial_data.get_result(frame)
        
        

        




        

