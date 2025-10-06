# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import time
from threading import Thread
from typing import Callable, Tuple, Optional

from sirion_dep_frame.plugin_frame import PuginBase


class ThreadTask:
    def __init__(self, task_name: str = "", task_function:Callable = None,
                 args:Tuple = (), is_interval:bool=False, interval_time:int = 0) -> None:
        self.task_name = task_name
        self.task_function = task_function
        self.args = args
        self.is_interval = is_interval
        self.interval_time = interval_time
        self.thread:Optional[Thread] = Thread(target=self.task_run, daemon=True)
        self.thread.start()

    def task_run(self):
        while True:
            self.task_function(*self.args)
            if self.is_interval:
                time.sleep(self.interval_time)
            else:
                return







