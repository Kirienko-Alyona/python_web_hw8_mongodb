from pymongo import MongoClient
from termcolor import colored
from decor import input_error

from models import Quotes, Authors
from connect import conn


@input_error
def return_quote(list_quote: Quotes) -> str:
    res_quotes = []
    for quote in list_quote:
        quote = quote.quote
        res_quotes.append(quote)
    return res_quotes


@input_error
def search_name(name: str) -> str:
    authors = Authors.objects(fullname=name)
    list_quote = Quotes.objects(author=authors[0].id)
    return return_quote(list_quote)


@input_error
def search_tag(data: str) -> list:
    try:
        tags = data.split(",")
    except ValueError:
        return colored("This tag isn't.", "red")
    list_quote = Quotes.objects(tags__in=tags)
    return return_quote(list_quote)


if __name__ == '__main__':

    client = MongoClient(conn)
    db = client.mongo_db
    client.close()
