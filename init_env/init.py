# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import pydantic
from pydantic import BaseModel


class ConfigTemplate(BaseModel):
    base_work_path: str

config:ConfigTemplate = ConfigTemplate.parse_file("config.json")

