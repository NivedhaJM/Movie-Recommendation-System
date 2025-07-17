import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
movies_data = pd.read_csv("D:\\NIVEDHA\\N\\PROJECT\\MACHINE LEARNING\\movies.csv")

# Select relevant features
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Combine features into a single string
movies_data['combined_features'] = (movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' +
                                    movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' +
                                    movies_data['director'])

# Convert text to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(movies_data['combined_features'])

# Compute similarity matrix
similarity = cosine_similarity(feature_vectors)

# Save model and data
with open("model.pkl", "wb") as file:
    pickle.dump((movies_data, vectorizer, similarity), file)

print("Model saved as model.pkl")
