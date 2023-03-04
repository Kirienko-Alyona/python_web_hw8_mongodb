from mongoengine import Document, CASCADE
from mongoengine.fields import ReferenceField, ListField, StringField, ObjectId

class Authors(Document):
    
    # def __init__(self, jsonObj):
    #     self._initialised = True
    #     self._data = jsonObj
    #     self.fullname = jsonObj.get("fullname")
    #     self.born_date = jsonObj.get("born_date")
    #     self.born_location = jsonObj.get("born_location")
    #     self.description = jsonObj.get("description")
        
        
    fullname = StringField(required=True)
    born_date = StringField(required=True, max_lenght=30)
    born_location = StringField(required=True, max_length=150)
    description = StringField(required=True)
    
class Quotes(Document):
    
    # def __init__(self, jsonObj):
    #     self.tags = jsonObj.tags
    #     self.authors = jsonObj.authors
    #     self.quote = jsonObj.quote
        
    tags = ListField(max_length=10)
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField(max_length=250)
    

#new_quote = Quotes(tags=tags, )