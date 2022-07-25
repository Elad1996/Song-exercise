import pytest
from logic import Admin, Song
from logic import User
from logic import Playlist


@pytest.fixture()
def delete_all_users_in_db():
    r = Admin.delete_all_users()


@pytest.fixture()
def add_user_to_db(delete_all_users_in_db):
    User.add_user(user_name='Elad', user_password='Elgazar')
    # User.add_user(user_name='Adam', user_password='Zaft')


@pytest.fixture()
def add_playlist_to_user(add_user_to_db):
    r = User.add_playlist(playlist_name="I'll be back", user_name='Elad', user_password='Elgazar')
    r = User.add_playlist(playlist_name="I'll be back", user_name='Adam', user_password='Zaft')


@pytest.fixture()
def add_song_to_db():
    r = Admin.delete_all_song()
    r = Song.add_song(song_genre='pop', song_year=1971, song_title="Ain't No Sunshine", song_performer='Bill Withers')
    r = Song.add_song(song_genre='pop', song_year=1998, song_title="Get up, Stand Up", song_performer='Bob Marley')


@pytest.fixture()
def delete_all_song():
    r = Admin.delete_all_song()


@pytest.fixture()
def add_song_to_playlist(add_playlist_to_user):
    r = Playlist.add_song_to_playlist(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Ain't No Sunshine")
    r = Playlist.add_song_to_playlist(user_name='Adam', user_password='Zaft', playlist_name="I'll be back", song_title="Ain't No Sunshine")
