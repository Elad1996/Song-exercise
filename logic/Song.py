from infra import infrastructure_layer
from logic import Responses


def add_song(song_genre, song_year, song_performer, song_title):
    song = {
        "song_genre": song_genre,
        "song_year": song_year,
        "song_performer": song_performer,
        "song_title": song_title,
    }
    r = infrastructure_layer.send_post_message("/songs/add_song", song)
    message = Responses.response(r)
    return r, message


def get_song(song_title):
    r = infrastructure_layer.send_get_message("/songs/get_song" + '?' + 'song_title=' + song_title)
    message = Responses.response(r)
    return r, message


def song_upvote(user_name, user_password, playlist_name, song_title):
    song = {
        "user_name": user_name,
        "user_password": user_password,
        "playlist_name": playlist_name,
        "song_title": song_title
    }
    r = infrastructure_layer.send_put_message("/songs/upvote", song)
    message = Responses.response(r)
    return r, message


def song_downvote(user_name, user_password, playlist_name, song_title):
    song = {
        "user_name": user_name,
        "user_password": user_password,
        "playlist_name": playlist_name,
        "song_title": song_title
    }
    r = infrastructure_layer.send_put_message("/songs/downvote", song)
    message = Responses.response(r)
    return r, message


def get_song_by_rank(rank, op):
    r = infrastructure_layer.send_get_message("/songs/ranked_songs?rank=" + rank + "&op=" + op)
    message = Responses.response(r)
    return r, message
