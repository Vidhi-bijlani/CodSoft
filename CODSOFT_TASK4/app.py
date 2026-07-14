import streamlit as st
import pandas as pd
from data_loader import load_data
from recommender import get_recommendations, get_similar_movies

st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System - CodSoft Task 4")
st.write("Get movie suggestions based on users OR movie similarity")

# Load data
df = load_data("ratings.csv", "movies.csv")

tab1, tab2 = st.tabs(["👤 By User", "🔍 By Movie"])

with tab1:
    st.subheader("Get recommendations based on similar users")
    user_id = st.selectbox("Select User ID:", sorted(df['userId'].unique()))
    
    if st.button("✨ Get User Recommendations", key="user_btn"):
        with st.spinner("Finding similar users..."):
            recs = get_recommendations(df, user_id, top_n=5)
        
        st.subheader(f"🔥 Top 5 Recommendations for User {user_id}")
        for i, row in recs.iterrows():
            st.success(f"**{i+1}. {row['title']}** \n\n Genre: {row['genres']} \n\n ⭐ Avg Rating: {row['rating']:.2f}")

with tab2:
    st.subheader("Get similar movies to the one you like")
    movie_list = sorted(df['title'].unique())
    selected_movie = st.selectbox("Search Movie:", movie_list)
    
    if st.button("🎭 Find Similar Movies", key="movie_btn"):
        with st.spinner("Analyzing movie..."):
            similar = get_similar_movies(df, selected_movie, top_n=5)
        
        st.subheader(f"Because you liked **{selected_movie}**")
        for i, movie in enumerate(similar, 1):
            st.info(f"**{i}. {movie}**")

st.markdown("---")
st.caption("Built with Collaborative Filtering + Content-Based Filtering")