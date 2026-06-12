import streamlit as st
import pandas as pd

from dashboard.analytics import (
    total_movies,
    total_ratings,
    average_rating
)

from dashboard.charts import (
    genre_chart,
    rating_chart
)

from models.hybrid import (
    hybrid_recommend
)

movies = pd.read_csv(
    "dataset/movies.csv"
)

st.set_page_config(
    page_title="Movie Recommendation Engine",
    layout="wide"
)

st.title(
    "🎬 Hybrid Movie Recommendation Engine"
)

# Metrics

c1, c2, c3 = st.columns(3)

c1.metric(
    "Movies",
    total_movies()
)

c2.metric(
    "Ratings",
    total_ratings()
)

c3.metric(
    "Average Rating",
    average_rating()
)

st.divider()

movie = st.selectbox(
    "Choose Movie",
    movies["title"]
)

if st.button(
        "Recommend Movies"):

    recs = hybrid_recommend(
        movie
    )

    st.subheader(
        "Recommended Movies"
    )

    st.dataframe(recs)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        genre_chart(),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        rating_chart(),
        use_container_width=True
    )