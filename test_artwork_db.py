#Sources Used:  # http://docs.peewee-orm.com/en/latest/peewee/database.html
from unittest import TestCase
from peewee import *
import artwork_db as artwork_db
from artists_artworks import Artists, Artworks
from artwork_ui import ArtworkDataError

test_db_url = SqliteDatabase('artwork_catalog.db')

MODELS = [Artists, Artworks]

class TestArtworkCatalog(TestCase):
    # Create table for testing
    def setUp(self):
        test_db_url.bind(MODELS, bind_refs= False, bind_backrefs= False)
        test_db_url.connect()
        test_db_url.create_tables(MODELS)
    # Removes the tables each time to start fresh
    def tear_down(self):
        test_db_url.drop_tables(MODELS)
        test_db_url.close()
    # Adding the artists data to the database
    def test_add_artists_data(self):
        self.artist1 = Artists('Leonardo Da Vinci', 'leonardo_da_vinci@gmail.com')
        self.artist2 = Artists('Vincent Van Gogh', 'vincent_van_gogh@gmail.com')
        self.artist1.save()
        self.artist2.save()
    
    # Adding the artworks data to the database
    def test_add_artworks_data(self):
        self.artwork1 = Artworks('Leonardo Da Vinci', 'Mona Lisa', 830000000, True)
        self.artwork2 = Artworks('Vincent Van Gogh', 'The Starry Night', 120000000, True)
        self.artwork1.save()
        self.artwork2.save()
    # Test if the user cannot add the same artist info
    def test_add_artist_duplicate_error(self):
        self.artist1 = Artists('Leonardo Da Vinci', 'leonardo_da_vinci@gmail.com')
        self.artist1.save()
        with self.assertRaises(ArtworkDataError):
            self.artist1_duplicate = Artists('Leonardo Da Vinci', 'leonardo_da_vinci@gmail.com')
            self.artist1_duplicate.save()
    # Test if the name of the artist that the user need to see their artwork is in the database
    def test_search_artwork_by_the_user(self):
        self.test_add_artworks_data()
        artist_search = Artists('Leonardo Da Vinci', 'leonardo_da_vinci@gmail.com')
        artwork_db.search_all_artwork(artist_search)
        self.assertIn(artist_search, Artworks)
    # Test if the name of the artist that the user enter is not in the database
    def test_search_artwork_is_not_in_db(self):
        self.test_add_artworks_data()
        artist_search = Artists('Edvard Munch', 'edvard_munch@gmail.com')
        with self.assertRaises(ArtworkDataError):
            artwork_db.search_all_artwork(artist_search)
    # Test if the program display only the available artwork    
    def test_search_available_artwork(self):
        self.test_add_artworks_data()
        artwork_search1 = Artworks('Leonardo Da Vinci', 'Mona lisa', 830000000, True)
        artwork_db.search_available_artwork(artwork_search1)
        artwork_search2 = Artworks('Leonardo Da Vinci', 'Mona lisa', 830000000, False)
        with self.assertRaises(ArtworkDataError):
            artwork_db.search_available_artwork(artwork_search2)
    # Test the artwork is completely deleted from the database
    def test_delete_artwork(self):
        self.test_add_artworks_data()
        artwork_db.delete_an_artwork(self.artwork2)
        self.assertNotIn(self.artwork2, Artworks)
    # Test the deleted artwork is not in database
    def test_delete_artwork_not_in_db(self):
        self.test_add_artworks_data()
        self.artwork3= Artworks('Edvard Munch', 'The Scream', 119900000, True)
        with self.assertRaises(ArtworkDataError):
            artwork_db.delete_an_artwork(self.artwork3)
    
    # Test the status availibility update from the user is saved correctly
    def test_save_update_artwork_availibility_changes(self):
        artwork = Artworks('Leonardo Da Vinci', 'Mona lisa', 830000000, True)
        artwork_db.update_status_artwork(artwork, True)
        artwork.save()
        artwork.available = False
        artwork_db.update_status_artwork(artwork, False)
        artwork.save()
        self.assertEqual(artwork, artwork_db.update_status_artwork(artwork.name, False))
