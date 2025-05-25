"""
Application Settings
Configuration settings for the application.
"""

# TODO: Add MongoDB settings
# TODO: Add Redis settings
# TODO: Add API settings
# TODO: Add logging configuration
from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str
    debug: bool
    environment: str
    
    mongodb_url: str
    redis_host: str
    redis_port: int
    
    api_host: str
    api_port: int
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()