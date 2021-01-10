from fastapi import FastAPI, Query

from typing import List
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Mood(str, Enum):
    happy = "Happy"
    sad = "Sad"
    hurt = "Hurt"
    angery = "Angery"
    tired = "Tired"
    loved = "Loved"
    thrilled = "Thrilled"


@app.get("/getmovies/")
def getMoviesRecommendation(moods: List[Mood] = Query(...)):
    return moods