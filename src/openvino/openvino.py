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


        for blob_name in self.net.inputs:
            self._input_blob = blob_name

        out_blob = next(iter(self._net.outputs))

        n, c, h, w = self._net.inputs[self._input_blob].shape

    def run_ie(self, frame=None):

        feed_dict = {}

        next_frame = frame

        frame_h, frame_w = frame.shape[:2]
        next_request_id = 1
        cur_request_id = 0

        in_frame = cv2.resize(next_frame, (w, h))
        in_frame = in_frame.transpose((2, 0, 1))  # Change data layout from HWC to CHW
        in_frame = in_frame.reshape((n, c, h, w))
        feed_dict[input_blob] = in_frame
        self._exec_net.start_async(request_id=next_request_id, inputs=feed_dict)
        res = self._exec_net.requests[cur_request_id].outputs[out_blob]
        key = cv2.waitKey(80)
        for obj in res[0][0]:
            # Draw only objects when probability more than specified threshold
            if obj[2] > 0.5:
                xmin = int(obj[3] * frame_w)
                ymin = int(obj[4] * frame_h)
                xmax = int(obj[5] * frame_w)
                ymax = int(obj[6] * frame_h)
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0,255,0), 2)
                cv2.imshow("Detection Results", frame)

        cur_request_id, next_request_id = next_request_id, cur_request_id
        frame = next_frame
        frame_h, frame_w = frame.shape[:2]
        
        if key == ord("q"):
            cv2.destroyAllWindows()
            break







