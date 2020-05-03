import requests
import json
from secrets import spotify_token, spotify_user_id


def create_playlist():

    request_body = json.dumps({
        "name": "Youtube Liked Vids",
        "description": "All Liked Youtube Videos",
        "public": False
    })

    query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
    
    response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
    )
    
    response_json = response.json()

        # playlist id
    return response_json["id"]


if __name__ == '__main__':
    playlist_id = create_playlist()