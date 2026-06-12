import plotly.express as px
import pandas as pd

movies = pd.read_csv(
    "dataset/movies.csv"
)

ratings = pd.read_csv(
    "dataset/ratings.csv"
)


def genre_chart():

    genres = (
        movies["genres"]
        .str.split("|")
        .explode()
        .value_counts()
    )

    fig = px.pie(
        values=genres.values,
        names=genres.index,
        title="Genre Distribution"
    )

    return fig


def rating_chart():

    fig = px.histogram(
        ratings,
        x="rating",
        nbins=10,
        title="Rating Distribution"
    )

    return fig