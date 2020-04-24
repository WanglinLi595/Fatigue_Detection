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
        self._tf_model = tf_model

        self._cap = cv.VideoCapture(cap_index)

        if(self._cap.isOpened==False):
            QMessageBox.critical(self, "警告", "相机打开失败")

    def get_frame(self):
        ret, frame = self._cap.read()
        if(ret==False):
            QMessageBox.critical(self, "警告", "未获取帧")
        return frame

    def get_result(self):
        facial_keypoints = tf.keras.models.load_model("self._tf_model")
        return facial_keypoints
