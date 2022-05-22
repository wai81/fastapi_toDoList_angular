from typing import Any, Optional, List

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import status

from models.todo import Todo
from shemas.todo import TodoCreate, TodoUpdate


async def get(todo_id: Any, db: AsyncSession):
    query = select(Todo).where(Todo.id == todo_id)
    result = await db.execute(query)
    obj = result.scalars().first()
    if not obj:
        raise HTTPException(status_code=404, detail="Object not found")
    return obj


async def get_list(db: AsyncSession) -> List[Todo]:
    query = select(Todo)
    result = await db.execute(query)
    obj = result.scalars().all()
    return obj


async def create(obj_in: TodoCreate, db: AsyncSession) -> Todo:
    
    new_obj = Todo(
        title=obj_in.title,
        complited=False
    )
    db.add(new_obj)
    await db.commit()
    await db.refresh(new_obj)
    return new_obj


async def update(db_obj: Todo, obj_in: TodoUpdate, db: AsyncSession) -> Todo:

    obj_data = jsonable_encoder(db_obj)

    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])

    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def remove(obj_id: int, db: AsyncSession) -> Todo:
    try:
        obj = await get(obj_id, db)
        await db.delete(obj)
        await db.commit()
        return obj
    except SQLAlchemyError as ex:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex))

