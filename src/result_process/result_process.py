#!/usr/bin/env python
# coding=utf-8
'''
@描述: 人脸关键点数据分析
@版本: V1_0
@作者: LiWanglin
@创建时间: Do not edit
@最后编辑人: LiWanglin
@最后编辑时间: Do not Edit
'''

import numpy as np

class ResultProcess():
    def __init__(self):
        pass

    def eyes_process(self, eyes_data):
        if(len(eyes_data != 24)):
            return -1
        else:
            # 左眼闭合程度
            dot1_distance = ((eyes_data[4]-eyes_data[6])**2 + (eyes_data[5]-eyes_data[7])**2)**0.5
            dot2_distance = ((eyes_data[8]-eyes_data[10])**2 + (eyes_data[9]-eyes_data[11])**2)**0.5
            dot3_distance = ((eyes_data[0]-eyes_data[2])**2 + (eyes_data[1]-eyes_data[3])**2)**0.5
            left_eye = (dot1_distance + dot2_distance) / (2 * dot3_distance)

            # 右眼闭合程度
            dot4_distance = ((eyes_data[16]-eyes_data[18])**2 + (eyes_data[17]-eyes_data[19])**2)**0.5
            dot5_distance = ((eyes_data[20]-eyes_data[22])**2 + (eyes_data[21]-eyes_data[23])**2)**0.5
            dot6_distance = ((eyes_data[12]-eyes_data[14])**2 + (eyes_data[13]-eyes_data[15])**2)**0.5
            right_eye = (dot4_distance + dot5_distance) / (3 * dot6_distance)
            return left_eye, right_eye

    def mouse_porcess(self, mouse_data):
        if(len(mouse_data != 16)):
            return -1
        else:
            # 嘴巴闭合程度
            dot1_distance = ((mouse_data[4]-mouse_data[6])**2 + (mouse_data[5]-mouse_data[7])**2)**0.5
            dot2_distance = ((mouse_data[8]-mouse_data[10])**2 + (mouse_data[9]-mouse_data[11])**2)**0.5
            dot3_distance = ((mouse_data[12]-mouse_data[14])**2 + (mouse_data[13]-mouse_data[15])**2)**0.5
            dot4_distance = ((mouse_data[0]-mouse_data[2])**2 + (mouse_data[1]-mouse_data[3])**2)**0.5
            left_eye = (dot1_distance + dot2_distance + dot3_distance) / (3 * dot4_distance)

    def comprehensive_results(self):
        pass