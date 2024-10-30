from fastapi import APIRouter, HTTPException, Depends, Response
from passlib.context import CryptContext
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from database import users_collection
from models import UserCreate, UserLogin, UserResponse
from utils import hash_password, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from dependencies import get_current_user

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    user_data = {
        "username": user.username,
        "email": user.email,
        "password_hash": hashed_password,
        "created_at": datetime.utcnow()
    }
    result = await users_collection.insert_one(user_data)
    user_data["_id"] = str(result.inserted_id)
    return UserResponse(id=user_data["_id"], username=user.username, email=user.email, created_at=user_data["created_at"])

@router.post("/login")
async def login(user: UserLogin):
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user["email"]}, expires_delta=access_token_expires
    )

    response = JSONResponse({"access_token": access_token, "token_type": "bearer"})
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True, 
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60, 
        samesite="strict"
    )
    return response

@router.get("/logout")
async def logout():
    response = JSONResponse({"message": "User logged out successfully"})
    response.delete_cookie(key="access_token")  # Clear the access token cookie
    return response

@router.get("/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    return {"username": current_user["username"], "email": current_user["email"]}
