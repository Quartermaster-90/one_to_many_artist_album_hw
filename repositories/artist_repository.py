from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository

def save(artist):
    sql = "INSERT INTO tasks (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


def delete_all():
    sql = "DELETE  FROM artist" 
    run_sql(sql)


def select(id):
    artist = None
    sql = "SELECT * FROM artist WHERE id = %s"  
    values = [id] 
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = Artist(result['name'], result['id'])
    return artist


def select_all():  
    artist = [] 

    sql = "SELECT * FROM artist"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artist.append(artist)
    return artist


def update(artist):
    sql = "UPDATE artist SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE  FROM artist WHERE id = %s" 
    values = [id]
    run_sql(sql, values)