from fastapi import APIRouter
from ..models.answer import Answer
from pymongo import MongoClient

router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

@router.post("/answers/")
async def create_answer(answer: Answer):
    answer_dict = answer.dict()
    db.answers.insert_one(answer_dict)
    return answer_dict