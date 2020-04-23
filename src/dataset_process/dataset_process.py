#!/usr/bin/env python
# coding=utf-8
'''
@描述: 处理人脸关键点数据集
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.04.23
@最后编辑人: LiWanglin
@最后编辑时间: 2020.04.23
'''

import re
import os
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def main():
    # 保存文件路径
    points_path = "E:/fcaial_keypoints_data/SmithCVPR2013_dataset_resized/points/"   # 人脸关键点数据文件夹
    images_path = "E:/fcaial_keypoints_data/SmithCVPR2013_dataset_resized/images/"   # 人年图片文件夹

    # 获取文件夹内的文件名
    points_files = os.listdir(points_path)
    files_count = len(points_files)

    # 指定修改后图片文件的尺寸
    image_size_h, image_size_w = 120, 120

    # 建立 ndarray 数组，用来保存数据
    fcaial_keypoints = np.zeros([files_count, 388], dtype=np.float64)           # 保存关键点数据
    image_datas = np.zeros([files_count, image_size_h, image_size_w, 1], dtype=np.uint8)        # 保存图片数据
    image_scale = np.zeros([files_count, 2], dtype=np.float64)                  # 保存图片的缩放比

    # 获取人脸关键点数据以及图片数据
    count = 0  # 用来计数
    for points_file in points_files:
        points_file_path = points_path + points_file   # 人脸关键点路径
        with open(points_file_path, "r") as f:
            # 获取关键点数据
            points_str = f.read()
            image_path = re.match(r"\w+_\w+", points_str)   
            points = re.findall(r"\w+\.\w+", points_str)     # 提取列表中的关键点字符   
            key_points = [float(x) for x in points]         # 将字符转化为浮点
            fcaial_keypoints[count] = key_points            # 保存到 ndarray 中
            
            # 获取图片数据
            image_path = images_path + image_path.group() + ".jpg"
            image_data = cv.imread(image_path)
            image_h, image_w = image_data.shape[:2]
            image_scale[count] = image_h/image_size_h, image_w/image_size_w
            image_data = cv.resize(image_data, (image_size_h, image_size_w))
            image_data = cv.cvtColor(image_data, cv.COLOR_RGB2GRAY)
            image_data = np.reshape(image_data, [image_size_h, image_size_w, 1])
            image_datas[count] = image_data   
            count += 1

    # 对人脸关键点数据进行缩放
    count = 0  # 用来计数
    for i in image_scale:
        facial_keypoint = fcaial_keypoints[count]        # 获取单个人脸关键点数据
        facial_keypoint[::2] = facial_keypoint[::2] / i[1] # 对人脸关键点数据的宽进行缩放
        facial_keypoint[1::2] = facial_keypoint[1::2] / i[0] # 对人脸关键点数据的长进行缩放
        count += 1  


    # 查看数据效果
    #-----------------------------------------------------#
    # 嘴巴上的点：58 - 113
    # 右眼的点：114 - 134
    # 左眼的点：134 - 153
    #-----------------------------------------------------#
    # plt.figure(figsize=[500, 500], dpi=80)
    # for j in range(20):    # 总共展示十张图片
    #     image = image_datas[j]    # 获取图片数据
    #     image = cv.cvtColor(image, cv.COLOR_BGR2RGB)   # 由于 matplotlib 支持的是 rgb 色彩空间，所以我们需要将 bgr 转化为 rgb
    #     for i in range(134, 154):
    #         cv.circle(image, (int(fcaial_keypoints[j, 2*i]), int(fcaial_keypoints[j, 2*i+1])), 2, (255, 0, 0), -1)   # 进行打点
    #     plt.subplot(2, 10, j+1)
    #     plt.imshow(image)
    # plt.show()

    fcaial_keypoints_part = fcaial_keypoints[:,[232,233,238,239,244,245,250,251,256,257,262,263,268,269,274,275,280,281,286,287,292,293,298,299]]

    # 保存数据
    np.save(r"E:\fcaial_keypoints_data\SmithCVPR2013_dataset_resized/fcaial_keypoints", fcaial_keypoints)
    np.save(r"E:\fcaial_keypoints_data\SmithCVPR2013_dataset_resized/image_datas", image_datas)
    np.save(r"E:\fcaial_keypoints_data\SmithCVPR2013_dataset_resized/fcaial_keypoints_part", fcaial_keypoints_part)

if __name__ == "__main__":
    main()
