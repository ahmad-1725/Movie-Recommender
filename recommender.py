import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# print("\n Head", movies.head())
# print("\n", ratings.head())

# print("\n Shape", movies.shape)
# print("\n", ratings.shape)

# print("\n Info", movies.info())
# print("\n", ratings.info())

# print("\n Describe", movies.describe())
# print("\n", ratings.describe())

# print("\n Null Sum", movies.isnull().sum())
# print("\n", ratings.isnull().sum())

movie_ratings = pd.merge(ratings, movies, on="movieId")


interaction_matrix = movie_ratings.pivot_table(
    index="userId", columns="title", values="rating"
)

# filling missing values
interaction_matrix = interaction_matrix.fillna(0)
# print(interaction_matrix.head())

similarity_matrix = cosine_similarity(interaction_matrix)
# print(similarity_matrix)

similarity_df = pd.DataFrame(
    similarity_matrix, index=interaction_matrix.index, columns=interaction_matrix.index
)

# recommender function
def recommend_movies(user_id, num_recommendations=5):

    similar_users = similarity_df[user_id].sort_values(ascending=False)

    # remove the user himself being counted as similar user
    similar_users = similar_users.drop(user_id)

    top_user = similar_users.index[0]

    print(f"\nMost similar user to User {user_id}: User {top_user}")

    # Movies that the user has watched
    user_movies = interaction_matrix.loc[user_id]
    # if watched then rating > 0
    watched_movies = user_movies[user_movies > 0].index.tolist()

    # Movies that the similar user has watched

    similar_user_movies = interaction_matrix.loc[top_user]

    # recommend movies that the similar user has rated higher than 4
    recommended_movies = similar_user_movies[similar_user_movies > 4].index.tolist()

    final_recommendations = []

    # do not include movies that have already been watched
    for movie in recommended_movies:
        if movie not in watched_movies:
            final_recommendations.append(movie)
    return final_recommendations


recommendations = recommend_movies(1)

print("\nTotal Recommendations : ",len(recommendations))

print("\nRecommended Movies : ")
for movie in recommendations:
    print(movie)