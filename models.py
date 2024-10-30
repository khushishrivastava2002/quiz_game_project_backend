from pydantic import BaseModel, EmailStr,Field
from typing import Optional
from datetime import datetime
from bson import ObjectId


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    created_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Question Model
class Question(BaseModel):
    id: Optional[str] = None  # We will use ObjectId for MongoDB
    question: str
    answer: str

class GameSession(BaseModel):
    id: str
    players: list
    scores: dict
    questions: list
    

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)


class Room(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    room_code: str
    admin_id: str
    is_active: bool = True


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    # Add other user-related fields as needed
