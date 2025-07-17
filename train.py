import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset (modify the file path if needed)
movies_data = pd.read_csv("D:\\NIVEDHA\\N\\PROJECT\\MACHINE LEARNING\\movies.csv")  # Ensure this file has a 'title' & 'description' column

# Fill missing values (if any)
movies_data['overview'] = movies_data['overview'].fillna("")

# Convert text data to numerical vectors
vectorizer = TfidfVectorizer(stop_words="english")
movie_vectors = vectorizer.fit_transform(movies_data['overview'])

# Compute similarity scores
similarity = cosine_similarity(movie_vectors)

# Save model components
with open("model.pkl", "wb") as file:
    pickle.dump((movies_data, vectorizer, similarity), file) 

print("Model trained and saved successfully!")
