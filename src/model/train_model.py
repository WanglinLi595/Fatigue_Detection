#!/usr/bin/env python
# coding=utf-8
'''
@描述: 训练人脸数据集
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.04.11
@最后编辑人: LiWanglin
@最后编辑时间: 2020.04.11
'''

import tensorflow as tf
from tensorflow.keras import layers, Sequential
import pandas as pd

class FacicalKeypointsModel():

    def __init__(self, datasets_path=""):
        self._datasets_path = datasets_path
        self.data_process()

    def data_process(self):
        if(self._datasets_path == ""):
            print("请输入数据集路径")
            return
        datastas = pd.read_csv(self._datasets_path)     # 读取数据集
        print(datastas.head(10))
        return model_datasets

    def train_model(self, X_train=None, y_train=None, epochs=150):
        self._facial_model = Sequential()
        # 第一层
        

        # 第二层
        self.facial_model.add(layers.Conv2D(36, (5, 5)))
        self.facial_model.add(layers.Activation('relu'))
        self.facial_model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        self.facial_model.add(layers.Dropout(0.2))

        # 第三层
        self.facial_model.add(layers.Conv2D(48, (5, 5)))
        self.facial_model.add(layers.Activation('relu'))
        self.facial_model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        self.facial_model.add(layers.Dropout(0.2))

        # 第四层
        self.facial_model.add(layers.Conv2D(64, (3, 3)))
        self.facial_model.add(layers.Activation('relu'))
        self.facial_model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        self.facial_model.add(layers.Dropout(0.2))

        # 第五层
        self.facial_model.add(layers.Conv2D(64, (3, 3)))
        self.facial_model.add(layers.Activation('relu'))
        self.facial_model.add(layers.Flatten())

        # layer 6
        self.facial_model.add(layers.Dense(500, activation="relu"))
        # layer 7
        self.facial_model.add(layers.Dense(90, activation="relu"))
        # layer 8
        self.facial_model.add(layers.Dense(30))

        self.facial_modelsummary()

        sgd = tf.nn.optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.95, nesterov=True)
        model.compile(optimizer=sgd, loss='mse', metrics=['accuracy'])
        history = model.fit(X_train, y_train, validation_split=0.2, shuffle=True, epochs=epochs, batch_size=20)

    def save_model_data(self):
        pass



if __name__ == "__main__":
    model = FacicalKeypointsModel(r"E:\Fatigue_Detection\WFLW_annotations\list_98pt_rect_attr_train_test\list_98pt_rect_attr_train.txt")




