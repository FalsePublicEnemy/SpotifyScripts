from config import *
from utils import Client

from logging import getLogger


logger = getLogger(__name__)

playlist_id = Client.write.user_playlist_create(
    user=Client.user_id,
    name='Liked songs to share',
    public=True,
    collaborative=False,
)['id']

result = {'items': []}

for offset in range(0, total_liked_tracks_amount, 50):
    tracks = Client.read.current_user_saved_tracks(
        limit=50,
        offset=offset,
    )
    ids = [
        track['track']['id']
        for track in tracks['items']
    ]
    Client.write.user_playlist_add_tracks(
        user=Client.user_id,
        playlist_id=playlist_id,
        tracks=ids,
    )
    logger.warn(f'Loading from offset {offset}')
    result['items'].extend(tracks['items'])

for idx, item in enumerate(result['items']):
    track = item['track']
    logger.warn(f'{idx} {track["artists"][0]["name"]} -  {track["name"]}')
