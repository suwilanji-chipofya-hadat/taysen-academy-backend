from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances
import numpy as np
import pandas as pd

# recommendation.py

def train_hybrid_recommendation_model(ratings):
    user_course_matrix = ratings.pivot_table(index='user_id', columns='course_id', values='rating', fill_value=0)

    # User-based collaborative filtering
    user_similarity = cosine_similarity(user_course_matrix)
    user_model = pd.DataFrame(user_similarity, index=user_course_matrix.index, columns=user_course_matrix.index)

    # Item-item collaborative filtering
    item_similarity = cosine_similarity(user_course_matrix.T)
    item_model = pd.DataFrame(item_similarity, index=user_course_matrix.columns, columns=user_course_matrix.columns)

    # Combine both models
    hybrid_model = 0.5 * user_model + 0.5 * item_model

    return hybrid_model
def train_user_to_user_recommendation_model(ratings):
    user_course_matrix = ratings.pivot_table(index='user_id', columns='course_id', values='rating', fill_value=0)
    course_user_matrix = user_course_matrix.values.T
    similarity = cosine_similarity(course_user_matrix)

    return pd.DataFrame(similarity, index=user_course_matrix.columns, columns=user_course_matrix.columns)

