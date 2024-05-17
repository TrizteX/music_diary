import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, EmailStr, HttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1
    BACKEND_CORS_ORIGINS : List = []
    PROJECT_NAME: str
    SUPERUSER: str
    SUPERUSER_PASSWORD: str
    ALGORITHM: str
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str
    EMAIL_TEST_USER: EmailStr = "dev@example.com"
    TOKEN_USER: str = "str"
    TOKEN_PASSWORD: str = "str"
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
