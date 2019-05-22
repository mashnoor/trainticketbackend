from peewee import *
class User(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db