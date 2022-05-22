import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict, Any, Optional, List
from pydantic import validator, AnyHttpUrl


env_path = Path('') / '.env'

load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "ToDo API"
    PROJECT_VERSION: str = "0.0.1"
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASS")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT", 5432)
         
    DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
settings = Settings()
