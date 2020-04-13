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

import cv2
from openvino.inference_engine import  IECore, IENetwork

class model_optimazor:
    def __init__(self, parent=None):
        pass

    def load_module_file(self, xml_file, bin_file):
        '''载入模型文件

        @参数说明: 
            xml_file ：模型的 xml 文件
            bin_file : 模型的 bin 文件

        @返回值: 
            无

        @注意: 
            无
        '''
        self._ie = IECore()
        self._net = IENetwork(xml_file, bin_file)
        
        self._input_blob = next(iter(self._net.inputs))
        self._out_blob = next(iter(self._net.outputs))
        self._exec_net = self._ie.load_network(network=self._net, device_name="cpu", num_requests=2)

        self._n, self._c, self._h, self._w = self._net.inputs[self._input_blob].shape

        self._feed_dict = {}
        self._next_request_id = 1
        self._cur_request_id = 0

    def run_ie(self, frame=None):
        self._frame = frame
        frame_h, frame_w = frame.shape[:2]
        in_frame = cv2.resize(self._frame, (self._w, self._h))
        in_frame = in_frame.transpose((2, 0, 1))  # Change data layout from HWC to CHW
        in_frame = in_frame.reshape((self._n, self._c, self._h, self._w))
        self._feed_dict[self._input_blob] = in_frame

        self._exec_net.start_async(request_id=self._next_request_id, inputs=self._feed_dict)

        # 成功获取 Blob
        if self._exec_net.requests[self._cur_request_id].wait(-1) == 0:
            res = self._exec_net.requests[self._cur_request_id].outputs[self._out_blob]
            res = res[0]
            print(res[:2] * frame_w)
            pt1 = (int(res[0] * frame_w), int(res[2] * frame_h))
            pt2 = (int(res[1] * frame_w), int(res[3] * frame_h))
            cv2.circle(self._next, pt1, 5, (0,255,0), -1)
            cv2.circle(self._next, pt2, 5, (0,0,255), -1)
            res_frame = self._next
        
        # 交换 id 以及 frame
        self._cur_request_id, self._next_request_id = self._next_request_id, self._cur_request_id
        self._next = self._frame

        return res_frame










