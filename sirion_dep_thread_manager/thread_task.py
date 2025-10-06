# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import time
import traceback
from threading import Thread
from typing import Callable, Tuple, Optional

from sirion_dep_frame.plugin_frame import PluginBase
from sirion_dep_util_tools.logger.logger import dep_error, DEP_TAG


class ThreadTask:
    def __init__(self, task_name: str = "", task_function:Optional[Callable] = None,
                 args:Tuple = (), is_interval:bool=False, interval_time:int = 0) -> None:
        self.task_name = task_name
        self.task_function = task_function
        self.args = args
        self.is_interval = is_interval
        self.interval_time = interval_time
        self.thread:Optional[Thread] = Thread(target=self.task_run, daemon=True)
        self.thread.start()

    def task_run(self):
        if self.task_function is None:
            dep_error("该任务未绑定可用函数")
            return
        while True:
            try:
                self.task_function(*self.args)
                if self.is_interval:
                    time.sleep(self.interval_time)
                else:
                    return
            except Exception as e:
                err_info = traceback.format_exc()
                dep_error(DEP_TAG,err_info)
                dep_error(DEP_TAG,"任务执行失败-->",e)







