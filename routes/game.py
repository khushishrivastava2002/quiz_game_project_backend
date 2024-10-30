# routers/game.py
from fastapi import APIRouter, HTTPException
from database import (
    simple_questions_collection,
    medium_questions_collection,
    difficult_questions_collection,
    very_difficult_questions_collection
)
import random

router = APIRouter()

@router.get("/random-question")
async def get_random_question():
    # Fetch random questions from each collection
    simple_questions = await simple_questions_collection.aggregate([{"$sample": {"size": 1}}]).to_list(1)
    medium_questions = await medium_questions_collection.aggregate([{"$sample": {"size": 1}}]).to_list(1)
    difficult_questions = await difficult_questions_collection.aggregate([{"$sample": {"size": 1}}]).to_list(1)
    very_difficult_questions = await very_difficult_questions_collection.aggregate([{"$sample": {"size": 1}}]).to_list(1)

    # Combine and shuffle questions
    questions = simple_questions + medium_questions + difficult_questions + very_difficult_questions
    if not questions:
        raise HTTPException(status_code=404, detail="No questions available")

    question = questions[0]  # Get the first question from the combined list
    hint = hide_answer(question["answer"])
    
    return {
        "question": question["question"],
        "hint": hint,
        # "answer": question["answer"]  # You might want to avoid sending the answer here
    }


def hide_answer(answer: str) -> str:
    """Hides parts of the answer, revealing minimal letters."""
    if len(answer) < 4:
        return "_" * len(answer)  # Hide all letters if the answer is less than 4 characters

    # If the answer has 4 or more characters, only reveal the first and last letters
    hidden_answer = [answer[0]]  # Start with the first character

    # Randomly hide or reveal the middle characters
    for char in answer[1:-1]:  # Iterate through middle characters
        # Randomly decide to hide each middle character
        if random.choice([True] * 3 + [False]):  # 3 out of 4 chances to hide
            hidden_answer.append("_")
        else:
            hidden_answer.append(char)

    hidden_answer.append(answer[-1])  # Add the last character
    return ''.join(hidden_answer)  # Join the list back into a string

