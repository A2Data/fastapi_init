#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :index_crud
# @Date :2023/7/19 11:25
# @Author :{{ cookiecutter.author_name.lower().replace(' ', '_') }}
# @Desc：CRUD
-------------------------------------------------
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from apps.api.models.index_model import *
from apps.api.schemas.index_schema import *


async def create_index(db: AsyncSession, index: IndexCreate):
    db_index = IndexTable(**index.dict())
    db.add(db_index)
    await db.commit()
    await db.refresh(db_index)
    return db_index


async def get_index(db: AsyncSession, idx_id: int):
    return (await db.execute(select(IndexTable).where(IndexTable.id == idx_id))).scalar_one_or_none()
    # result = await db.execute(select(IndexTable).where(IndexTable.id == idx_id))
    # return result.scalars().first()


async def get_index_list(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(IndexTable).offset(skip).limit(limit))
    return result.scalars().all()


async def update_index(db: AsyncSession, idx: int, index: IndexCreate):
    result = await db.execute(select(IndexTable).where(IndexTable.id == idx))
    db_index = result.scalars().first()
    for key, value in index.dict().items():
        setattr(db_index, key, value)
    await db.commit()
    return db_index


async def delete_index(db: AsyncSession, idx: int):
    result = await db.execute(select(IndexTable).where(IndexTable.id == idx))
    db_index = result.scalars().first()
    await db.delete(db_index)
    await db.commit()
