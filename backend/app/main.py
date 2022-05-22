import uvicorn
from fastapi import FastAPI
from core.config import settings
from api.base import api_router

def include_route(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_route(app)
    return app

app = start_application()

if __name__ == '__main__':
    uvicorn.run("main:app", port=4000, host='127.0.0.1')
