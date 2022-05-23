import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from api.base import api_router

origins_ = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3030",
    "http://loalhost:4200",
    "http://127.0.0.1:4200",
]

origins = ["*"]

def include_route(app):
    app.include_router(api_router)
    

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )
    
    include_route(app)
    return app

app = start_application()

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host='127.0.0.1')
