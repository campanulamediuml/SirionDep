# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import os

from pydantic import BaseModel


class ConfigTemplate(BaseModel):
    base_work_path: str


env_config:ConfigTemplate = ConfigTemplate.parse_file("config.json")

LOG_PATH = os.path.join(env_config.base_work_path, "logs")
os.makedirs(LOG_PATH, exist_ok=True)
WORKFLOW_PATH = os.path.join(env_config.base_work_path, "workflows")
os.makedirs(WORKFLOW_PATH, exist_ok=True)
BENCHMARK_PATH = os.path.join(env_config.base_work_path, "benchmark")
os.makedirs(BENCHMARK_PATH, exist_ok=True)
LIBPATH = os.path.join(env_config.base_work_path, "lib")
os.makedirs(LIBPATH, exist_ok=True)


