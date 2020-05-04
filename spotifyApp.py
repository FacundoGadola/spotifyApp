import playlist_functions 
import youtube_functions

playlist_name = 'spotify APP'
playlist_description = 'Hello world'

playlist_id = playlist_functions.create_playlist(playlist_name,playlist_description)

all_song_info = youtube_functions.get_liked_videos()

uris = [info["spotify_uri"]
                for song, info in all_song_info.items()]


playlist_functions.add_song_to_playlist(playlist_id,uris)

