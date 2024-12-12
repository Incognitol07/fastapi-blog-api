# app/utils/config.py

from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "Blog API"
    APP_DESCRIPTION: str = "An API for a blog web application"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")  # Default to 'development'
    DEBUG: bool = ENVIRONMENT == "development"

    # Uncomment this to use a SQLite database
    # DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Comment this to use a SQLite database
    DATABASE_URL: str = 'sqlite:///blog.db'

    # Admin Master Key
    MASTER_KEY: str = os.getenv("MASTER_KEY", "master_key")

    # JWT and authentication settings
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "myjwtsecretkey")  # Default secret

    # Other security settings
    ALLOWED_HOSTS: list = ["*"]
    CORS_ORIGINS: list = ["http://localhost", "http://localhost:3000", "http://localhost:5173"]  # Add frontend URL if applicable

    class Config:
        env_file = ".env"  # Load environment variables from a .env file if available

# Instantiate settings
settings = Settings()
