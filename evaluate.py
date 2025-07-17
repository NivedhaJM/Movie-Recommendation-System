from app import recommend  # Import the recommend function from app.py

def precision_at_k(recommend_func, ground_truth, k=5):
    correct_predictions = 0
    total_movies = len(ground_truth)

    for movie, relevant_movies in ground_truth.items():
        recommendations = recommend(movie)[:k]  # Get top-K recommendations
        correct_predictions += len(set(recommendations) & set(relevant_movies))

    return correct_predictions / (total_movies * k)

# Example ground truth dataset (Movie: [Relevant Movies])
ground_truth = {
    "Inception": ["Interstellar", "The Prestige", "Memento", "Shutter Island"],
    "The Dark Knight": ["Batman Begins", "The Dark Knight Rises", "Joker", "Man of Steel"]
}

accuracy = precision_at_k(recommend, ground_truth, k=5)
print(f"Model Accuracy (Precision@5): {accuracy:.2f}")
