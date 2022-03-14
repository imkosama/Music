import streamlit as st
import pickle
import pandas as pd

musics = pickle.load(open("songs1.pkl", "rb"))
similarity=pickle.load(open("similarity.pkl","rb"))

from PIL import Image
img=Image.open("img.jpg")
st.image(img,width=1000,use_column_width=1500,clamp=False,channels="RGB",output_format="auto")

def recommend(music):
    music_index=musics[musics['Songs'] ==music].index[0]
    distance=similarity[music_index]
    music_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_music=[]
    for i in music_list:
        recommended_music.append(musics.iloc[i[0]].Songs)
    return recommended_music


st.title("Music Recommendation")
Selected_music_name = st.selectbox(
        'How would you like to be contacted?',
        musics['Songs'].values)

if st.button('Recommend'):
    recommendations= recommend(Selected_music_name)
    st.subheader("Recommended songs For You")
    for i in recommendations:
        st.write(i)
