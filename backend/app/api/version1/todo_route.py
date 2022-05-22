from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from shemas.todo import TodoCreate, TodoUpdate
from shemas.todo import Todo
from crud.crud_todo import get_list, get, create, update, remove
from db.database import db

router = APIRouter()

@router.get("/", response_model=List[Todo])
async def list_items(db: AsyncSession = Depends(db)) -> Any:
    obj = await(get_list(db=db))
    return obj


@router.get("/{todo_id}", response_model=Todo)
async def get_item(todo_id: int, db: AsyncSession = Depends(db)):
    obj = await get(todo_id=todo_id, db=db)
    return obj

    
@router.post("/", response_model=Todo)
async def create_item(todo_in: TodoCreate, db: AsyncSession = Depends(db)):
    obj = await create(obj_in=todo_in, db=db)
    return obj


@router.put("/{todo_id}", response_model=Todo)
async def update_item(todo_id: int, obj_in: TodoUpdate, db: AsyncSession = Depends(db)):
    obj_exist = await get(todo_id=todo_id, db=db)
    if not obj_exist:
        raise HTTPException(
            status_code=404,
            detail="Todo dose not exist",
        )        
    obj = await update(db_obj=obj_exist, obj_in=obj_in, db=db)
    return obj


@router.delete("/{todo_id}", response_model=Todo)
async def delete_item(todo_id: int, db: AsyncSession =Depends(db)):
    obj_exist = await get(todo_id=todo_id, db=db)
    if not obj_exist:
        raise HTTPException(
            status_code=404,
            detail="Todo dose not exist",
        )
    obj = await remove(obj_id=todo_id, db=db)
    return obj
