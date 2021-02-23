from peewee import *

db = SqliteDatabase('artwork_catalog.db')

# Create dbModel to specifies database
# Source: http://docs.peewee-orm.com/en/latest/peewee/models.html
class dbModel(Model):
    class Meta:
        database = db

# Create model class for artists info
class Artists(dbModel):

    name = CharField()
    email = CharField()
    
    def __str__(self):
        return f'Artist: {self.name} | Email Address: {self.email}'

# Create model class for artworks info
class Artworks(dbModel):

    # Source for creating foreign key: https://stackoverflow.com/questions/25105188/python-peewee-how-to-create-a-foreign-key
    artist = ForeignKeyField(Artists, to_field= 'name')
    artwork_name = CharField()
    price = FloatField()
    available = BooleanField()

    def __str__(self):
        return f'{self.artist} | Artwork name: {self.artwork_name} | Price: $ {self.price} | Available: {self.available}'