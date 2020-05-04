import requests
import json
from secrets import username
import spotify_client


spotify_token = spotify_client.get_token()


def create_playlist():
    # Crear una playlist para el usuario de user_id

    request_body = json.dumps({
        "name": "Youtube Liked Vids",
        "description": "All Liked Youtube Videos",
        "public": False
    })

    query = "https://api.spotify.com/v1/users/{}/playlists".format(username)
    
    response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
    )
    
    response_json = response.json()

    return response_json["id"]


def get_user_playlists():
    # Obtener las playlist del usuario dado su user_id

    query = "https://api.spotify.com/v1/users/{}/playlists".format(username)

    header = {
        "Authorization": "Bearer {}".format(spotify_token)
    }

    response = requests.get(query,headers=header)

    return response.json()


def add_song_to_playlist(playlist_id,uris):

    ## Recibe como parametros la id de la playlist y las uris de las canciones
    ## Agrega las canciones a la playlist 

    query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

    header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
    }

    request_body = json.dumps(uris)

    response = requests.post(
            query,
            request_body,
            headers= header
    )

    return response.json()

def search_song(song_name, artist):

    ## Busca la cancion de nombre 'song_name' y artista 'artist'
    ## Retorna la uri de la cancion

    query = "https://api.spotify.com/v1/search?q={}&type=track".format(artist + ' ' + song_name)

    header = {
            "Authorization": "Bearer {}".format(spotify_token)
    }

    response = requests.get(
        query, 
        headers=header
        )

    response_json = response.json()

    songs = response_json["tracks"]["items"]
    
    # Solo usa la primer cancion que encuentra 
    uri = songs[0]['uri']

    return uri 