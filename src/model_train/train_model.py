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
from tensorflow.keras.layers import (BatchNormalization, Conv2D, Activation, MaxPooling2D, Dense,
                                    GlobalAveragePooling2D, Dropout, Flatten)
from tensorflow.keras import optimizers, Sequential
import numpy as np

class FacicalKeypointsModel():
    def __init__(self):
        pass

    def model_build(self):
        # 建立模型
        self._facial_model = Sequential()
        # input layer
        self._facial_model.add(BatchNormalization(input_shape=(120, 120, 1)))
        self._facial_model.add(Conv2D(48, (5, 5), kernel_initializer='he_normal'))
        self._facial_model.add(Activation('relu'))
        self._facial_model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        self._facial_model.add(Dropout(0.2))
        # layer 2
        self._facial_model.add(Conv2D(60, (5, 5)))
        self._facial_model.add(Activation('relu'))
        self._facial_model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        self._facial_model.add(Dropout(0.2))
        # layer 3
        self._facial_model.add(Conv2D(72, (5, 5)))
        self._facial_model.add(Activation('relu'))
        self._facial_model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        self._facial_model.add(Dropout(0.2))
        # layer 4
        self._facial_model.add(Conv2D(72, (3, 3)))
        self._facial_model.add(Activation('relu'))
        self._facial_model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        # layer 5
        self._facial_model.add(Conv2D(72, (3, 3)))
        self._facial_model.add(Activation('relu'))
        self._facial_model.add(Flatten())
        # layer 6
        self._facial_model.add(Dense(500, activation="relu"))
        self._facial_model.add(Dropout(0.2))
        # layer 6
        self._facial_model.add(Dense(256, activation="relu"))
        self._facial_model.add(Dropout(0.2))
        # layer 7
        self._facial_model.add(Dense(90, activation="relu"))
        self._facial_model.add(Dropout(0.2))
        # layer 8
        self._facial_model.add(Dense(40))

        self._facial_model.summary()

    def model_train(self, optimizer,epochs, x_train, y_train):
        self._facial_model.compile(optimizer=optimizer, loss='mse', metrics=['accuracy'])
        history = self._facial_model.fit(x_train, y_train, validation_split=0.2, shuffle=True, epochs=epochs, batch_size=20)
        return history

    def save_model(self, model_name="save_model"):
        tf.keras.models.save_model(model, model_name)


if __name__ == "__main__":
    # 提取数据
    facial_image = np.load(r"E:\Fatigue_Detection\model_data\image_datas.npy")
    facial_keypoints = np.load(r"E:\Fatigue_Detection\model_data\fcaial_keypoints_part.npy")

    model = FacicalKeypointsModel()
    model.model_build()
    sgd = optimizers.SGD(lr=0.008, decay=1e-6, momentum=0.95, nesterov=True)
    model.model_train(sgd, 300, facial_image, facial_keypoints)
    model.save_model()





