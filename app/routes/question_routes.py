from fastapi import APIRouter
from ..models.question import Question
from pymongo import MongoClient

router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

@router.post("/questions/")
async def create_question(question: Question):
    question_dict = question.dict()
    db.questions.insert_one(question_dict)
    return question_dict