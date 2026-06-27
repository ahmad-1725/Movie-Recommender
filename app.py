import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Merge datasets
movie_ratings = pd.merge(ratings, movies, on='movieId')

# Create movie-user matrix
movie_matrix = movie_ratings.pivot_table(
    index='title',
    columns='userId',
    values='rating'
).fillna(0)

# Create similarity matrix
movie_similarity = cosine_similarity(movie_matrix)

similarity_df = pd.DataFrame(
    movie_similarity,
    index=movie_matrix.index,
    columns=movie_matrix.index
)

# Recommendation function
def recommend_movies(movie_name, num_recommendations=5):

    similar_movies = similarity_df[movie_name].sort_values(
        ascending=False
    )

    # Remove selected movie itself
    similar_movies = similar_movies.drop(movie_name)

    similar_movies = similar_movies.head(num_recommendations).index.tolist()
    return similar_movies

# Streamlit UI
st.title("Movie Recommendation System")

st.write("Select a movie to get recommendations.")

# Movie selection
selected_movie = st.selectbox(
    "Choose a Movie",
    movie_matrix.index
)

# Button
if st.button("Recommend"):

    recommendations = recommend_movies(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(movie)