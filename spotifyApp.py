import playlist_functions 


artist = 'joao jilberto'
song = ''

playlist_id = playlist_functions.create_playlist()

song_uri = playlist_functions.search_song(song,artist)

uri = [song_uri]

playlist_functions.add_song_to_playlist(playlist_id,uri)

