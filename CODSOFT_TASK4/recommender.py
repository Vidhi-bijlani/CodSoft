import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def get_recommendations(df, user_id, top_n=5):
    # 1. Create user-movie matrix
    pivot = df.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    
    # 2. If user_id doesn't exist, return top rated
    if user_id not in pivot.index:
        top_movies = df.groupby('movieId').agg({'rating':'mean', 'title':'first', 'genres':'first'}).sort_values('rating', ascending=False).head(top_n)
        return top_movies.reset_index()
    
    # 3. Cosine similarity between users
    similarity = cosine_similarity(pivot)
    sim_df = pd.DataFrame(similarity, index=pivot.index, columns=pivot.index)
    
    # 4. Find 10 most similar users
    similar_users = sim_df[user_id].sort_values(ascending=False)[1:11].index
    
    # 5. Get movies those users liked
    user_movies = df[df['userId'] == user_id]['movieId'].tolist()
    recommendations = df[(df['userId'].isin(similar_users)) & (~df['movieId'].isin(user_movies))]
    
    # 6. Average rating and sort
    recommendations = recommendations.groupby('movieId').agg({
        'rating': 'mean',
        'title': 'first',
        'genres': 'first'
    }).sort_values('rating', ascending=False).head(top_n)
    
    return recommendations.reset_index()


def get_similar_movies(df, movie_title, top_n=5):
    # 1. Get unique movies with genres
    movies_df = df[['movieId', 'title', 'genres']].drop_duplicates('movieId')
    
    # 2. Convert genres to numbers using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['genres'])
    
    # 3. Calculate similarity between all movies
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    # 4. Get index of movie
    indices = pd.Series(movies_df.index, index=movies_df['title']).drop_duplicates()
    
    if movie_title not in indices:
        return []
        
    idx = indices[movie_title]
    
    # 5. Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # 6. Get top 5 most similar movies, excluding itself
    sim_scores = sim_scores[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    
    return movies_df['title'].iloc[movie_indices].tolist()