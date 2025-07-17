from flask import Flask, request, jsonify, render_template
import pickle
import difflib

# Load the trained model
with open("model.pkl", "rb") as file:
    movies_data, vectorizer, similarity = pickle.load(file)

app = Flask(__name__) #--> initialise web app

@app.route('/')
def home():
    return render_template("index.html") 

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie')

    if not movie_name:
        return jsonify({"error": "Please provide a movie name"}), 400

    # Get closest match
    list_of_titles = [str(title) for title in movies_data['title'].dropna()]

    close_match = difflib.get_close_matches(movie_name, list_of_titles, n=3)

    if not close_match:
        return jsonify({"error": "Movie not found"}), 404

    movie_index = movies_data[movies_data.title == close_match[0]].index[0]
    similarity_scores = list(enumerate(similarity[movie_index]))
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:6]

    recommendations = [movies_data.iloc[movie[0]]['title'] for movie in sorted_movies]

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
