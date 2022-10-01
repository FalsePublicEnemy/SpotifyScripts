import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPES = {
    'playlist_write': 'playlist-modify-public',
    'tracks_read': 'user-library-read',
}

class Client:
    write = spotipy.Spotify(
        auth_manager=SpotifyOAuth(scope=SCOPES['playlist_write'])
    )
    read = spotipy.Spotify(
        auth_manager=SpotifyOAuth(scope=SCOPES['tracks_read'])
    )
    user_id = spotipy.Spotify(
        auth_manager=SpotifyOAuth()
    ).current_user()['id']
