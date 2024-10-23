from tokenAPI import *

def search_for_artist(artist_name, token):
    url = "https://api.spotify.com/v1/search"
    query = f"?q={artist_name}&type=artist&limit=1" # query to search for artists
    headers = get_auth_header(token)

    try:
        query_url = url + query
        result = get(query_url, headers=headers)

        json_result = json.loads(result.content)["artists"]["items"]
        if (json_result == 0):
            print("No artist with this name exists...")
            return None
        
        return json_result[0]
    except:
        print("An error occurred")
        

def get_songs_by_artists(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)

    try:
        result = get(url, headers=headers)
        json_result = json.loads(result.content)["tracks"]
    except:
        print("An error occurred")
    return json_result

def get_albuns_by_artists(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = get_auth_header(token)

    try:
        result = get(url, headers=headers)
        json_result = json.loads(result.content)["items"]
    except:
        print("An error occurred")
    return json_result