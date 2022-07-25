from infra import infrastructure_layer
from logic import Responses


def add_song_to_playlist(user_name, user_password, playlist_name, song_title):
    song = {
        "user_name": user_name,
        "user_password": user_password,
        "playlist_name": playlist_name,
        "song_title": song_title,
    }
    r = infrastructure_layer.send_post_message("/playlists/add_song", song)
    message = Responses.response(r)
    return r, message
