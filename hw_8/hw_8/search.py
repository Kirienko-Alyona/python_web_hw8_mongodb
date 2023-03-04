from pymongo import MongoClient

from models import Quote, Author
from connect import conn

res = []


def search_name(data: str) -> str:
    author = Author.objects(fullname=data)
    for item in author:
        author_id = item.id
        list_quote = Quote.objects(author=author_id)
        for quote in list_quote:
            search_quote(quote)
    return None


def search_quote(quote: Quote) -> str:
    global res

    quote = quote.quote

    if not quote in res:
        print(quote)
        res.append(quote)
    return quote


def search_tag(data: str) -> list:
    res = []
    try:
        tags = data.split(",")
    except:
        return "This tag isn't."
    for tag in tags:
        set_quote = Quote.objects(tags=tag)
        for quote in set_quote:
            search_quote(quote)
    return None


if __name__ == '__main__':

    client = MongoClient(conn)
    db = client.mongo_db
    search_tag("life,live")
    # search_tag("life")
    search_name(("Albert Einstein"))
    client.close()
