from logic import User
import pytest
import re
from logic.Responses import status_templates

# p_ok = re.compile(r"2\d{2}")
# p_fail = re.compile(r"4\d{2}")


@pytest.mark.parametrize(("user_name", "user_password"), [("Elad", "Elgazar"), ("Adam", "Zaft"), ("Maxim", "Max")])
def test_add_user(delete_all_users_in_db, user_name, user_password):
    response, user_details = User.add_user(user_name, user_password)
    res = re.match(status_templates['p_ok'], str(response.status_code))
    assert bool(res), f'{user_details}'
    # assert bool(p_ok.match(str(response.status_code))), f'{user_details}'
    response, user_details = User.get_user(user_name)
    assert user_details['user_name'] == user_name, f'{user_details}'

# def test_add_user(delete_all_users_in_db):
#     r, message = User.add_user(user_name='Elad', user_password='Elgazar')
#     assert r.status_code == 200, f'{message}'
#
#     r1, message1 = User.get_user(user_name='Elad')
#     assert message1['user_name'] == 'Elad', f'{message1}'


def test_add_user_with_same_username(add_user_to_db):
    r, message = User.add_user(user_name='Elad', user_password='Elad')
    assert bool(p_fail.match(str(r.status_code))), f'{message}'


def test_get_user(add_user_to_db):
    r, message = User.get_user(user_name='Elad')
    assert bool(p_ok.match(str(r.status_code))), f'{message}'
    assert message['user_name'] == 'Elad'


def test_get_user_that_dose_not_exist(add_user_to_db):
    r, message = User.get_user(user_name='Tal')
    assert bool(p_fail.match(str(r.status_code))), f'{message}'


def test_add_friend(add_user_to_db):
    r, message = User.add_friend(friend_name='Adam', user_name='Elad', user_password='Elgazar')
    assert bool(p_ok.match(str(r.status_code))), f'{message}'

    r1, message1 = User.get_user(user_name='Elad')
    assert r1.status_code == 200, f'{message1}'
    assert 'Adam' in message1['friends'], f'{message1}'


def test_add_friend_by_wrong_username(add_user_to_db):
    r, message = User.add_friend(friend_name='Elad', user_name='Tal', user_password='Elad')
    r1, message1 = User.get_user(user_name='Elad')
    assert bool(p_fail.match(str(r.status_code))) or bool(p_fail.match(str(r1.status_code))) or 'Tal' not in message1['friends'], f'{message}'


def test_add_friend_by_wrong_password(add_user_to_db):
    r, message = User.add_friend(friend_name='Adam', user_name='Elad', user_password='Adam')
    assert bool(p_fail.match(str(r.status_code))), f'{message}'

    r1, message1 = User.get_user(user_name='Elad')
    assert 'Adam' not in message1['friends'], f'{message1}'


def test_add_playlists(add_user_to_db):
    r, message = User.add_playlist(playlist_name="I'll be back", user_name='Elad', user_password='Elgazar')
    assert bool(p_ok.match(str(r.status_code))), f'{message}'

    r1, message1 = User.get_user(user_name='Elad')
    assert bool(p_ok.match(str(r1.status_code))), f'{message1}'
    assert "I'll be back" in message1['playlists'], f'{message1}'

    r2, message2 = User.add_playlist(playlist_name="Elad", user_name='Elad', user_password='Elgazar')
    assert bool(p_ok.match(str(r2.status_code))), f'{message2}'

    r1, message1 = User.get_user(user_name='Elad')
    assert bool(p_ok.match(str(r1.status_code))), f'{message1}'
    assert "I'll be back" in message1['playlists'], f'{message1}'

    r, message = User.get_user(user_name='Elad')
    assert bool(p_ok.match(str(r.status_code))), f'{message}'
    assert "Elad" in message1['playlists'], f'{message}'


