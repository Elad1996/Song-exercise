from infra import infrastructure_layer


def delete_all_users():
    r = infrastructure_layer.send_delete_message('/admin/delete_all_users')
    return r


def delete_all_song():
    r = infrastructure_layer.send_delete_message('/admin/delete_all_songs')
    return r


def set_song_into_the_db(song):
    r = infrastructure_layer.send_post_message('/admin/set_songs', song)
    return r


def set_users_into_the_db(user):
    r = infrastructure_layer.send_post_message('/admin/set_users', user)
    return r
