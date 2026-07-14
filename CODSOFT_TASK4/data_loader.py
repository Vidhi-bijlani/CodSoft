import pandas as pd

def load_data(ratings_path, movies_path):
    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path)
    
    # Merge them so we have userId + title + genres together
    df = pd.merge(ratings, movies, on='movieId')
    
    # Clean data
    df['title'] = df['title'].str.strip()
    df['genres'] = df['genres'].str.replace('|', ', ')
    return df