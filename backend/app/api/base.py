from fastapi import APIRouter
from api.version1 import todo_route

api_router = APIRouter()
api_router.include_router(todo_route.router, prefix="/todos", tags=["Todos"])