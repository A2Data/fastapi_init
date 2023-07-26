#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :index_schema
# @Date :2023/7/19 11:24
# @Author :{{ cookiecutter.author_name.lower().replace(' ', '_') }}
# @Desc：
-------------------------------------------------
"""
from pydantic import BaseModel


class IndexBase(BaseModel):
    name: str
    email: str


class IndexCreate(IndexBase):
    pass


class Index(IndexBase):
    id: int


