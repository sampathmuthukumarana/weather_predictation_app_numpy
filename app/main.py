from fastapi import FastAPI
from pydantic import BaseModel
from app.ai import call_model

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = await call_model(request.message)
    return ChatResponse(reply=reply)
