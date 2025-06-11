import pandas as pd
import pickle
import os

# Create model folder if not exists
os.makedirs('model', exist_ok=True)

# Load data
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')

# Merge average ratings into movies
avg_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()
movies = movies.merge(avg_ratings, on='movieId', how='left')
movies['rating'].fillna(0, inplace=True)

# Extract genres into a list
movies['genres'] = movies['genres'].str.split('|')

# Save preprocessed data
with open('model/movies_genres.pkl', 'wb') as f:
    pickle.dump(movies, f)

print("✅ Genre-based data prepared and saved!")
