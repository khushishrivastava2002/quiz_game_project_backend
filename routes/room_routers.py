import random
from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from database import users_collection, game_sessions_collection, db

from pydantic import BaseModel

router = APIRouter()


async def generate_room_code():
    """Generates a 4-digit room code and ensures it's unique."""
    while True:
        code = f"{random.randint(1000, 9999)}"
        existing_room = await game_sessions_collection.find_one({"room_code": code, "is_active": True})
        if not existing_room:
            return code


# Define a Pydantic model for the request body
class CreateRoomRequest(BaseModel):
    admin_name: str

@router.post("/create_room")
async def create_room(data: CreateRoomRequest):
    room_code = await generate_room_code()
    room_data = {
        "room_code": room_code,
        "admin_name": data.admin_name,
        "is_active": True,
    }
    result = await game_sessions_collection.insert_one(room_data)
    if result.inserted_id:
        return {"room_code": room_code, "message": "Room created successfully!"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create room")



@router.post("/join_room")
async def join_room(room_code: str, user_name: str):
    print(f"Received room_code: {room_code}, user_name: {user_name}")  # Debug log
    room = await game_sessions_collection.find_one({"room_code": room_code, "is_active": True})
    if not room:
        print("Room not found or inactive")  # Debug log
        raise HTTPException(status_code=404, detail="Room code is not valid or the room is inactive")
    return {"message": "Successfully joined the room!"}




@router.post("/end_room")
async def end_room(admin_name: str, room_code: str):
    """Ends a room if the admin chooses to end it."""
    room = await game_sessions_collection.find_one({"room_code": room_code, "admin_name": admin_name, "is_active": True})
    if not room:
        raise HTTPException(status_code=404, detail="Room not found or you are not the admin")

    # Set room as inactive
    result = await game_sessions_collection.update_one({"room_code": room_code}, {"$set": {"is_active": False}})
    if result.modified_count:
        return {"message": "Room ended successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to end the room")