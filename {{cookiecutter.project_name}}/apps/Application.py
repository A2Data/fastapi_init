#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :Application
# @Date :2023/7/6 01:45
# @Author : {{ cookiecutter.author_name }}
# @Desc： 应用程序
-------------------------------------------------
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from apps.api import ApiRouter
from apps.core.base.BaseSettings import *


def create_app() -> FastAPI:
    """
    生成FatAPI对象
    docs_url：配置交互文档的路由地址，如果禁用则为None，默认为 /docs
    redoc_url： 配置 Redoc 文档的路由地址，如果禁用则为None，默认为 /redoc
    openapi_url：配置接口文件json数据文件路由地址，如果禁用则为None，默认为/openapi.json
    :return:
    """
    app = FastAPI(
        debug=DEBUG,
        title=TITLE,
        description=DESCRIPTION,
        version=VERSION,
        docs_url=DOCS_URL,
        redoc_url=REDOC_URL
    )

    # 跨域设置
    register_cors(app)
    # 注册路由
    register_router(app)

    return app


def register_router(app: FastAPI) -> None:
    """
    注册路由
    :param app:
    :return:
    """
    # 项目API
    for url in ApiRouter.urlpatterns:
        app.include_router(url["ApiRouter"], prefix=url["prefix"], tags=url["tags"])


def register_cors(app: FastAPI) -> None:
    """
    配置允许域名列表、允许方法、请求头、cookie等
    :param app:
    :return:
    """
    if CORS_ORIGIN_ENABLE:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=ALLOW_ORIGINS,
            allow_credentials=ALLOW_CREDENTIALS,
            allow_methods=ALLOW_METHODS,
            allow_headers=ALLOW_HEADERS,
        )
