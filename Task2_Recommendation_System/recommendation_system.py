import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Program Started")

movies = pd.read_csv("movies.csv")
print("Dataset Loaded")

movies["genres"] = movies["genres"].fillna("")
movies["genres"] = movies["genres"].str.replace("|", " ", regex=False)

cv = CountVectorizer()
vectors = cv.fit_transform(movies["genres"])

similarity = cosine_similarity(vectors)

print("Similarity Matrix Created")

def recommend(movie_name):
    movie_name = movie_name.lower()

    matches = movies[movies["title"].str.lower().str.contains(movie_name, na=False)]

    if matches.empty:
        print("Movie not found!")
        return

    index = matches.index[0]

    distances = list(enumerate(similarity[index]))
    recommended_movies = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    print("\nRecommended Movies:\n")

    for movie in recommended_movies:
        print(movies.iloc[movie[0]]["title"])

movie = input("Enter movie name: ")
recommend(movie)