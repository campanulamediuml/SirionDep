# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import os


class Logger:
    def __init__(self, name):
        self.full_log_path = os.path.join("logs", name)
        os.makedirs(name)

    def log_task(self, message):
        print(f"[{self.name}] {message}")
