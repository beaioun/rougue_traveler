import json
import urllib
import requests
import keys # this is a terrible way to do this

def get_image(searchstring):

    encoded_string = urllib.parse.quote_plus(searchstring)
    url = f"https://www.googleapis.com/customsearch/v1?key={keys.google_search_key}&cx={keys.google_engine}&q={searchstring}&searchType=image&imgSize=large&imgType=photo"

    resp = requests.get(url)


    # assuming valid
    x= json.loads(resp.content)
    whichResult = 0
    # use the Kth result    
    return x['items'][whichResult]['link']