#!/usr/bin/env python
# coding=utf-8
'''
@描述: 获取人脸多特征点数据
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.04.23
@最后编辑人: LiWanglin
@最后编辑时间: 2020.05.05
'''

import cv2 as cv
import numpy as np
import tensorflow as tf
from tensorflow import keras

class GetFacialData():
    '''获取人脸多特征点数据

    @属性说明: 
        self._model：人脸多特征点检测神经网络模型
        self._cap：VideoCapture 类，用来获取摄像头数据


    @方法说明: 
        get_frame()：获取通过摄像头的图片数据
        get_facial()：人脸检测
        process_frame()：处理图片数据
        get_result()：对输入的图片进行预测，得到人脸多特征点数据

    @注意: 
        暂无
    '''
    def __init__(self, tf_model, facial_model_file, cap_index=0):
        '''完成初始化工作

        @参数说明: 
            tf_model：人脸多特征点检测神经网络模型
            facial_model_file：OpenCV人脸检测模型文件

        @返回值: 
            无

        @注意: 

        '''
        self._model = tf.keras.models.load_model(tf_model)       # 载入人脸多特征点检测神经网络模型
        self._cap = cv.VideoCapture(cap_index)                  # 创建 VideoCapture 类，用来获取摄像头数据
        # 改变摄像头分辨率
        self._cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280) #宽度
        self._cap.set(cv.CAP_PROP_FRAME_HEIGHT, 960) #高度
        self._face_cascade = cv.CascadeClassifier(facial_model_file)        # OpenCV 中的级联分类器

    def get_frame(self):
        '''获取通过摄像头的图片数据

        @参数说明: 
            无

        @返回值: 
            -1：摄像头打开失败
            -2：未获取摄像头的数据
            frame：通过获取摄像头的图片数据

        @注意: 
            暂无
        '''
        if(self._cap.isOpened==False):      # 判断摄像头是否打开成功
            return -1, []
        ret, frame = self._cap.read()       # 读取摄像头数据
        if(ret==False):                     # 判读数据是否读取成功
            return -2, []
        return 0, frame                        # 返回摄像头获取的图片数据

    def get_facial(self, frame):
        '''人脸检测

        通过 OpenCV 中的工具检测图片中的人脸

        @参数说明: 
            frame：要检测人脸的图片数据

        @返回值: 
            如果图片中只检测出一个人脸，返回 0 以及扩大范围获得人脸区域
            如果不是检测一个人脸，返回 -1 以及检测的人脸个数

        @注意: 
            暂无
        '''
        # 人脸检测模型网络
        face = frame     # 读取图片数据
        image_h, image_w = face.shape[:2]               
        gray=cv.cvtColor(face, cv.COLOR_BGR2GRAY)      # 灰度图转换
        faces = self._face_cascade.detectMultiScale(gray,1.1,5) # 检测人脸
        if(len(faces) != 1):       # 只检测一张人脸
            return -1, len(faces)
        else:
            x,y,w,h = faces[0]   # 获取人脸范围
            # 扩大人脸范围，可以提高人脸多特征点检测效果
            x_min = 0 if x-50<0 else x-50
            x_max = image_w if x+w+50>image_w else x+w+50
            y_min = 0 if y-50<0 else y-50
            y_max = image_h if y+h+50>image_h else y+h+50
            return 0, [x_min, x_max, y_min, y_max]         # 返回扩大的人脸范围


    def process_frame(self, frame):
        '''处理图片数据

        对传入的图片进行灰度转换，尺寸变换，维度变换以及数据归一化，处理后的数据可直接进行预测

        @参数说明: 
            frame：要处理的图片数据 

        @返回值: 
            image：处理后的图片数据

        @注意: 
            暂无
        '''
        image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)           # 转化为灰度图
        image = cv.resize(image, (150, 150))                    # 改变图片尺寸
        image = np.reshape(image, [1, 150, 150, 1])             # 改变图片数据维度
        image = image / 255.                                    # 数据归一化处理
        return image

    def get_result(self, frame_data):
        '''对输入的图片进行预测，得到人脸多特征点数据

        经过 process_frame() 方法处理后的图片数据，可以通过此方法获取人脸多特征点数据

        @参数说明: 
            frame_data：经过 process_frame() 方法处理后的图片数据 

        @返回值: 
            facial_keypoints：人脸多特征点数据

        @注意: 
            暂无
        '''
        facial_keypoints = self._model.predict(frame_data)         # 进行预测，得到人脸多特征点数据   
        return facial_keypoints
