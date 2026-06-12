from surprise import Dataset
from surprise import Reader
from surprise import SVD

import pandas as pd

ratings = pd.read_csv("dataset/ratings.csv")

reader = Reader(rating_scale=(0.5, 5))

data = Dataset.load_from_df(
    ratings[["userId", "movieId", "rating"]],
    reader
)

trainset = data.build_full_trainset()

model = SVD()

model.fit(trainset)


def predict_rating(user_id, movie_id):
    return model.predict(
        user_id,
        movie_id
    ).est