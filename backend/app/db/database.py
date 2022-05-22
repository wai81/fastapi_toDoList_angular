from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import settings
from db.base import Base

#Base = declarative_base()

SQLALCHEMY_DATABASE_URL = settings.DB_CONFIG

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# Dependency
async def db() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError as sql_ex:
            await session.rollback()
            raise sql_ex
        except HTTPException as http_ex:
            await session.rollback()
            raise http_ex
        finally:
            await session.close()
            
'''

class AsyncDatabaseSession:
    def __init__(self):
        self._session = None
        self._engine = None
        
    def __getattr__(self, name):
        return getattr(self._session, name)
    
    def init(self):
        self._engine = create_async_engine(
            settings.DB_CONFIG,
            future=True,
            echo=True,
        )
        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )()
        
    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            
db=AsyncDatabaseSession()
'''
