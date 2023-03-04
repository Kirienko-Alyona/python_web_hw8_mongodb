from mongoengine import Document, CASCADE
from mongoengine.fields import ReferenceField, ListField, StringField, ObjectId


class Author(Document):

    fullname = StringField(required=True)
    born_date = StringField(required=True, max_lenght=30)
    born_location = StringField(required=True, max_length=150)
    description = StringField(required=True)


class Quote(Document):

    tags = ListField(max_length=10, required=True)
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField(max_length=250, required=True)
