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

from PySide2.QtWidgets import  QMainWindow, QMessageBox
from PySide2.QtCore import  Slot
from ui.gui_main_interface import Ui_main_interface
import cv2

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
        self._connect_slot()

    def _connect_slot(self):
        self.ui.btn_start.clicked.connect(self._run_start_ie)

    @Slot()
    def _run_start_ie(self):
        # 从 self.ui.le_cam_index 获取摄像头索引
        index = eval(self.ui.le_cam_index.text())
        # 打开摄像头
        cap = cv2.VideoCapture(index)

        if cap.isOpened() == False:
            print("打开摄像头失败")
            QMessageBox.warning(self, "警告", "打开摄像头失败")


        

