from fastapi import FastAPI
from .routes import question_routes, answer_routes

app = FastAPI()

app.include_router(question_routes.router)
app.include_router(answer_routes.router)