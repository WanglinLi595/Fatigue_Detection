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
from PyQt5.QtChart import QChartView, QChart, QLineSeries, QValueAxis
from ui.gui_main_interface import Ui_main_interface
import cv2
from get_data.get_data import GetData
import numpy as np
from result_process import result_process


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
        model_path = r"E:\tensorflow_usage_flow"
        self.facial_data = GetData(tf_model=model_path)
        self.time.start(1000)
        if(checked==False):
            self.time.stop()

    def test(self):
        frame = self.facial_data.get_frame()
        frame = cv2.medianBlur(frame, 5)
        ret, rect = self.facial_data.get_facial(frame)
        # x_min, x_max, y_min, y_max = self.facial_data.get_facial(frame)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        if(ret == -1):
            h, w = frame.shape[:2]
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            temp_q_image = QImage(frame, w, h, QImage.Format_RGB888)
            #  在 lb_display 中显示图片
            self.ui.lb_display.setPixmap(QPixmap.fromImage(temp_q_image))
            print("未检测到人脸")
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            print(rect[0],rect[1], rect[2],rect[3])
            facial = frame[rect[2]:rect[3], rect[0]:rect[1]]

            image = cv2.cvtColor(facial, cv2.COLOR_RGB2GRAY)
            image_h, image_w = image.shape[:2]
            image = cv2.resize(image , (150, 150))
            image = np.reshape(image, [1, 150, 150, 1])
            image = image / 255.
            facial_keypoints = self.facial_data.get_result(image)
            facial_keypoints = (facial_keypoints[0] + 1) / 2
            facial_keypoints[::2] = facial_keypoints[::2] * image_w + rect[0]
            facial_keypoints[1::2] = facial_keypoints[1::2] * image_h + rect[2]
            
            # 圈出人脸范围
            facial = cv2.rectangle(frame, (rect[0],rect[2]), (rect[1],rect[3]), (255,0,0), 1)
            for i in range(12):
                facial = cv2.circle(frame, (int(facial_keypoints[2*i]), int(facial_keypoints[2*i+1])), 2, (255, 0, 0), -1)   # 进行打点
            a = result_process.eyes_process(facial_keypoints)
            print(a)
            h, w = facial.shape[:2]
            temp_q_image = QImage(facial.data, w, h, QImage.Format_RGB888)
            #  在 lb_display 中显示图片
            self.ui.lb_display.setPixmap(QPixmap.fromImage(temp_q_image))


            # image = cv2.resize(facial, (150, 150))
            # image = np.reshape(image, [1, 150, 150, 1])
            # image = image / 255.
            # facial_keypoints = self.facial_data.get_result(image)
            # print(facial_keypoints)
            # h, w = frame.shape[:2]
            # facial_keypoints = (facial_keypoints + 1) / 2
            # facial_keypoints[::2] = facial_keypoints[::2] * w
            # facial_keypoints[1::2] = facial_keypoints[1::2] * h
            # for i in range(12):
            #     cv2.circle(frame, (int(facial_keypoints[0, 2*i]), int(facial_keypoints[0, 2*i+1])), 2, (255, 0, 0), -1)   # 进行打点
            # print(facial_keypoints)
            # temp_q_image = QImage(frame.data, w, h, QImage.Format_RGB888)
            # #  在 lb_display 中显示图片
            # self.ui.lb_display.setPixmap(QPixmap.fromImage(temp_q_image))
        

        




        

