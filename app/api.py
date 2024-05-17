from . import schemas
import app.schemas as schemas
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict
import datetime

app = FastAPI()
@app.post(
    "/get_link",
    tags=["chatbot"]
)
async def get_link(
    _model: schemas.ChatReq
    
):
    return {'pl_link': 'https://open.spotify.com/playlist/6Lk8l0fYwTX2axjx3bQvyb?si=7e29067ba72149ee'}

