import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

artist_1 = Artist("Elton John")
artist_repository.save(artist_1)
artist_2 = Artist("Paul McCartney")
artist_repository.save(artist_2)
artist_3 = Artist("Paul McCartney")
artist_repository.save(artist_3)


album_1 = Album("Goodbye Yellow Brick Road", "Pop Rock", artist_1)
album_repository.save(album_1)
album_2 = Album("Flaming Pie", "Rock", artist_2)
album_repository.save(album_2)

user_repository.select_all()


pdb.set_trace()
