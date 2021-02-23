## This app is a modle of an art store catalog,
#  It gets  artisits and artwork associated with the artist. you can search for each artist artwork and also see if it's available or sold out##
from artists_artworks import Artists, Artworks
import artwork_db as artwork_db
import artwork_ui as artwork_ui

# Main function
def main():
    while True:
        print(' *** Welcome to Artwork Catalog Program ***')
        print('Please choose one of the following options: ')
        print('1. Add a new artist\n2. Search artwork\n3. Search available artwork\n4. Add a new artwork\n5. Delete an artwork\n6. Change the status of an artwork\n7. Exit')
        user_choices = int(input('Your choice?....'))
        artwork_db.create_tables()
        if user_choices == 1:
            artwork_ui.add_artist_user_input()
        elif user_choices == 2:
            artwork_ui.search_artwork_by_the_user()
        elif user_choices == 3:
            artwork_ui.search_available_artwork_by_the_user()
        elif user_choices == 4:
            artwork_ui.add_new_artwork_by_the_user()
        elif user_choices == 5:
            artwork_ui.delete_artwork_by_the_user()
        elif user_choices == 6:
            artwork_ui.update_status_artwork_by_the_user()
        elif user_choices == 7:
            print('Thank you For using the application \nGoodbye!')
            return False
        else:
            print('INVALID INPUT, Please Enter a number between 1 to 7 only')  
            main()  

if __name__ == '__main__':
    main()









