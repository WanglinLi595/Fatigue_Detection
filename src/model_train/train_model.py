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
import pandas as pd

class FacicalKeypointsModel():
    def __init__(self, datasets_path=""):
        pass

    def model_build(self):
        # 建立模型
        model = Sequential()
        # input layer
        model.add(BatchNormalization(input_shape=(120, 120, 1)))
        model.add(Conv2D(48, (5, 5), kernel_initializer='he_normal'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(0.2))
        # layer 2
        model.add(Conv2D(60, (5, 5)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(0.2))
        # layer 3
        model.add(Conv2D(72, (5, 5)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(0.2))
        # layer 4
        model.add(Conv2D(72, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(0.2))
        # layer 5
        model.add(Conv2D(72, (3, 3)))
        model.add(Activation('relu'))
        model.add(Flatten())
        # layer 6
        model.add(Dense(500, activation="relu"))
        model.add(Dropout(0.2))
        # layer 7
        model.add(Dense(90, activation="relu"))
        model.add(Dropout(0.2))
        # layer 8
        model.add(Dense(24))

    def model_train(self, model, optimizer, x_train, y_train):
        model.compile(optimizer=optimizer, loss='mse', metrics=['accuracy'])
        history = model.fit(x_train, y_train, validation_split=0.2, shuffle=True, epochs=epochs, batch_size=20)
        return history

    def save_model(self):
        tf.keras.models.save_model(model, "save_model")


if __name__ == "__main__":
    


