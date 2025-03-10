from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .chatbot import get_reply

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    return get_reply(data["message"])

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "OK"}