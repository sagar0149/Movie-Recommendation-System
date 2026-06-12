import pandas as pd

movies = pd.read_csv(
    "dataset/movies.csv"
)

ratings = pd.read_csv(
    "dataset/ratings.csv"
)


def total_movies():
    return len(movies)


def total_ratings():
    return len(ratings)


def average_rating():
    return round(
        ratings["rating"].mean(),
        2
    )