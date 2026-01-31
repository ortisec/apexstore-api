from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    DATABASE_URL: str
    CORS_ORIGINS: str
    

    API_V1_PREFIX: str = "/api/v1"
    APP_NAME: str = "ApexStore API"
    ENV: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def CORS_ORIGINS(self) -> List[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS_RAW.split(",")]

settings = Settings()
