import streamlit as st
import pandas as pd
import pickle
import requests
import os

titles=[]
def fetch_poster(title):
    json_data = {'s': str(title)}
    rs = requests.get('http://www.omdbapi.com/?apikey=451b8a0d&', params=json_data)
    response=rs.json()
    # print(response)
    i=0
    if response['Response']=='True':
        i=1
        url = response['Search'][0]['Poster']
        if response['Search'][0]['Title'] in titles:
            url = response['Search'][-1]['Poster']
        if url == 'N/A':
            i=0
            print(url)
        else:
            st.image(url,channels='RGB',caption=title)
    return i

def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_index_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:13]
    recommend_movie_list=[]
    for i in movies_index_list:
        recommend_movie_list.append(df.iloc[i[0]].title)
    return recommend_movie_list

df = pd.read_excel(os.path.join(os.getcwd(),'movies.xlsx'))
similarity = pickle.load(open(os.path.join(os.getcwd(),'similarity.pkl'),'rb'))

st.title('Movie Recommendation System')
selectedMovie = st.selectbox(
    'Which Movie do you like the most?',
     df['title'].values)

if st.button('Recommend'):
    recommend_movie_list = recommend(selectedMovie)
    # col1,col2,col3,col4,col5=st.columns(5)
    for index,i in enumerate(st.columns(5)):
        with i:
            code=fetch_poster(recommend_movie_list[index])
            if code==1:
                pass
            else:
                code = fetch_poster(recommend_movie_list[index+5])
                if code==1:
                    pass
                else:
                    code = fetch_poster(recommend_movie_list[index+6])