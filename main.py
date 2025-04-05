import streamlit as st
import pickle
import pandas as pd
import requests #requests module is a popular HTTP library that allows you to send 
                #HTTP requests and handle their responses.
                #an make HTTP requests to interact with web services, APIs, or fetch data from a URL. 
def fetch_poster(movie_id):
    ## Construct the URL for the TMDb API with the provided movie_id
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    #Make a GET request to the TMDb API
    data = requests.get(url)
    #Parse the response as JSON(converting the response received from an HTTP request, typically in the form of a JSON 
    #                      (JavaScript Object Notation) string, into a corresponding Python data structure.)
    data = data.json()
    #Extract the poster path from the API response
    poster_path = data['poster_path']
    #Construct the full URL for the poster image using the poster_path
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
#fetches the poster path for that movie from The Movie Database (TMDb) API. 
#The function then constructs the full URL for the poster image.

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]   #Retrieve the similarity scores from the 'similarity' matrix for the given movie.
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    #list of tuples, where each tuple contains the index and similarity score. 
    #Sort this list in descending order based on the similarity score and select the top 5 

    #completes the recommendation process by iterating through the list of top similar movies and fetching their movie IDs, 
    #titles, and posters using the 'fetch_poster' function.
    #returns two lists: one containing the recommended movie titles and the other containing their corresponding posters.
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

#movies_dict=pickle.load(open('c:\\Users\\NIDHI KAINTURA\\Desktop\\Mini Project\\movie_list.pkl','rb'))

movies_dict=pickle.load(open('c:\\Users\\NIDHI KAINTURA\\Desktop\\Mini Project\\movie_list.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('c:\\Users\\NIDHI KAINTURA\\Desktop\\Mini Project\\similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox('Which type of movie would you like to see?',movies['title'].values)

if st.button('Show Recommendation'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])