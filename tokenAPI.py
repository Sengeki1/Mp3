from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv() # load the env file in the current folder

client_id = os.getenv("CLIENT_ID") # get value of an env Variable
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content) # reads string from json file and converts into a dictionary
    
    token = json_result["access_token"]
    return token

def refresh_token(url : str, header : dict): # refresh token
    data = {"grant_type": "refresh_token"}
    result = post(url, headers=header, data=data)

    json_result = json.loads(result.content) # string

    if (result.status_code == 200):
        return json_result["refresh_token"]
    else:
        pass

def get_auth_header(token):
    return {"Authorization": "Bearer " + token} # Authorization to seach for artist data