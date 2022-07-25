from logic import Song
from logic import Playlist
from logic import User


def test_add_song(delete_all_song):
    r, message = Song.add_song(song_genre='pop', song_year=1971, song_title="Ain't No Sunshine", song_performer='Bill Withers')
    assert r.status_code == 200, f'{message}'

    r1, message1 = Song.get_song(song_title="Ain't No Sunshine")
    assert message1['genre'] == 'pop', f' expect song_genre="pop" but got {message1["genre"]}'
    assert message1['performer'] == 'Bill Withers', f' expect song_performer="Bill Withers" but got {message1["performer"]}'
    assert message1['rating'] == 0, f' expect song_rating=0 but got {message1["rating"]}'
    assert message1['title'] == "Ain't No Sunshine", f' expect song_title= "Aint No Sunshine" but got {message1["title"]}'
    assert message1['year'] == 1971, f' expect song_year=1971 but got {message1["year"]}'


def test_add_same_song_to_db(add_song_to_db):
    r, message = Song.add_song(song_genre='pop', song_year=1998, song_title="Get up, Stand Up", song_performer='Bob Marley')
    assert r.status_code != 200, f'{message}'


def test_get_song(add_song_to_db):
    r, message = Song.get_song(song_title="Get up, Stand Up")
    assert r.status_code == 200, f'{message}'
    assert message['genre'] == 'pop', f' expect song_genre="pop" but got {message["genre"]}'
    assert message['performer'] == 'Bob Marley', f' expect song_performer="Bob Marley" but got {message["performer"]}'
    assert message['rating'] == 0, f' expect song_rating=0 but got {message["rating"]}'
    assert message['title'] == "Get up, Stand Up", f" expect song_title= Get up, Stand Up but got {message['title']}"
    assert message['year'] == 1998, f' expect song_year= 1998 but got {message["year"]}'


def test_get_song_that_dose_not_exist(add_song_to_db):
    r, message = Song.get_song(song_title="No Woman No Cry")
    assert r.status_code != 200, f'{message}'


def test_add_song_to_playlist(add_playlist_to_user):
    r, message = Playlist.add_song_to_playlist(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Get up, Stand Up")
    assert r.status_code == 200, f'{message}'

    r1, message1 = User.get_playlist(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back")
    assert r1.status_code == 200, f'{message1}'
    assert "Get up, Stand Up" in message1[0]['title'], f" expect song_title= Get up, Stand Up but got {message1[0]}"


def test_add_song_that_dose_not_exist_to_playlist(add_playlist_to_user):
    r, message = Playlist.add_song_to_playlist(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Hello")
    assert r.status_code != 200, f'{message}'


def test_add_song_to_playlist_that_dose_not_exist(add_playlist_to_user):
    r, message = Playlist.add_song_to_playlist(user_name='Elad', user_password='Elgazar', playlist_name="Hello", song_title="Ain't No Sunshine")
    assert r.status_code != 200, f'{message}'


def test_add_song_to_playlist_that_already_exist(add_playlist_to_user):
    r, message = Playlist.add_song_to_playlist(user_name='Elad', user_password='Elgazar', playlist_name="Hello", song_title="Ain't No Sunshine")
    assert r.status_code != 200, f'{message}'


def test_song_upvote(add_song_to_playlist):
    r, message = Song.get_song(song_title="Ain't No Sunshine")
    assert r.status_code == 200, f'{message}'

    r1, message1 = Song.song_upvote(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Ain't No Sunshine")
    assert r1.status_code == 200, f'{message1}'

    assert message['rating'] + 1 == message1['rating'], f" expect song_rating={message['rating'] + 1}  but got { message1['rating']}"


def test_song_upvote_to_same_song_twice(add_song_to_playlist):
    r, message = Song.get_song(song_title="Ain't No Sunshine")
    assert r.status_code == 200, f'{message}'

    r1, message1 = Song.song_upvote(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Ain't No Sunshine")
    assert r1.status_code == 200, f'{message1}'
    r2, message2 = Song.song_upvote(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Ain't No Sunshine")
    assert r.status_code == 200, f'{message2}'
    assert message2['rating'] == message1['rating'] and message1['rating'] == 1 + message['rating'], f" expect song_rating={message1['rating']}  but got { message2['rating']}"


def test_song_downvote(add_song_to_playlist):
    r, message = Song.get_song(song_title="Ain't No Sunshine")
    assert r.status_code == 200, f'{message}'

    r1, message1 = Song.song_downvote(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Ain't No Sunshine")
    assert r1.status_code == 200, f'{message1}'

    assert message['rating'] - 1 == message1['rating'], f" expect song_rating={message['rating'] - 1}  but got { message1['rating']}"


def test_song_downvote_to_same_song_twice(add_song_to_db, add_song_to_playlist):
    r, message = Song.song_upvote(user_name='Adam', user_password='Zaft', playlist_name="I'll be back", song_title="Get up, Stand Up")
    assert r.status_code == 200, f"{message}"
    r, message = Song.song_upvote(user_name='Adam', user_password='Zaft', playlist_name="I'll be back", song_title="Get up, Stand Up")
    assert r.status_code == 200, f"{message}"
    r1, message1 = Song.song_downvote(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Ain't No Sunshine")
    assert r1.status_code == 200, f'{message1}'
    r2, message2 = Song.song_downvote(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Ain't No Sunshine")
    assert r2.status_code == 200, f'{message2}'

    assert message['rating'] == message1['rating'] + 1 == message2['rating'] + 1, f"expect song_rating={message['rating'] -1}, but got {message2['rating']}"


def test_song_downvote_less_than_zero(add_song_to_db, add_song_to_playlist):
    r, message = Song.get_song(song_title="Ain't No Sunshine")
    assert r.status_code == 200, f'{message}'

    r1, message1 = Song.song_downvote(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Ain't No Sunshine")
    assert r1.status_code == 200, f'{message1}'

    assert message['rating'] == message1['rating'], f" expect song_rating={message['rating']}  but got { message1['rating']}"


def test_get_song_by_rank_by_eq(add_song_to_db):
    r, message = Song.get_song_by_rank(rank='0', op='eq')
    assert r.status_code == 200, f'{message}'
    assert "Ain't No Sunshine" in message


def test_get_song_by_rank_by_less(add_song_to_db, add_song_to_playlist):
    r1, message1 = Song.song_upvote(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Get up, Stand Up")
    assert r1.status_code == 200, f'{message1}'

    r, message = Song.get_song_by_rank(rank='1', op='less')
    assert r.status_code == 200, f'{message}'
    assert "Ain't No Sunshine" in message, f" expect song: Ain't No Sunshine. but got {message}"
    assert "Get up, Stand Up" not in message, f" expect song not: Get up, Stand Up. but got {message}"


def test_get_song_by_rank_by_greater(add_song_to_db, add_song_to_playlist):
    r1, message1 = Song.song_upvote(user_name='Elad', user_password='Elgazar', playlist_name="I'll be back", song_title="Get up, Stand Up")
    assert r1.status_code == 200, f'{message1}'

    r, message = Song.get_song_by_rank(rank='0', op='greater')
    assert r.status_code == 200, f'{message}'
    assert "Ain't No Sunshine" not in message, f" expect song not: Ain't No Sunshine. but got {message}"
    assert "Get up, Stand Up" in message, f" expect song: Get up, Stand Up. but got {message}"


def test_get_song_by_rank_less_than_zero(add_song_to_db, add_song_to_playlist):
    r, message = Song.get_song_by_rank(rank='0', op='less')
    assert r.status_code == 200, f'{message}'
    assert not message, f" expect empty list but got : {message['data']}"
