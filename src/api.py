from fastapi import FastAPI
from pydantic import BaseModel

from src.rag import ask

app = FastAPI(
    title="AI Customer Support Agent",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Customer Support Agent API is running."
    }


@app.post("/chat")
def chat(request: ChatRequest):

    answer, sources = ask(request.question)

    return {
        "answer": answer,
        "sources": sources
    }