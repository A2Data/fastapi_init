#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :dev_env
# @Date :2023/7/20 18:17
# @Author : {{ cookiecutter.author_name }}
# @Desc： 开发环境数据库配置
-------------------------------------------------
"""


"""
系统配置 
"""

Prot = 8000
Host = '127.0.0.1'



"""
SQLITE 数据库配置项
"""
# 是否输出 SQL
SQLITE_ECHO = True
SQLITE_DATABASE_URL = "sqlite+aiosqlite:///./apps/resource/data/fastapi.db"
