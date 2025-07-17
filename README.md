# 🎬 Movie Recommendation System

A personalized movie recommendation system built using Python, and cosine similarity. It suggests movies similar to the user's input based on content features.

---

## 📌 Features

- Recommends similar movies based on content (title, genre, keywords, etc.)
- Uses **cosine similarity** for computing movie closeness
- Interactive console or web interface (extendable to Streamlit/Flask)
- Clean and efficient code using **Pandas** and **scikit-learn**

## 🛠️ Tech Stack

- Python 3.x  
- Pandas  
- scikit-learn  
- Jupyter Notebook / Flask / Streamlit (optional)



## 📂 Dataset

- [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
- Fields used: `title`, `genres`, `keywords`, `overview`, `cast`, `crew`



## 🚀 How It Works

1. Combines important features (genre, keywords, etc.) into a single string
2. Converts them to vector space using **CountVectorizer**
3. Calculates **cosine similarity** between all movie vectors
4. Returns top N similar movies based on a given input title

---

# ▶️ HOW TO RUN

1. Clone the repository:

```
git clone https://github.com/NivedhaJM/Movie-Recommendation-System.git

cd Movie-Recommendation-System
 ```

2. Extract all files, including `movies.zip`

 🎯 **Note**: `movies.zip` contains the dataset. Make sure to extract it in the same folder where `app.py` or `train.py` is located. It should contain the file `movies.csv`.

3. Run the training script: **`python train.py`**

This will generate a `model.pkl` file.

4. Launch the app: **`python app.py`**

5. Open the `localhost` URL provided in the terminal in your browser.



## OUTPUT

The Movie Recommendation UI will load in your browser.

Enter a movie name and click `Get Recommendations` — you’ll get a list of similar movies instantly!


## 📸 SCREENSHOT

[Movie Recommendation UI](./assets/ui-screenshot.png)


## 📈 Future Improvements

- Deploy using Flask or Streamlit for a web UI

- Add collaborative filtering (user-based recommendations)

- Include ratings and popularity scores for better results


# 🤝 Contributions
Pull requests and suggestions are welcome!
