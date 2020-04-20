import re
import os
import numpy as np
import cv2 as cv
import pandas as pd
from matplotlib import pyplot as plt

file_path = "E:/Fatigue_Detection/fical_keypoints_data/300w/01_Indoor"
a = os.listdir(file_path)

files_num = int(len(a)/2)
facial_keypoints = np.zeros([files_num, 68*2], dtype=np.float64)
facial_image = np.zeros([files_num, 500, 500, 3], dtype=np.uint8)
image_scale = np.zeros([files_num, 2], dtype=np.float64)

count_1 = 0
count_2 = 0
for i in a:
    ret = re.match(r".\w+\.pts", i)
    if ret:
        # 读取 pts 点
        pts_file = file_path + "/" + i
        with open(pts_file, "r") as f:
            a = f.read()
        
        # 读取当中的关键点数据
        key_point = re.findall(r"\d+\.\d+", a)
        
        # 将列表中的字符串转化为数字
        key_point = [float(x) for x in key_point]
        # 添加到 facial_keypoints
        facial_keypoints[count_1] = key_point
        count_1 += 1
    else:
        # 获取图片文件路径
        image_file = file_path + "/" + i
        # 打开图片
        image = cv.imread(image_file, cv.IMREAD_COLOR)
        # 获取图片长和宽
        image_h, image_w = image.shape[:2]
        # 改变图片尺寸
        image = cv.resize(image, (500, 500))
        # 得到缩放比
        image_scale[count_2] = [image_h/500, image_w/500]
        # 添加到 facial_image
        facial_image[count_2] = image
        count_2 += 1
count_1 = 0

# 将人脸关键点数据也进行缩放
for i in image_scale:
    facial_keypoint = facial_keypoints[count_1] 
    facial_keypoint[::2] = facial_keypoint[::2] / image_scale[count_1, 1]
    facial_keypoint[1::2] = facial_keypoint[1::2] / image_scale[count_1, 0]
    count_1 += 1


# 保存处理的数据
np.save("./facial_image", facial_image)
np.save("./facial_keypoints", facial_keypoints)