def test_add_playlists_with_same_name_to_different_users(add_user_to_db):
    r, message = User.add_playlist(playlist_name="I'll be back", user_name='Elad', user_password='Elgazar')
    assert bool(p_ok.match(str(r.status_code))), f'{message}'

    r, message = User.get_user(user_name='Elad')
    assert bool(p_ok.match(str(r.status_code))), f'{message}'
    assert "I'll be back" in message['playlists'], f'{message}'

    r1, message1 = User.add_playlist(playlist_name="I'll be back", user_name='Adam', user_password='Zaft')
    assert bool(p_ok.match(str(r.status_code))), f'{message1}'

    r1, message1 = User.get_user(user_name='Adam')
    assert bool(p_ok.match(str(r1.status_code))), f'{message1}'
    assert "I'll be back" in message1['playlists'], f'{message1}'


def test_add_playlist_with_same_playlistname(add_playlist_to_user):
    r, message = User.add_playlist(playlist_name="I'll be back", user_name='Elad', user_password='Elgazar')
    assert bool(p_fail.match(str(r.status_code))), f'{message}'


def test_add_playlist_by_wrong_password(add_user_to_db):
    r, message = User.add_playlist(playlist_name="I'll be back1", user_name='Elad', user_password='Adam')
    assert bool(p_fail.match(str(r.status_code))), f'{message}'

    r1, message1 = User.get_user(user_name='Elad')
    assert r1.status_code == 200, f'{message1}'
    assert "I'll be back1" not in ['playlists'], f'{message1}'


def test_add_playlist_by_wrong_username(add_user_to_db):
    r, message = User.add_playlist(playlist_name="I'll be back2", user_name='Adam', user_password='Elgazar')
    assert bool(p_fail.match(str(r.status_code))), f'{message}'


def test_get_playlist(add_playlist_to_user):
    r, message = User.get_playlist(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back")
    assert r.status_code == 200, f'{message}'

    r1, message1 = User.get_user(user_name='Elad')
    assert r1.status_code == 200, f'{message1}'
    assert "I'll be back1" not in ['playlists'], f'{message1}'


def test_get_playlist(add_playlist_to_user):
    r, message = User.get_playlist(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back")
    assert r.status_code == 200, f'{message}'


def test_get_playlist_that_dose_not_exist(add_playlist_to_user):
    r, message = User.get_playlist(user_name='Elad', user_password='Elgazar', playlist_name="Hello")
    assert bool(p_fail.match(str(r.status_code))), f'{message}'


def test_get_playlist_by_wrong_password(add_playlist_to_user):
    r, message = User.get_playlist(user_name='Elad', user_password='Adam', playlist_name="I'll be back")
    assert bool(p_fail.match(str(r.status_code))), f'{message}'


def test_get_playlist_by_wrong_username(add_playlist_to_user):
    r, message = User.get_playlist(user_name='Adam', user_password='Elgazar', playlist_name="I'll be back")
    assert bool(p_fail.match(str(r.status_code))), f'{message}'


def test_change_user_password(add_user_to_db):
    r, message = User.add_playlist(playlist_name="I'll be back", user_name='Elad', user_password='Elgazar')
    assert r.status_code == 200, f'{message}'

    r1, message1 = User.get_user(user_name='Elad')
    assert r1.status_code == 200, f'{message1}'
    assert "I'll be back" in message1['playlists'], f'{message1}'

    r, message = User.change_user_password(user_name='Elad', user_password='Elgazar', user_new_password='Adam')
    assert r.status_code == 200, f'{message}'
    User.add_playlist(playlist_name="I'll be back2", user_name='Elad', user_password='Elgazar')
    r, message = User.get_user(user_name='Elad')
    assert "I'll be back2" not in message['playlists'], f'{message}'


def test_change_user_password_by_wrong_username(add_user_to_db):
    r, message = User.change_user_password(user_name='Adam', user_password='Elgazar', user_new_password='Adam')
    assert bool(p_fail.match(str(r.status_code))), f'{message}'


def test_change_user_password_by_wrong_password(add_user_to_db):
    r, message = User.change_user_password(user_name='Elad', user_password='Adam', user_new_password='Adam')
    assert bool(p_fail.match(str(r.status_code))), f'{message}'
