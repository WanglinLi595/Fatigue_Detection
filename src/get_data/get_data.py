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
        self._cap = cv.VideoCapture(r"C:\Users\LWL\Pictures\Camera Roll\WIN_20200503_07_51_19_Pro.mp4")
        # self._cap = cv.VideoCapture(0)
        if(self._cap.isOpened==False):
            return -1

    def get_frame(self):
        ret, frame = self._cap.read()
        if(ret==False):
            return -1
        return frame

    def get_facial(self, frame):
        # 人脸检测模型网络
        face_cascade = cv.CascadeClassifier(r"D:\anaconda\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
        face = frame     # 读取图片数据
        image_h, image_w = face.shape[:2]
        gray=cv.cvtColor(face, cv.COLOR_BGR2GRAY)      # 灰度图转换
        faces = face_cascade.detectMultiScale(gray,1.1,5) # 检测人脸
        if(faces.shape != (1, 4)):       # 只检测一张人脸
            return -1, ()
        else:
            x,y,w,h = faces[0]   # 获取人脸范围
            # 扩大人脸范围
            x_min = 0 if x-50<0 else x-50
            x_max = image_w if x+w+50>image_w else x+w+50
            y_min = 0 if y-50<0 else y-50
            y_max = image_h if y+h+50>image_h else y+h+50
            return 0, [x_min, x_max, y_min, y_max]         # 返回扩大的人脸范围


    def process_frame(self, frame):
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        image = cv.resize(image, (150, 150))
        image = np.reshape(image, [1, 150, 150, 1])
        image = image / 255.
        return image

    def get_result(self, frame):
        facial_keypoints = self.model.predict(frame)
        return facial_keypoints
