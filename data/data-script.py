#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore

import pandas as pd

#cred = credentials.Certificate('grey-movie-firebase-adminsdk-9561z-8dadf14839.json')


# Get data from movies.csv
filename = 'movies.csv'
movies = pd.read_csv(filename, sep = ',')
size = len(movies.index)
for i in range(size):
    print(movies.loc[i,'movieId'])
    print(movies.loc[i,'title'])
    genres = movies.loc[i,'genres'].split('|')
    for genre in genres:
        print(genre)

# Get data from ratings.csv
filename = 'ratings.csv'
ratings = pd.read_csv(filename, sep = ',')
avg_ratings = ratings.groupby('movieId', as_index = False)['rating'].mean()
size = len(avg_ratings.index)
for i in range(size):
    print(avg_ratings.loc[i,'movieId'])
    print(avg_ratings.loc[i,'rating'])