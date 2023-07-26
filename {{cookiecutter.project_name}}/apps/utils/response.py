#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :response
# @Date :2023/7/20 02:24
# @Author : {{ cookiecutter.author_name }}
# @Desc： 响应类封装
-------------------------------------------------
"""

# 依赖安装：pip install orjson
from fastapi.responses import ORJSONResponse as Response
from fastapi import status as http_status
from . import http_status as http


class SuccessResponse(Response):
    """
    成功响应
    """

    def __init__(self, data=None, msg="success", code=http.HTTP_SUCCESS, status=http_status.HTTP_200_OK
                 , **kwargs):
        self.data = {
            "code": code,
            "message": msg,
            "data": data
        }
        self.data.update(kwargs)
        super().__init__(content=self.data, status_code=status)


class ErrorResponse(Response):
    """
    失败响应
    """

    def __init__(self, msg=None, code=http.HTTP_ERROR, status=http_status.HTTP_200_OK, **kwargs):
        self.data = {
            "code": code,
            "message": msg,
            "data": []
        }
        self.data.update(kwargs)
        super().__init__(content=self.data, status_code=status)
