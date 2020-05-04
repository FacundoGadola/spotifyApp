import spotipy 
import spotipy.util as util
from secrets import username,client_id,client_secret


scope = "user-read-private%20playlist-modify-private%20"
redirect_uri = "http://localhost:8080"

def get_token():    
    token = util.prompt_for_user_token(username,
                           scope,
                           client_id=client_id,
                           client_secret=client_secret,
                           redirect_uri=redirect_uri)
    return token
