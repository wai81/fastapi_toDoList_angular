from typing import Optional
from pydantic import BaseModel


class TodoBase(BaseModel):
    title: Optional[str] = None
    complited: bool = False

    
class TodoCreate(TodoBase):
    title: str
    

class TodoUpdate(TodoCreate):
    pass

class TodoShow(TodoBase):
    id: Optional[int] = None
    
    class Config():
        orm_mode = True
        
class Todo(TodoShow):
    pass

