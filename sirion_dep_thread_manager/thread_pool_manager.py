# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
from typing import Callable, Tuple, Dict, List

from sirion_dep_thread_manager.thread_task import ThreadTask


class ThreadPoolManager:
    def __init__(self):
        self.thread_pool:Dict[int,ThreadTask] = {}

    def add_task(self,task_name: str = "", task_function:Callable = None,
                 args:Tuple = (), is_interval:bool=False, interval_time:int = 0):
        task = ThreadTask(task_name, task_function, args, is_interval, interval_time)
        self.thread_pool[task.thread.ident] = task
        return task.thread.ident

    def get_task_by_ident(self, task_ident:int) -> ThreadTask:
        return self.thread_pool.get(task_ident)

    def get_running_tasks(self) -> List[ThreadTask]:
        return list(self.thread_pool.values())

    def count_running_tasks(self) -> int:
        return len(self.thread_pool)

t_pool_manager = ThreadPoolManager()


