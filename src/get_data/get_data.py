#!/usr/bin/env python
# coding=utf-8
'''
@描述: 获取数据
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.04.23
@最后编辑人: LiWanglin
@最后编辑时间: 2020.04.23
'''

import cv2 as cv
from PyQt5.QtWidgets import QMessageBox
import tensorflow as tf
from tensorflow import keras

class GetData():
    def __init__(self, tf_model, cap_index=0):
        print("正在载入模型成功")
        self.model = tf.keras.models.load_model(tf_model)
        print("载入模型成功")
        self._cap = cv.VideoCapture(cap_index)
        if(self._cap.isOpened==False):
            QMessageBox.critical(self, "警告", "相机打开失败")

    def get_frame(self):
        ret, frame = self._cap.read()
        if(ret==False):
            QMessageBox.critical(self, "警告", "未获取帧")
        return frame

    def get_result(self, frame):
        facial_keypoints = self.model.predict(frame)
        return facial_keypoints
