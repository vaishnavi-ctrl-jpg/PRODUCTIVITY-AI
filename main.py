import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from agent import root_agent

load_dotenv()

app = FastAPI(title="Productivity AI", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    app_name="productivity_assistant",
    session_service=session_service
)

APP_NAME = "productivity_assistant"
user_sessions = {}


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = "default"


class ChatResponse(BaseModel):
    reply: str
    session_id: str
    status: str


@app.get("/health")
def health():
    return {"status": "healthy", "agent": "productivity_assistant", "version": "2.0.0"}


@app.get("/sessions")
def sessions():
    return {"active_sessions": list(user_sessions.keys()), "count": len(user_sessions)}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    session_id = request.session_id or "default"

    if session_id not in user_sessions:
        session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=session_id
        )
        user_sessions[session_id] = session.id

    message = Content(role="user", parts=[Part(text=request.message)])
    response_text = ""

    async for event in runner.run_async(
        user_id=session_id,
        session_id=user_sessions[session_id],
        new_message=message
    ):
        if event.is_final_response() and event.content:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text

    if not response_text:
        raise HTTPException(status_code=500, detail="No response from agent.")

    return ChatResponse(reply=response_text, session_id=session_id, status="success")


@app.get("/")
def serve_ui():
    ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    if os.path.exists(ui_path):
        return FileResponse(ui_path, media_type="text/html")
    return {"status": "running", "message": "Productivity AI API", "docs": "/docs"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
