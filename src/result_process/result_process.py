#!/usr/bin/env python
# coding=utf-8
'''
@描述: 人脸关键点数据分析
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.04.29
@最后编辑人: LiWanglin
@最后编辑时间: 2020.05.05
'''

import numpy as np


def eyes_process(eyes_data):
    '''测量左右眼的闭合程度

    利用欧式距离测量左右眼的闭合程度

    @参数说明: 
        eyes_data：左右眼 24 个点数据

    @返回值: 
        如果输入数据有误，返回 -1
        如果输入正确，返回左右眼闭合程度

    @注意: 
        暂无
    '''
    if(len(eyes_data) != 24):
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
        right_eye = (dot4_distance + dot5_distance) / (2 * dot6_distance)
        return [left_eye, right_eye]

def mouse_porcess(self, mouse_data):
    '''测量嘴巴的闭合程度

    利用欧式距离测量嘴巴的闭合程度

    @参数说明: 
        mouse_data：嘴巴 16 个点数据

    @返回值: 
        如果输入数据有误，返回 -1
        如果输入正确，返回嘴巴闭合程度

    @注意: 
        暂无
    '''
    if(len(mouse_data != 16)):
        return -1
    else:
        # 嘴巴闭合程度
        dot1_distance = ((mouse_data[4]-mouse_data[6])**2 + (mouse_data[5]-mouse_data[7])**2)**0.5
        dot2_distance = ((mouse_data[8]-mouse_data[10])**2 + (mouse_data[9]-mouse_data[11])**2)**0.5
        dot3_distance = ((mouse_data[12]-mouse_data[14])**2 + (mouse_data[13]-mouse_data[15])**2)**0.5
        dot4_distance = ((mouse_data[0]-mouse_data[2])**2 + (mouse_data[1]-mouse_data[3])**2)**0.5
        mouse = (dot1_distance + dot2_distance + dot3_distance) / (3 * dot4_distance)
        return 
        
def perclos_judge(eye_process_data, threshold):
    '''对眼部的闭合程度数据进行处理

    @参数说明: 
        eye_process_data：传入的眼部处理数据
        threshold：眼睛睁闭眼的阈值

    @返回值: 
        返回 -2 ，为过度疲劳状态
        返回 -1 ，为疲劳状态
        返回 0 ，表明状态良好
    @注意: 
        无
    '''
    threshold_count = 0                 # 用来记录小于阈值的个数
    data_count = len(eye_process_data)   # 获取总的数据长度
    for i in eye_process_data:
        if float(i) < threshold:
            threshold_count += 1
    proportion = threshold_count / data_count       # 计算闭眼在整个数据的比例
    print(proportion)
    if(proportion > 0.8):       # 比例大于 80%
        return -2               # 为过度疲劳状态
    if(proportion > 0.2 and proportion < 0.8):       # 比例小于 80% 大于 20%
        return -1               # 为疲劳状态
    else:                                       
        return 0                # 状态良好                      

