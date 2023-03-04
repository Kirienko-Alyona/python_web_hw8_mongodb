from pymongo import MongoClient

from models import Quote, Author
from connect import conn


def search_name(data: str):
    authors = Author.objects(fullname=data)
    
    return res


def search_tag(datas: str):
    res = []
    for data in datas:
        quotes = Quote.objects(tags=data)
        for quote in quotes:
            quote = quote.quote
            if not quote in res:
                res.append(quote)
    print(res)
    return res


if __name__ == '__main__':

    client = MongoClient(conn)
    db = client.mongo_db
    search_tag(("world", "change"))
    search_name(("world", "change"))
    client.close()
