# # routers/game.py
# from fastapi import APIRouter, HTTPException
# from database import (
#     simple_questions_collection,
#     medium_questions_collection,
#     difficult_questions_collection,
#     very_difficult_questions_collection
# )
# import random

# router = APIRouter()

# @router.get("/random-question")
# async def get_random_question():
#     # Fetch random questions from each collection
#     simple_questions = await simple_questions_collection.aggregate([{"$sample": {"size": 1}}]).to_list(1)
#     medium_questions = await medium_questions_collection.aggregate([{"$sample": {"size": 1}}]).to_list(1)
#     difficult_questions = await difficult_questions_collection.aggregate([{"$sample": {"size": 1}}]).to_list(1)
#     very_difficult_questions = await very_difficult_questions_collection.aggregate([{"$sample": {"size": 1}}]).to_list(1)

#     # Combine and shuffle questions
#     questions = simple_questions + medium_questions + difficult_questions + very_difficult_questions
#     if not questions:
#         raise HTTPException(status_code=404, detail="No questions available")

#     question = questions[0]  # Get the first question from the combined list
#     hint = hide_answer(question["answer"])
    
#     return {
#         "question": question["question"],
#         # "hint": hint,
#         # "answer": question["answer"]  # You might want to avoid sending the answer here
#     }


# def hide_answer(answer: str) -> str:
#     """Hides parts of the answer, revealing minimal letters."""
#     if len(answer) <= 4:
#         return "_" * len(answer)  # Hide all letters if the answer is less than 4 characters

#     # If the answer has 4 or more characters, only reveal the first and last letters
#     hidden_answer = [answer[0]]  # Start with the first character

#     # Randomly hide or reveal the middle characters
#     for char in answer[1:-1]:  # Iterate through middle characters
#         # Randomly decide to hide each middle character
#         if random.choice([True] * 3 + [False]):  # 3 out of 4 chances to hide
#             hidden_answer.append("_")
#         else:
#             hidden_answer.append(char)

#     hidden_answer.append(answer[-1])  # Add the last character
#     return ''.join(hidden_answer)  # Join the list back into a string


# ----------------code-------------------------------


# routers/game.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from database import (
    simple_questions_collection,
    medium_questions_collection,
    difficult_questions_collection,
    very_difficult_questions_collection,
    game_sessions_collection
)
from bson import ObjectId
import random

router = APIRouter()

# Keep track of active connections
class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

@router.websocket("/ws/game/{room_id}")
async def websocket_game_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Process the received data
            await websocket.send_text(f"You said: {data}")
    except WebSocketDisconnect:
        print(f"Client disconnected from room {room_id}")


async def fetch_question(game_state):
    """Fetch a random question from each collection."""
    collections = [
        simple_questions_collection,
        medium_questions_collection,
        difficult_questions_collection,
        very_difficult_questions_collection
    ]
    collection = random.choice(collections)
    question = await collection.aggregate([{"$sample": {"size": 1}}]).to_list(1)
    return question[0] if question else None


def hide_answer(answer: str) -> str:
    """Initial hint with some letters hidden."""
    if len(answer) <= 4:
        return "_" * len(answer)
    hidden_answer = [answer[0]] + ["_" for _ in answer[1:-1]] + [answer[-1]]
    return ''.join(hidden_answer)


def reveal_hint(hint: str, answer: str) -> str:
    """Reveal additional random letters."""
    hint_list = list(hint)
    for i, char in enumerate(hint_list):
        if char == "_":
            hint_list[i] = answer[i]  # Reveal original letter in place of "_"
            break
    return ''.join(hint_list)


def check_guess(guess: str, answer: str, hint: str) -> (bool, str): # type: ignore
    """Check guess and update hint if wrong."""
    if guess.lower() == answer.lower():
        return True, hint
    return False, hint


async def start_game_session(room_id: str):
    """Start a new game session."""
    game_session = {
        "room_id": room_id,
        "current_question": 0,
        "scores": {}
    }
    await game_sessions_collection.insert_one(game_session)
    return game_session


async def update_score(room_id: str, user_id: str, points: int):
    """Update the score for a user."""
    await game_sessions_collection.update_one(
        {"room_id": room_id},
        {"$inc": {f"scores.{user_id}": points}}
    )
