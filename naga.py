from fastapi import FastAPI
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

current_direction = Direction.UP

@app.get("/")
async def root():
    return {"apiversion": "1", "author": "Naga", "color": "#FAFA33", "head": "gamer", "tail": "mouse","version": "0.0.1"}

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

@app.get("/left")
async def left():
    global current_direction
    current_direction = Direction.LEFT
    return {"move": current_direction}

@app.get("/up")
async def up():
    global current_direction
    current_direction = Direction.UP
    return {"move": current_direction}

@app.get("/right")
async def right():
    global current_direction
    current_direction = Direction.RIGHT
    return {"move": current_direction}

@app.get("/down")
async def down():
    global current_direction
    current_direction = Direction.DOWN
    return {"move": current_direction}
