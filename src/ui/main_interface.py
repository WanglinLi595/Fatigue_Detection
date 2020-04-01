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
from PySide2.QtCore import  Slot, QTimer
from PySide2.QtGui import QPixmap, QImage
from ui.gui_main_interface import Ui_main_interface
from vino.vino import model_optimazor
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
        
        model_xml = r"E:\model\face-detection-adas-binary-0001\FP32-INT1\face-detection-adas-binary-0001.xml"
        model_bin = r"E:\model\face-detection-adas-binary-0001\FP32-INT1\face-detection-adas-binary-0001.bin"

        # 创建 model_optimazor
        self._ie = model_optimazor()
        self._ie.load_module_file(model_xml, model_bin)

        # 新建定时器
        self._timer = QTimer()

        self._connect_slot()

    def _connect_slot(self):
        self.ui.btn_start.clicked.connect(self._run_start_ie)
        self._timer.timeout.connect(self._display)

    @Slot()
    def _run_start_ie(self):
        # 从 self.ui.le_cam_index 获取摄像头索引
        index = eval(self.ui.le_cam_index.text())
        # 打开摄像头
        # self._cap = cv2.VideoCapture(r"C:\Users\LWL\Desktop\sample-videos-master\face-demographics-walking.mp4")
        self._cap = cv2.VideoCapture(0)
        # if cap.isOpened() == False:
        #     print("打开摄像头失败")
        #     QMessageBox.warning(self, "警告", "打开摄像头失败")
        self._timer.start(10)

        

    def _display(self):
        ret, self._frame = self._cap.read()
        frame = self._ie.run_ie(self._frame)

        h, w = frame.shape[:2]
        temp_q_image = QImage(frame.data, w, h, QImage.Format_BGR888)
        #  在 lb_display 中显示图片
        self.ui.lb_display.setPixmap(QPixmap.fromImage(temp_q_image))
        # cv2.imshow("res", frame)

        




        

