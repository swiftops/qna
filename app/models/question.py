from pydantic import BaseModel

class Question(BaseModel):
    id: str
    question_text: str