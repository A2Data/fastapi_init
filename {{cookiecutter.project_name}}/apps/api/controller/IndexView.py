#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :index_view
# @Date :2023/7/19 11:23
# @Author :{{ cookiecutter.author_name.lower().replace(' ', '_') }}
# @Desc：
-------------------------------------------------
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from apps.api.schemas.index_schema import *
from apps.api.service import index_crud
from apps.api.service.index_crud import create_index
from apps.core.db.database import get_async_session
from apps.utils.response import SuccessResponse

index_router = APIRouter()


@index_router.get("/index", summary="初始化项目views")
async def index():
    data = [
        {"id": 1, "name": "Fast-API", "desc": "基于FastAPI的后端项目"},
        {"id": 2, "name": "Jack", "desc": "撰写 《Python和FastAPI高性能Web开发实战》"}
    ]

    return SuccessResponse(data)


@index_router.post("/index/", response_model=Index, summary="创建 Index 数据")
async def create_index_route(index: IndexCreate, db: AsyncSession = Depends(get_async_session)):
    return await create_index(db=db, index=index)


@index_router.get("/index/", response_model=List[Index], summary="分页查询数据")
async def read_index(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_session)):
    db_idx = await index_crud.get_index_list(db, skip=skip, limit=limit)
    return db_idx


@index_router.get("/index/{index_id}", response_model=Index, summary="根据 id 查询")
async def read_index(idx: int, db: AsyncSession = Depends(get_async_session)):
    db_idx = await index_crud.get_index(db, idx_id=idx)
    if db_idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_idx


@index_router.put("/index/{index_id}", response_model=Index, summary="根据 id 更新")
async def update_index(idx_id: int, index: IndexCreate, db: AsyncSession = Depends(get_async_session)):
    return await index_crud.update_index(db=db, idx=idx_id, index=index)


@index_router.delete("/index/{index_id}", summary="根据 id 删除")
async def delete_index(idx: int, db: AsyncSession = Depends(get_async_session)):
    await index_crud.delete_index(db=db, idx=idx)
    return {"detail": "Index deleted"}
