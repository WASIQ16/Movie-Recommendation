import pandas as pd
import pickle
import streamlit as st
import random

# Load data
with open('model/movies_genres.pkl', 'rb') as f:
    movies = pickle.load(f)

# Flatten all genres
all_genres = sorted({genre for sublist in movies['genres'] for genre in sublist})

# App UI
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

st.markdown(
    """
    <div style="text-align:center">
        <h1 style="color:#ff4b4b;">Movie Recommender System 🎬</h1>
        <p style="font-size:18px;">Select your favorite genre and get movie suggestions!</p>
    </div>
    """, unsafe_allow_html=True)

# User Inputs
genre = st.selectbox("Select a genre:", all_genres)
min_rating = st.slider("Select minimum average rating:", 0.0, 5.0, 3.0, 0.5)

if st.button("Recommend") or st.button("Refresh Recommendations"):
    filtered = movies[movies['genres'].apply(lambda x: genre in x)]
    filtered = filtered[filtered['rating'] >= min_rating]

    if filtered.empty:
        st.warning("No movies found for this genre and rating. Try adjusting the filter!")
    else:
        recommendations = filtered.sample(min(5, len(filtered)))  # 5 random movies

        st.subheader(f"Top Recommendations for {genre} Movies:")
        for i, row in recommendations.iterrows():
            st.markdown(f"**🎬 {row['title']}** - ⭐ {row['rating']:.1f}")

st.markdown(
    """
    <style>
        .stButton>button {
            color: white;
            background-color: #ff4b4b;
            border-radius: 8px;
            padding: 0.5em 1em;
            font-size: 16px;
        }
    </style>
    """, unsafe_allow_html=True)


st.markdown(
    """
    <hr>
    <div style="text-align:center; font-size:14px;">
        Built with ❤️ using Python, Pandas, and Streamlit.
    </div>
    """, unsafe_allow_html=True)
