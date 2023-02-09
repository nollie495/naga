from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

current_direction = Direction.UP

@app.get("/")
async def root():
    return {"message": "Naga"}

@app.post("/start")
async def start():
    return "ok"

@app.post("/end")
async def end():
    return "ok"

@app.post("/move")
@app.get("/move")
async def move():
    return {"move": current_direction.name.lower()}

@app.post("/turn")
async def turn(body: dict):
    global current_direction
    current_direction = Direction[body["move"].upper()]
    return {"move": current_direction}