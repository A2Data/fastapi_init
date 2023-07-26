#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :ApiRouter
# @Date :2023/7/5 20:23
# @Author : {{ cookiecutter.author_name }}
# @Desc： 路由文件
-------------------------------------------------
"""

from .controller import index_router

# 引入应用中的路由
urlpatterns = [
    {"ApiRouter": index_router, "prefix": "/v1", "tags": ["初始化接口"]},
]
