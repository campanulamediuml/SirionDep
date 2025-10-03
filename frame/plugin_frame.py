# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
from typing import Dict, Any

from frame.data_object_frame.data_object import DataContext


class PuginBase:
    def __init__(self,global_config:Dict):
        self.global_config = global_config

    def initial_work(self, parameters:Dict[str, Any]):
        raise NotImplementedError("initial_work method not implemented")

    def execute(self, data:DataContext):
        raise NotImplementedError("run method not implemented")

    def get_results(self) -> DataContext:
        raise NotImplementedError("get_results method not implemented")





