import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pandas as pd

cred = credentials.Certificate('grey-movie-firebase-adminsdk-9561z-8dadf14839.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Get data from movies.csv and add them to Firestore
filename = 'movies.csv'
movies = pd.read_csv(filename, sep = ',')
size = len(movies.index)
for i in range(size):
    movieId = str(movies.loc[i,'movieId'])
    genres = movies.loc[i,'genres'].split('|')
    data = {
        'title' : movies.loc[i,'title'],
        'genres': genres
    }
    db.collection('movies').document(movieId).set(data)

# Get data from ratings.csv and add them to Firestore
filename = 'ratings.csv'
ratings = pd.read_csv(filename, sep = ',')
avg_ratings = ratings.groupby('movieId', as_index = False)['rating'].mean()
size = len(avg_ratings.index)
for i in range(size):
    movieId = str(avg_ratings.loc[i,'movieId'])
    db.collection('movies').document(movieId).update({
        'rating': avg_ratings.loc[i,'rating']
    })