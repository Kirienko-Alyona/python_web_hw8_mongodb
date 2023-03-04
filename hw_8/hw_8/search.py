from bson import ObjectId
from pymongo import MongoClient

from models import Quote, Author
from connect import conn


def search_name(data: str) -> str:
    author = Author.objects(fullname=data)
    for item in author:
        author_id = item.id
        search_quote(author_id)
    return 

def search_quote(author_id: ObjectId) -> list:
    res = []
  
    quotes = Quote.objects(author=author_id)      
    for quote in quotes:
        quote = quote.quote
        if not quote in res:
            res.append(quote)
    print(res)
    return res
    
        
def search_tag(data: str) -> list:
    res = []
    try:
        tags = data.split(",")
    except:
        return "This tag isn't."
    for tag in tags:    
        quotes = Quote.objects(tags=tag)      
        for quote in quotes:
            quote = quote.quote
            if not quote in res:
                res.append(quote)
    print(res)
    return res


if __name__ == '__main__':

    client = MongoClient(conn)
    db = client.mongo_db
    #search_tag("life,live")
    #search_tag("life")
    search_name(("Albert Einstein"))
    client.close()
