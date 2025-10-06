# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import os
import time
from queue import SimpleQueue
from typing import TypedDict, List, TextIO, Optional, Dict
import threading

from sirion_dep_init_env.init import env_config
from sirion_dep_util_tools.time_tool.time_tool import time_to_str

LOG_LEVEL_DEBUG = 0
LOG_LEVEL_INFO = 1
LOG_LEVEL_WARNING = 2
LOG_LEVEL_ERROR = 3

LOG_LEVEL_TAG_DICT: Dict[int, str] = {
    LOG_LEVEL_DEBUG: 'DEBUG',
    LOG_LEVEL_INFO: 'INFO',
    LOG_LEVEL_WARNING: 'WARNING',
    LOG_LEVEL_ERROR: 'ERROR',
}

class LogCtx(TypedDict):
    log_conent:List[str]
    log_timestamp:int


class Logger:
    def __init__(self, task_name: str = "default_task"):
        self.task_name:str = task_name
        self.fd:Optional[TextIO] = None
        self.log_file_name:str = ""
        self.log_queue: SimpleQueue[LogCtx] = SimpleQueue()
        self.__init_log_path(int(time.time()*1000))
        self.log_thread = threading.Thread(target=self.write_log_task, daemon=True).start()


    def __init_log_path(self,time_stamp:int):
        """
        初始化日志文件路径
        :param time_stamp:
        :return:
        """
        now_date = time_to_str(time_stamp).split(" ")[0]
        log_filename = os.path.join(env_config.base_work_path, "logs", now_date, f"{self.task_name}.log")
        if log_filename == self.log_file_name and self.fd is not None:
            return log_filename
        if not os.path.exists(os.path.join(env_config.base_work_path, "logs", now_date, f"{self.task_name}.log")):
            os.makedirs(os.path.join(env_config.base_work_path, "logs", now_date), exist_ok=True)
        if self.fd is not None:
            self.fd.close()
        self.fd = open(log_filename, "a", encoding="utf-8")
        self.log_file_name = log_filename

    def write_log_task(self):
        """
        日志写入任务
        :return:
        """
        while 1:
            log_context = self.log_queue.get()
            self.__init_log_path(log_context["log_timestamp"])
            for line in log_context["log_conent"]:
                print(line, end="")
                self.fd.write(f"{line}")

logger_writer = Logger()


def create_log_ctx(source,level:int,*msg):
    log_timestamp = int(time.time() * 1000)
    time_string = time_to_str(log_timestamp)
    log_content = ' '.join([str(i) for i in msg])
    log_data_list = ["[%s][%s][%s][%s]%s\n"%(
        time_string,
        log_timestamp,
        source,
        LOG_LEVEL_TAG_DICT[level],
        line
    )for line in log_content.split('\n')]
    ctx:LogCtx = {
        "log_conent": log_data_list,
        "log_timestamp": log_timestamp,
    }
    logger_writer.log_queue.put(ctx)

def dep_dbg(source, *msg):
    if env_config.log_level >= LOG_LEVEL_DEBUG:
        create_log_ctx(source,LOG_LEVEL_DEBUG,*msg)

def dep_info(source, *msg):
    if env_config.log_level >= LOG_LEVEL_INFO:
        create_log_ctx(source,LOG_LEVEL_INFO,*msg)

def dep_warn(source, *msg):
    if env_config.log_level >= LOG_LEVEL_WARNING:
        create_log_ctx(source,LOG_LEVEL_WARNING,*msg)

def dep_error(source, *msg):
    if env_config.log_level >= LOG_LEVEL_ERROR:
        create_log_ctx(source,LOG_LEVEL_ERROR,*msg)





