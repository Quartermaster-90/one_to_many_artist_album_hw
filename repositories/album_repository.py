from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist


def save(album):
    sql = "INSERT INTO users (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def delete_all():
    sql = "DELETE  FROM album"
    run_sql(sql)


def select(id):
    album = None
    sql = "SELECT * FROM album WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        album = Album(result['title'], result['genre'], result['artist'], result['id'])
    return album


def select_all():
    albums = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        album = Album(row['title'], row['genre'], row['artist'], row['id'])
        albums.append(album)
    return albums


def update(album):
    sql = "UPDATE album SET (title, genre, artist) = (%s, %s, %a) WHERE id = %s"
    values = [album.title, album.genre, album.artist, album.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE  FROM album WHERE id = %s"
    values = [id]
    run_sql(sql, values)