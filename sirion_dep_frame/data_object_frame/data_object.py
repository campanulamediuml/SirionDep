# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import time
from typing import Dict, Optional


class DataContext:
    def __init__(self, data: Dict, data_tag: str, data_timestamp_watermark: Optional[int] = None,
                 ctx_info: Optional[Dict] = None):
        self.__data = data
        self.__data_tag = data_tag
        self.__data_timestamp_watermark = data_timestamp_watermark
        self.__ctx_info = ctx_info
        if self.__ctx_info is None:
            self.__ctx_info = {}
        if self.__data_timestamp_watermark is None:
            self.__data_timestamp_watermark = int(time.time() * 1000)

    def get_watermark(self) -> int:
        """
        获取数据的时间戳水印，单位毫秒
        :return:
        """
        return self.__data_timestamp_watermark

    def get_data(self) -> Dict:
        """
        获取数据对象
        :return:
        """
        return self.__data

    def get_context(self):
        """
        获取上下文信息
        :return:
        """
        return self.__ctx_info

    def set_data(self, new_data: Dict):
        """
        更新数据对象
        :param new_data:
        :return:
        """
        self.__data.update(new_data)

    def update_context(self, new_ctx: Dict):
        """
        更新上下文信息
        :param new_ctx:
        :return:
        """
        self.__ctx_info.update(new_ctx)
