#!/usr/bin/env python
# coding=utf-8
'''
@描述: 
@版本: V1_0
@作者: LiWanglin
@创建时间: Do not edit
@最后编辑人: LiWanglin
@最后编辑时间: Do not Edit
'''

from PyQt5.QtWidgets import  QMainWindow, QMessageBox
from PyQt5.QtCore import  QTimer, pyqtSlot, QEvent
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtChart import QChartView, QChart, QLineSeries, QValueAxis
from ui.gui_main_interface import Ui_main_interface
import cv2
from get_data.get_data import GetFacialData
import numpy as np
from result_process import result_process
import re


class MainInterface(QMainWindow):
    '''实现 GUI 以及其连接整个程序的功能

    @属性说明: 


    @方法说明: 


    @注意: 

    '''
    def __init__(self, parent=None):
        super().__init__(parent)            # 父类初始化
        self.ui = Ui_main_interface()       # 创建UI类
        self.ui.setupUi(self)
        self.showMaximized()                # 最大化界面
        self.setWindowTitle("疲劳检测")      # 界面标题
        self.time = QTimer()                # 创建定时器
        self._connect_slot()                # 初始化槽函数连接
        self.eye_data_chart_init()          # 初始化眼睛闭合数据折线图
        self._t = 0                         # 用来计数
        self._perclos_threshold = 0.3       # 设置初始化阈值

    def _connect_slot(self):
        '''初始化信号与槽的连接

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''
        self.ui.btn_start.clicked.connect(self._display)
        self.time.timeout.connect(self.test)

    def paintEvent(self, evevt):
        """绘图软件背景图

        Qt里面默认事件处理函数，在界面需要重新绘制时触发
        此方法主要是绘制软件的背景图

        @参数说明: 
            evevt：Qt默认事件

        @返回值: 
            无

        @注意: 
            无
        """
        temp_painter = QPainter(self)
        # 创建背景图QPixmap（）对象
        soft_background_image = QPixmap("resources/groud.jpg")
        # 绘制背景图
        temp_painter.drawPixmap(0, 0, self.width(), self.height(), soft_background_image)
        # 执行父类的paintEvent()函数，以便父类执行其内建的一些操作
        super().paintEvent(evevt)

    def eye_data_chart_init(self):
        '''初始化左右眼闭合程度曲线图表

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''
        # 创建 chart 和 chartview
        self._chart = QChart()
        self._chart.setTitle("眼睛闭合程度值")          # 设置图表标题
        self._chartView = QChartView(self)
        self._chartView.setChart(self._chart)           # chart 添加到 chartview

        # 完成布局
        self.ui.horizontalLayout_2.addWidget(self._chartView)   

        ## 创建曲线系列
        self._series0 = QLineSeries()
        self._series1 = QLineSeries()
        self._series0.setName("左眼曲线")           # 设置曲线名
        self._series1.setName("右眼曲线")
        self._chart.addSeries(self._series0)        # 序列添加到图表
        self._chart.addSeries(self._series1)

        # 创建坐标轴
        self._axis_x = QValueAxis()          # x 轴
        self._axis_x.setRange(0, 60)        # 设置 x 轴坐标范围
        self._axis_x.setTitleText("time(secs)")     # x 轴标题
        self._axis_y = QValueAxis()         # y 轴
        self._axis_y.setRange(0, 0.5)       # 设置 y 轴坐标范围
        self._axis_y.setTitleText("value")  # y 轴标题

        # 为序列设置坐标轴
        self._chart.setAxisX(self._axis_x, self._series0)
        self._chart.setAxisY(self._axis_y, self._series0)
        self._chart.setAxisX(self._axis_x, self._series1)
        self._chart.setAxisY(self._axis_y, self._series1)

    @pyqtSlot(bool)
    def _display(self, checked):
        '''

        @参数说明: 


        @返回值: 


        @注意: 

        '''
        if(checked==False):         # 当按键为 False 时，停止检查
            self.ui.le_eye_threshold.setEnabled(True)
            self.ui.btn_start.setText("启动")
            self.ui.lb_fatigue_detection.setText("检测停止")
            self.time.stop()
        else:
            threshold_str = self.ui.le_eye_threshold.text()        # 获得睁闭眼阈值
            threshold_str = re.match(r"\d\.\d\d$", threshold_str)      # 对睁闭眼阈值做限定 
            if(threshold_str==None):
                message_title = "阈值格式错误"
                message_text = "请输入正确的阈值格式，格式为 x.xx (x 为数字)"
                QMessageBox.critical(self, message_title, message_text)
            else:
                self.ui.btn_start.setText("停止")
                self.ui.le_eye_threshold.setEnabled(False)
                model_path = r"E:\make_data\facial"            # 人脸关键模型路径
                opencv_facial_path = r"E:\Fatigue_Detection\model_data\facial_model\haarcascade_frontalface_default.xml"    # 人脸检测模型路径
                cap_index = eval(self.ui.cmb_cap_index.currentText())       # 从 combabox 获取设想头索引
                # cap_file = r"C:\Users\LWL\Pictures\Camera Roll\WIN_20200503_07_51_19_Pro.mp4"
                self.facial_data = GetFacialData(tf_model=model_path, facial_model_file=opencv_facial_path, cap_index=cap_index) # 创建 GetFacialData 类
                self.time.start(1000)       # 设置每次检测的间隔时间
                self.ui.lb_fatigue_detection.setText("检测中")
                self._series0.clear()
                self._series1.clear()
                self._t=0       # 重新开始计数
                self._perclos_threshold = eval(threshold_str.group())


    def test(self):
        ret, frame = self.facial_data.get_frame()          
        if(ret == -1):
            message_title = "摄像头打开失败"
            message_text = "摄像头打开失败，请检测摄像头索引是否正确"
            self.time.stop()
            QMessageBox.critical(self,message_title, message_text)
        if(ret == -2):
            message_title = "获取帧失败"
            message_text = "从摄像头获取帧失败，请重启软件"
            self.time.stop()
            QMessageBox.critical(self, message_title, message_text)
        else:
            frame = cv2.medianBlur(frame, 5)
            ret, rect = self.facial_data.get_facial(frame)
            h, w = frame.shape[:2]
            if(ret == -1):
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                temp_q_image = QImage(frame, w, h, QImage.Format_RGB888)
                #  在 lb_display 中显示图片
                self.ui.lb_display.setPixmap(QPixmap.fromImage(temp_q_image))
                self.ui.lb_facial_number.setText(str(rect))        # 显示当前检测人脸数
            else:
                self.ui.lb_facial_number.setText("1")        # 显示当前检测人脸数
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                facial = frame[rect[2]:rect[3], rect[0]:rect[1]]

                image = cv2.cvtColor(facial, cv2.COLOR_RGB2GRAY)
                image_h, image_w = image.shape[:2]
                image = cv2.resize(image , (150, 150))
                image = np.reshape(image, [1, 150, 150, 1])
                image = image / 255.
                facial_keypoints = self.facial_data.get_result(image)
                facial_keypoints = (facial_keypoints[0] + 1) / 2
                facial_keypoints[::2] = facial_keypoints[::2] * image_w + rect[0]
                facial_keypoints[1::2] = facial_keypoints[1::2] * image_h + rect[2]
                
                # 圈出人脸范围
                facial = cv2.rectangle(frame, (rect[0],rect[2]), (rect[1],rect[3]), (255,0,0), 1)

                # 将人脸多特征点标记到图片上
                for i in range(12):
                    facial = cv2.circle(frame, (int(facial_keypoints[2*i]), int(facial_keypoints[2*i+1])), 2, (255, 0, 0), -1)   # 进行打点

                # 获得左右眼的闭合程度
                eye_process_data = result_process.eyes_process(facial_keypoints)

                # 添加点到图表上
                self._series0.append(self._t, eye_process_data[0])
                self._series1.append(self._t, eye_process_data[1])

                # 在label上显示左右眼计算值
                self.ui.lb_left_eye_figure.setText(str(eye_process_data[0]))    # 显示左眼的计算值
                self.ui.lb_right_eye_figure.setText(str(eye_process_data[1]))   # 显示右眼的计算值

                temp_q_image = QImage(facial.data, w, h, QImage.Format_RGB888)
                #  在 lb_display 中显示图片
                self.ui.lb_display.setPixmap(QPixmap.fromImage(temp_q_image))

                self._t += 1   # 每个 1s 绘制点
                if(self._t>60):
                    # 获取 series0 以及 series1 中所有的数据
                    left_eye_point = self._series0.pointsVector()
                    right_eye_point = self._series1.pointsVector()
                    # 使用正则表达式提取其中的计算数据
                    left_eye_data = np.array(re.findall(r"\d+\.\d{2,5}", str(left_eye_point)))
                    right_eye_data = np.array(re.findall(r"\d+\.\d{2,5}", str(right_eye_point)))
                    perclos_judge_result = result_process.perclos_judge(left_eye_data, self._perclos_threshold)
                    # 对 perclos_judge 的结果进行输出
                    if(perclos_judge_result == -2):
                        self.ui.lb_fatigue_detection.setText("过度疲劳")
                        message_title = "过度疲劳警告提醒"
                        message_text = "为了你的人身安全，请停下手中工作，休息一段时间！"
                        QMessageBox.critical(self, message_title, message_text)     # 过度疲劳提醒
                    elif(perclos_judge_result == -1):
                        self.ui.lb_fatigue_detection.setText("疲劳状态")
                    else:
                        self.ui.lb_fatigue_detection.setText("状态良好")
                    # 清除所有的 series0 以及 series1 数据，重新绘图
                    self._series0.clear()
                    self._series1.clear()
                    self._t=0       # 重新开始计数
        

        




        

