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
import numpy as np
import tensorflow as tf
from tensorflow import keras

class GetData():
    def __init__(self, tf_model, cap_index=0):
        self.model = tf.keras.models.load_model(tf_model)
        self._cap = cv.VideoCapture(cap_index)
        if(self._cap.isOpened==False):
            return -1

    def get_frame(self):
        ret, frame = self._cap.read()
        if(ret==False):
            return -1
        return frame

    def process_frame(self, frame):
        frame = cv.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        image = cv.resize(image, (120, 120))
        image = np.reshape(image, [1, 120, 120, 1])
        image = image / 255.
        return image

    def get_result(self, frame):
        facial_keypoints = self.model.predict(frame)
        return facial_keypoints
