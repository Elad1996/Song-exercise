from infra import infrastructure_layer
from logic import Responses


def add_user(user_name, user_password):
    user = {
        "user_name": user_name,
        "user_password": user_password
    }
    r = infrastructure_layer.send_post_message("/users/add_user", user)
    message = Responses.response(r)
    return r, message


def get_user(user_name):
    r = infrastructure_layer.send_get_message("/users/get_user?user_name=" + user_name)
    message = Responses.response(r)
    return r, message


def add_friend(user_name, user_password, friend_name):
    user = {
        "user_name": user_name,
        "user_password": user_password,
        "friend_name": friend_name
    }
    r = infrastructure_layer.send_put_message("/users/add_friend", user)
    message = Responses.response(r)
    return r, message


def add_playlist(playlist_name, user_name, user_password):
    user = {
        "playlist_name": playlist_name,
        "user_name": user_name,
        "user_password": user_password
    }
    r = infrastructure_layer.send_post_message("/users/add_playlist", user)
    message = Responses.response(r)
    return r, message


def get_playlist(user_name, user_password, playlist_name):
    r = infrastructure_layer.send_get_message(
        "/users/get_playlist?user_name=" + user_name + "&user_password=" + user_password + "&playlist_name=" + playlist_name)
    message = Responses.response(r)
    return r, message


def change_user_password(user_name, user_new_password, user_password):
    user = {
        "user_name": user_name,
        "user_new_password": user_new_password,
        "user_password": user_password
    }
    r = infrastructure_layer.send_put_message("/users/change_password", user)
    message = Responses.response(r)
    return r, message
