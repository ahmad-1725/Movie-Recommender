# Movie Recommendation System

A Movie Recommendation System built using Python, Pandas, Scikit-learn, and Streamlit that recommends similar movies using collaborative filtering techniques and cosine similarity.

## Features

* Movie-based recommendation system
* Collaborative Filtering implementation
* Cosine Similarity for movie recommendations
* Interactive Streamlit web application
* Real-time movie recommendations
* Clean and beginner-friendly project structure

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

# 📂 Dataset

This project uses the MovieLens dataset.

Dataset Source:
https://grouplens.org/datasets/movielens/latest-small/

Files used:

* movies.csv
* ratings.csv

---

# ⚙️ How It Works

1. Load movie and ratings datasets
2. Create a movie-user interaction matrix
3. Compute cosine similarity between movies
4. Select a movie from the interface
5. Recommend similar movies based on user rating patterns

---

# 📁 Project Structure

```bash
movie-recommender/
│
├── app.py
├── recommender.py
├── data/
│   ├── movies.csv
│   └── ratings.csv
├── requirements.txt
└── README.md
```

---

# ▶️ Installation & Setup

## Clone Repository

```bash
git clone <your-github-repo-link>
cd movie-recommender
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Ubuntu/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📸 Application Preview

* Select a movie
* Click on recommend
* Get similar movie recommendations instantly

---

# 📌 Future Improvements

* Add movie posters using TMDB API
* Improve recommendation accuracy
* Add search functionality
* Deploy application online
* Add movie ratings and reviews

---

# 👨‍💻 Author

Ahmad
BS Information Technology Student
MERN Stack & Python Developer
