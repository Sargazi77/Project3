from artists_artworks import Artists, Artworks
from artwork_ui import ArtworkDataError
from peewee import *

# Setup database
db = SqliteDatabase('artwork_catalog.db')
db.connect()

# Create table 
def create_tables():
    with db:
        db.create_tables([Artists, Artworks]) # Creates 2 tables in the database 1 for artist and 2nd one for artworks
    
# Adds a new artist 
def add_new_artist(name, email):

    add_artist = Artists(name= name, email= email)
    add_artist.save()

    db.close()
    
# Finds all artworks by artist
def search_all_artwork(name):
    
    search_artist = Artworks.select().where(Artworks.artist == name)

    if name:
        for artist in search_artist:
            print(artist)
    else:
        raise ArtworkDataError
     
    db.close()

# Searches all available artworks by artist
def search_available_artwork(name):

    search_available = Artworks.select().where((Artworks.artist == name) |
                                            (Artworks.available == True))

    if name:
        for available_artwork in search_available:
            print (available_artwork)
    else:
        raise ArtworkDataError

    db.close()

# Adds a new artwork
def add_new_artwork(name, name_artwork, price, available):

    add_artwork = Artworks(artist= name, artwork_name= name_artwork, price= price, available=available)
    add_artwork.save()

    db.close()
    
# Deletes an artwork
def delete_an_artwork(name_artwork):

    Artworks.delete().where(Artworks.artwork_name == name_artwork).execute()

    db.close()

# Changes the status of an artwork
def update_status_artwork(name_artwork, availibility):

    Artworks.update(available= availibility).where(Artworks.artwork_name == name_artwork).execute()

    db.close()