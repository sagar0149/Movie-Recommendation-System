import pandas as pd

from models.content_based import (
    content_recommend
)

ratings = pd.read_csv(
    "dataset/ratings.csv"
)

movies = pd.read_csv(
    "dataset/movies.csv"
)


def hybrid_recommend(
        movie_title,
        top_n=10):

    recommendations = content_recommend(
        movie_title,
        top_n
    )

    return recommendations