from fastapi import FastAPI, Query

from typing import List
from pydantic import BaseModel
from enum import Enum

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class Mood(str, Enum):
    happy = "Happy"
    sad = "Sad"
    hurt = "Hurt"
    angery = "Angery"
    tired = "Tired"
    loved = "Loved"
    thrilled = "Thrilled"

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getmovies/")
def getMoviesRecommendation(moods: List[Mood] = Query(...)):
    return moods

@app.get("/test/")
def getTest():
    return {"testing": "complete"}