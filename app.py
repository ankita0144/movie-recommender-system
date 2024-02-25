import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x:x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
       recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies = pickle.load(open('movies.pkl', 'rb'))
# movies_list = movies_list['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie recommender system')

selected_movie_name = st.selectbox(
    'Select a movie',
    (movies['title']) )

st.write('You selected:', selected_movie_name)

if st.button("Recommend", type="primary"):
   recommendations = recommend(selected_movie_name)
   for i in recommendations:
      st.write(i)