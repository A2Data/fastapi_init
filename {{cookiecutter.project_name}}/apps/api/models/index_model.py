#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :index_model
# @Date :2023/7/19 11:24
# @Author :{{ cookiecutter.author_name.lower().replace(' ', '_') }}
# @Desc：
-------------------------------------------------
"""

from sqlalchemy import Column, Integer, String

from apps.core.db.database import Base


# 导入前文定义的Model基类

class IndexTable(Base):
    __tablename__ = "index_table"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)


class IndexAdmin(Base):
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String)
