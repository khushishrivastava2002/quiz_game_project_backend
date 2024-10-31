from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import game_sessions_collection
import random
import string

router = APIRouter()

class CreateRoomRequest(BaseModel):
    admin_name: str

async def generate_room_code() -> str:
    """Generate a 4-digit room code."""
    return ''.join(random.choices(string.digits, k=4))

@router.post("/create_room")
async def create_room(data: CreateRoomRequest):
    room_code = await generate_room_code()
    room_data = {
        "room_code": room_code,
        "admin_name": data.admin_name,
        "is_active": True,
        "players": []  # Initialize empty player list
    }
    result = await game_sessions_collection.insert_one(room_data)
    if result.inserted_id:
        return {"room_code": room_code, "message": "Room created successfully!", "admin_name": data.admin_name}
    else:
        raise HTTPException(status_code=500, detail="Failed to create room")

@router.post("/join_room")
async def join_room(room_code: str, user_name: str):
    print(f"Received room_code: {room_code}, user_name: {user_name}")  # Debug log
    
    # Find the active room
    room = await game_sessions_collection.find_one({"room_code": room_code, "is_active": True})
    if not room:
        print("Room not found or inactive")  # Debug log
        raise HTTPException(status_code=404, detail="Room code is not valid or the room is inactive")

    # Determine player number based on current players in the room
    player_number = len(room["players"]) + 1
    player_name = f"Player_{player_number}: {user_name}"
    
    # Update room's player list
    await game_sessions_collection.update_one(
        {"room_code": room_code},
        {"$push": {"players": player_name}}
    )

    # Return updated room details
    return {
        "message": "Successfully joined the room!",
        "room_code": room_code,
        "admin_name": room["admin_name"],
        "players": room["players"] + [player_name]  # Include the latest player
    }
@router.get("/room_details/{room_code}")
async def get_room_details(room_code: str):
    """Fetch room details including admin name and formatted player list."""
    room = await game_sessions_collection.find_one({"room_code": room_code, "is_active": True})
    if not room:
        raise HTTPException(status_code=404, detail="Room not found or inactive")

    # Format the player names as required
    formatted_players = [f"Player_{i + 1}: {name.split(': ')[1]}" for i, name in enumerate(room["players"])]

    return {
        "admin_name": room["admin_name"],
        "players": formatted_players
    }

@router.post("/end_room")
async def end_room(admin_name: str, room_code: str):
    """Ends a room if the admin chooses to end it."""
    # Find the active room with the specified room_code and admin_name
    room = await game_sessions_collection.find_one({"room_code": room_code, "admin_name": admin_name, "is_active": True})
    
    if not room:
        raise HTTPException(status_code=404, detail="Room not found or you are not the admin")

    # Set room as inactive
    result = await game_sessions_collection.update_one({"room_code": room_code}, {"$set": {"is_active": False}})
    
    if result.modified_count:
        return {"message": "Room ended successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to end the room")
    
# In your backend API router
@router.get("/{room_code}")
async def get_room_details(room_code: str):
    """Fetch room details including admin name."""
    room_details = await game_sessions_collection.find_one({"room_code": room_code})
    if room_details:
        return {"adminName": room_details.get("admin_name")}  # Adjust this based on your schema
    raise HTTPException(status_code=404, detail="Room not found")
