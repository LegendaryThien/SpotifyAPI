import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = 'b63fd35bb43542e68f1c49018710a672'
client_secret = '836b25d953ec494d99f053c49829ad71'
redirect_uri = 'http://localhost:8888/callback'

sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope='playlist-read-private')

while True:
    token_info = sp_oauth.get_access_token()

    sp = spotipy.Spotify(auth=token_info['access_token'])

    user_playlists = sp.current_user_playlists()
    playlist_count = len(user_playlists['items'])

    print(f"\nYou have {playlist_count} playlists:")
    for playlist in user_playlists['items']:
        print(f"- {playlist['name']} (ID: {playlist['id']})")

    playlist_id = input("\nEnter the playlist ID (type 'exit' to quit): ")

    if playlist_id.lower() == 'exit':
        break  # Exit the loop if the user enters 'exit'

    try:
        playlist_tracks = sp.playlist_tracks(playlist_id)

        print(f"\nTracks from Playlist (ID: {playlist_id}):")
        for track in playlist_tracks['items']:
            track_id = track['track']['id']
            track_name = track['track']['name']
            artist_name = track['track']['artists'][0]['name']
            print(f"Track: {track_name} - Artist: {artist_name} - ID: {track_id}")

    except spotipy.SpotifyException as e:
        print(f"\nError retrieving playlist: {e}")

    another_playlist = input("\nDo you want to retrieve another playlist? (yes/no): ")
    if another_playlist.lower() != 'yes':
        break
