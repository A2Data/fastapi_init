#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :database
# @Date :2023/7/5 20:25
# @Author :{{ cookiecutter.author_name.lower().replace(' ', '_') }}
# @Desc：SQLAlchemy 部分
-------------------------------------------------
"""
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from apps.core.base.BaseSettings import *

"""
echo=True表示引擎将用repr()函数记录所有语句及其参数列表到日志
由于SQLAlchemy是多线程，指定check_same_thread=False来让建立的对象任意线程都可使用。这个参数只在用SQLite数据库时设置
"""
engine = create_async_engine(
    SQLITE_DATABASE_URL,
    encoding='utf-8',
    echo=SQLITE_ECHO,
    future=True,
    connect_args={'check_same_thread': False}
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class CustomBase:
    """
    将表名统一为小写
    """

    @declared_attr
    def __tablename__(cls):
        # 如果有自定义就取自定义，否则就取小写类名
        if hasattr(cls, "__table__") and cls.__table__ is not None:
            table_name = cls.__table__.name
        else:
            model_name = cls.__name__
            ls = []
            for index, char in enumerate(model_name):
                if char.isupper() and index != 0:
                    ls.append("_")
                ls.append(char.lower())
            table_name = "".join(ls)
        return table_name


# 创建基本映射类
Base = declarative_base(cls=CustomBase)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    获取主数据库
    """
    async with async_session() as session:
        yield session
