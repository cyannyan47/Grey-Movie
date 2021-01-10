import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred=credentials.Certificate('../private/grey-movie-firebase-adminsdk-9561z-75f6d847e7.json')
firebase_admin.initialize_app(cred)
db=firestore.client()

mood_dict={
    "Happy":["Western", "Mystery", "Action", "Thriller", "Fantasy", "Sci-Fi"],
    "Sad":["Romance", "Comedy", "Musical", "Animation", "Drama"],
    "Hurt":["Film-Noir", "Comedy", "Musical", "Crime", "Drama"],
    "Angry":["Western", "Action", "War", "Horror", "Crime", "Drama"],
    "Tired":["Romance", "Comedy", "Musical", "Documentary", "Animation", "Children"],
    "Loved":["Romance", "Adventure", "Comedy", "Musical", "Drama"],
    "Thrilled":["Western", "Adventure", "Thriller", "Fantasy", "Sci-Fi"]
}

def jaccard_index(list1, list2):
    return len(set(list1).intersection(list2))/len(set(list1).union(list2))
    
# Initialize user's input
user_moods=["Sad", "Tired"]

def list_of_genres(user_moods):
    l=mood_dict[user_moods[0]]
    for i in range(len(user_moods)-1):
        if len(set(l).intersection(mood_dict[user_moods[i+1]]))==0:
            l=set(l).union(mood_dict[user_moods[i+1]])
        else:
            l=set(l).intersection(mood_dict[user_moods[i+1]])
        i+=1
    return list(l) 

#print(list_of_genres(user_moods))
def rec_movies(l):
    rec_movies=[]
    movies=db.collection('movies').stream()
    arr=[]
    for movie in movies:
        arr.append(movie.to_dict())
    count=0
    while count<5:
        rec_mov=arr[0]
        for i in range(len(arr)-1):
            if jaccard_index(l, rec_mov['genres']) < jaccard_index(l, arr[i+1]['genres']):
                rec_mov=arr[i+1]
        rec_movies.append(rec_mov['title'])
        arr.remove(rec_mov)
        count+=1
    return rec_movies

# Test 
print(rec_movies(list_of_genres(user_moods)))