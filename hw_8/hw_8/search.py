from pymongo import MongoClient

from models import Quotes, Authors
from connect import conn


def search_name(name: str) -> str:
    authors = Authors.objects(fullname=name)
    list_quote = Quotes.objects(author=authors[0].id)
    first_item = list_quote[0]
    return list_quote


def print_quote(quote: Quotes) -> str:
    global res

    quote = quote.quote

    #if not quote in res:
    print(quote)
    #res.append(quote)
    return quote


def search_tag(data: str) -> list:
    try:
        tags = data.split(",")
    except:
        return "This tag isn't."
    list_quote = Quotes.objects(tags__in=tags)

    return list_quote


if __name__ == '__main__':

    client = MongoClient(conn)
    db = client.mongo_db
    list_quotes = search_tag("life,humor")
    #list_quotes = search_tag("humor")
    #list_quotes = search_name(("Albert Einstein"))
    for quote in list_quotes:
        print_quote(quote)
    client.close()
