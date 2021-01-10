from fastapi import FastAPI

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = FastAPI()

@app.get("/getmovie/")
def read_user():
    return {"test": "true"}