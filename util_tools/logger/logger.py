# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import os
import time
from queue import SimpleQueue
from typing import TypedDict, List, TextIO, Optional
import threading

from init_env.init import env_config
from util_tools.time_tool.time_tool import time_to_str



class LogCtx(TypedDict):
    log_level:int
    log_level_tag:str
    log_conent:List[str]
    log_timestamp:int


class Logger:
    def __init__(self, task_name: str = "default_task"):
        self.task_name:str = task_name
        self.fd:Optional[TextIO] = None
        self.log_file_name:str = ""
        self.log_queue: SimpleQueue[LogCtx] = SimpleQueue()
        self.__init_log_path(int(time.time()*1000))
        self.log_thread = threading.Thread(target=self.write_log_task, daemon=True)


    def __init_log_path(self,time_stamp:int):
        now_date = time_to_str(time_stamp).split(" ")[0]
        log_filename = os.path.join(env_config.base_work_path, "logs", now_date, f"{self.task_name}.log")
        if log_filename == self.log_file_name and self.fd is not None:
            return log_filename
        if not os.path.exists(os.path.join(env_config.base_work_path, "logs", now_date, f"{self.task_name}.log")):
            os.makedirs(os.path.join(env_config.base_work_path, "logs", now_date), exist_ok=True)
        log_filename = os.path.join(env_config.base_work_path, "logs", now_date, f"{self.task_name}.log")
        if self.fd is not None:
            self.fd.close()
        self.fd = open(log_filename, "a", encoding="utf-8")
        self.log_file_name = log_filename

    def write_log_task(self):
        while 1:
            log_context = self.log_queue.get()
            self.__init_log_path(log_context["log_timestamp"])
            for line in log_context["log_conent"]:
                log_line = f"{time_to_str(log_context['log_timestamp'])} [{log_context['log_level_tag']}] {line}\n"
                print(log_line, end="")
                if self.fd is not None:
                    self.fd.write(log_line)




