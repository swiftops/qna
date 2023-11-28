from pydantic import BaseModel

class Answer(BaseModel):
    id: str
    question_id: str
    answer_text: str