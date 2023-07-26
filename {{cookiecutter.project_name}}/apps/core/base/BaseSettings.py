#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :BaseSettings
# @Desc： 主配置文件
-------------------------------------------------
"""
import os

"""项目根目录"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))))

""" Apps 目录 """
APP_DIR = 'apps'
APPS_ROOT = os.path.join(BASE_DIR, APP_DIR)

""" 安全警告: 不要在生产中打开调试运行! """
DEBUG = True

""" 项目说明 """
TITLE = {{ cookiecutter.title }}
""" 描述 """
DESCRIPTION = {{ cookiecutter.description }}

"""系统版本"""
VERSION = {{ cookiecutter.version }}

""" 文档地址 """
DOCS_URL = "/docs"

# Redoc 文档
REDOC_URL = "/redoc"

""" 日志存储周期 """
LogsDay = 3

# 随机生成1   openssl rand -base64 32
# 随机生成2   head -c 16 /dev/urandom | od -An -t x | tr -d ' '

"""引入数据库配置"""
if DEBUG:
    from ..config.dev_env import *
else:
    from ..config.pro_env import *

"""
挂载临时文件目录，并添加路由访问，此路由不会在接口文档中显示
TEMP_ENABLE：是否启用临时文件目录访问
TEMP_URL：路由访问
TEMP_DIR：临时文件目录绝对路径
官方文档：https://fastapi.tiangolo.com/tutorial/static-files/
"""
TEMP_ENABLE = True
TEMP_URL = "resource/temp"
TEMP_DIR = os.path.join(APPS_ROOT, TEMP_URL)

"""
挂载静态目录，并添加路由访问，此路由不会在接口文档中显示
STATIC_ENABLE：是否启用静态目录访问
STATIC_URL：路由访问
STATIC_ROOT：静态文件目录绝对路径
官方文档：https://fastapi.tiangolo.com/tutorial/static-files/
"""
STATIC_ENABLE = True
STATIC_URL = "/media"
STATIC_DIR = "resource/static"
STATIC_ROOT = os.path.join(APPS_ROOT, STATIC_DIR)

"""DATA 数据地址 """
DATA_DIR = 'resource/data'
DATA_ROOT = os.path.join(APPS_ROOT, DATA_DIR)

"""
跨域解决
详细解释：https://cloud.tencent.com/developer/article/1886114
官方文档：https://fastapi.tiangolo.com/tutorial/cors/
"""
# 是否启用跨域
CORS_ORIGIN_ENABLE = True
# 只允许访问的域名列表，* 代表所有
ALLOW_ORIGINS = ["*"]
# 是否支持携带 cookie
ALLOW_CREDENTIALS = True
# 设置允许跨域的http方法，比如 get、post、put等。
ALLOW_METHODS = ["*"]
# 允许携带的headers，可以用来鉴别来源等作用。
ALLOW_HEADERS = ["*"]
