from sqlalchemy import Column, Integer, String, Boolean
from db.base import Base


class Todo(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    complited = Column(Boolean(), default=False)
    
        