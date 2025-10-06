# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import time


def time_to_str(time_stamp: int) -> str:
    """
    将时间戳转换为字符串格式，精确到秒
    :param time_stamp: 时间戳，单位毫秒
    :return: 格式化的时间字符串，格式为 "YYYY-MM-DD HH:MM:SS"
    """
    time_array = time.localtime(time_stamp / 1000)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_array)


def str_to_time(time_str: str) -> int:
    """
    将字符串格式的时间转换为时间戳，精确到秒
    :param time_str: 格式化的时间字符串，格式为 "YYYY-MM-DD HH:MM:SS"
    :return: 时间戳，单位毫秒
    """
    time_array = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(time_array) * 1000)
