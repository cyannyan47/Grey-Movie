from fastapi import FastAPI, Query

from typing import List
from pydantic import BaseModel
from enum import Enum

from fastapi.middleware.cors import CORSMiddleware

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from logic.demo import rec_movies, list_of_genres

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
    rec_5_movies = rec_movies(list_of_genres(moods))
    return rec_5_movies

@app.get("/test/")
def getTest():
    return {"testing": "complete"}