from fastapi import APIRouter
from model import generate_answer

router = APIRouter()

@router.get("/")
def home():
    return {"message": "API Astra-test en ligne"}

@router.post("/ask")
def ask_ai(prompt: str):
    response = generate_answer(prompt)
    return {"prompt": prompt, "response": response}
