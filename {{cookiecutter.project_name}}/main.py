#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :main
# @Date :2023/7/5 18:37
# @Author : {{ cookiecutter.author_name }}
# @Desc： 入口文件
-------------------------------------------------
"""

import sys
import uvicorn
from art import *
from pathlib import Path

from apps.core.config.dev_env import Prot, Host
from apps.core.db.database import init_db
from apps.utils.logger import log
from fastapi import Request
from apps.Application import create_app

# 将当前目录添加到系统变量中
BASE_DIR = Path(__file__).parent.absolute()
sys.path.append(str(BASE_DIR))

app = create_app()


@app.get("/", include_in_schema=False)
def read_root(req: Request):
    log.debug('初始化项目, include_in_schema=False 在 docs 中不会展示 ')
    extra = {"method": req.method, "url": req.url, "status": 200, "content": "Hello World"}
    log.bind(**extra).info("首页收到请求！")
    return {'hello world'}


# 启动时
@app.on_event("startup")
async def on_startup():
    log.info('Start ...')

    await init_db()


# 关闭时
@app.on_event("shutdown")
async def on_shutdown():
    log.info('On shutdown ...')


if __name__ == '__main__':
    fastapi_art = text2art("FastAPI")
    extra = {"success": "👌 项目启动 ✅ ", "status": 200, "content": "Hello FastAPI"}
    log.bind(**extra).info(fastapi_art)
    uvicorn.run(app='main:app', host=Host, port=Prot, reload=True, access_log=True)
