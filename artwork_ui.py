import artwork_db as artwork_db
from artists_artworks import Artists, Artworks

# Create an error exception
class ArtworkDataError(Exception):
    pass

# Gets the user inputs
def add_artist_user_input():
    
    name = input('Enter the name of the artist: ')
    email = input('Enter the email of the artist: ')
    artwork_db.add_new_artist(name, email)
# gets the user input to seatch for an artwork
def search_artwork_by_the_user():
    try:
        name= input("Enter the name of the artwork's artist: ")
        artwork_db.search_all_artwork(name)
    except:
        print('Error: There is no artwork for this artist')

# gets user input to search for available art work for a specific user
def search_available_artwork_by_the_user():

    try:
        name = input("Enter the name of the artwork's artist: ")
        artwork_db.search_available_artwork(name)
    except:
        print('Error: There is no available artwork for this artist')

# gets user inputs to add new artwork
def add_new_artwork_by_the_user():
    name = input('Enter the name of the artist: ')
    name_artwork = input('Enter the name of the artwork: ')
    price = float(input('Enter the price of the artwork: '))
    available = bool(input('The status of the artwork (available or sold): '))

    if not isinstance(price, (float)) or price < 0:
        print('Error: Please enter valid positive number')
    
    artwork_db.add_new_artwork(name, name_artwork, price, available)

# gets user input to delete an artwork
def delete_artwork_by_the_user():

    try:
        name_artwork = input('Enter the name of artwork that needs to be deleted: ')
        artwork_db.delete_an_artwork(name_artwork)
    except:
        print('Error: The artwork cannot be found')

# gets the user input of the name of the artwork that needs to be change of their availibility status
def update_status_artwork_by_the_user():

    name_artwork = input('Enter the name of artwork to change their availibility: ')
    availibility = input('Enter \'available\' if the artwork is available or \'not available\' if the artwork is not available: ')
        
    if availibility.lower() in ['available', 'not available']:
        print('Artwork availibility status changed!')
        return availibility.lower() == 'available'
    else:
        print('Please enter \'available\' or \'not available\'')
    artwork_db.update_status_artwork(name_artwork, availibility)