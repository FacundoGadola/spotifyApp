import youtube_client
import requests
import youtube_dl
import playlist_functions

youtube = youtube_client.get_youtube_client()

all_song_info = {}

def get_liked_videos():
        """Grab Our Liked Videos & Create A Dictionary Of Important Song Information"""
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            myRating="like"
        )
        response = request.execute()

        # collect each video and get important information
        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url = "https://www.youtube.com/watch?v={}".format(
                item["id"])

            # use youtube_dl to collect the song name & artist name
            video = youtube_dl.YoutubeDL({}).extract_info(
                youtube_url, download=False)
            song_name = video["track"]
            artist = video["artist"]

            if song_name is not None and artist is not None:
                # save all important info and skip any missing song and artist
                all_song_info[video_title] = {
                    "youtube_url": youtube_url,
                    "song_name": song_name,
                    "artist": artist,
                    # add the uri, easy to get song to put into playlist
                    "spotify_uri": playlist_functions.search_song(song_name + ' ' + artist)

                }
            print (all_song_info)

        return all_song_info