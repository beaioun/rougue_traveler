import json
import urllib
import requests
import streamlit as st

def get_image(searchstring):
    google_engine = '16a42554b94ec4cb3'
    encoded_string = urllib.parse.quote_plus(searchstring)
    url = f"https://www.googleapis.com/customsearch/v1?key={st.session_state.google_search_key}&cx={google_engine}&q={searchstring}&searchType=image&imgSize=large&imgType=photo"

    resp = requests.get(url)


    # assuming valid
    x= json.loads(resp.content)
    whichResult = 0
    # use the Kth result    

    return x['items'][whichResult]['link']