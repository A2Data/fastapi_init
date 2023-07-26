#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :logger
# @Date :2023/7/6 02:36
# @Author : {{ cookiecutter.author_name }}
# @Desc： 日志处理类
-------------------------------------------------
"""
from loguru import logger
import os
import datetime
import sys

from apps.core.base.BaseSettings import LogsDay, BASE_DIR

"""
# 日志简单配置
# 具体其他配置 可自行参考 https://github.com/Delgan/loguru
"""

# 保留时间,如果不设置 默认为 10 天
log_days = f"{LogsDay} days"

# 日志 path,如果不设置 默认在当前路径下
log_path = os.path.join(BASE_DIR, 'logs')


def setup_logger(log_dir: str = ".././logs", retention: str = "10 days", rotation: str = "1 day",
                 format: str = "{time:YYYY/MM/DD HH:mm:ss}  {level}: {extra} {message}",
                 level: str = "INFO"):
    """
    配置 logger
    :param log_dir: 日志文件保存的路径
    :param retention: 日志文件的保留时间
    :param rotation: 日志文件的切换时间
    :param format: 日志输出的格式
    :param level: 日志的输出等级
    """

    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    now = datetime.datetime.now().strftime("%Y%m%d_%H")
    log_file_name = f"{log_dir}/log_{now}.log"

    logger.remove()

    logger.add(
        sink=log_file_name, rotation=rotation, retention=retention, level=level, format=format, colorize=True,
        enqueue=True
    )
    # 添加stdout输出，使得log可以同时打印在控制台和文件中
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green><level>{level: <8} </level></green> | <blue> {time:YYYY/MM/DD HH:mm:ss} </blue> |  <cyan>{"
               "name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <yellow>\n<level>{message}</level>"
               "</yellow>\n"
               "<red>Method:_ </red> <magenta>{extra} </magenta>",
        enqueue=True
    )
    return logger


log = setup_logger(log_path)
