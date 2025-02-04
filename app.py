import requests
import streamlit as st 

# api settings

def search_lyric(artist, song):
    endpoint = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(endpoint)
    lyric_result = response.json()["lyrics"] if response.status_code == 200 else ""
    return lyric_result

# website streamlit body

st.image("https://images.pexels.com/photos/1105666/pexels-photo-1105666.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
st.title("Music Lyrics")
artist = st.text_input("Type the artist´s name: ", key="artist")
song = st.text_input("Type the song´s name:  ", key="song")
click_search = st.button("Search")

# when clicking on search button

if click_search:
    lyric_result = search_lyric(artist, song)
    if lyric_result:
        st.success("We found the lyric you are looking for!")
        st.text(lyric_result)
    else:
        st.error("Sorry, we could not find this lyric.")