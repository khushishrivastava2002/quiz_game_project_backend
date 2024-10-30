from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from pydantic_settings import BaseSettings
from bson import ObjectId


class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "quiz_game"

settings = Settings()

client = AsyncIOMotorClient(settings.MONGODB_URL)
db = client[settings.DATABASE_NAME]
users_collection = db["users"]
simple_questions_collection = db["simple_questions"]
medium_questions_collection = db["medium_questions"]
difficult_questions_collection = db["difficult_questions"]
very_difficult_questions_collection = db["very_difficult_questions"]
game_sessions_collection = db["game_sessions"]