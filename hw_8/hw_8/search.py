from pymongo import MongoClient
from termcolor import colored
from decor import input_error

from models import Quotes, Authors
from connect import conn


@input_error
def return_quote(quote: Quotes) -> str:
    quote = quote.quote
    return quote


@input_error
def search_name(name: str) -> str:
    try:
        name.find(" ")
    except AttributeError:
        return colored("Wrong format. Please enter: '{command:}{author's name separated by a space and capitalized}'", "red")
    authors = Authors.objects(fullname=name)
    list_quote = Quotes.objects(author=authors[0].id)
    return return_quote(list_quote)


@input_error
def search_tag(data: list) -> list:
    for item in data:
        if (item.islower() == False) or (item.split(" ") == True):
            raise KeyError(colored("Wrong format. Please enter: '{command:}{tag,tag}' without spaces and in lower case.", "red"))
    list_quote = Quotes.objects(tags__in=data)
    if len(list_quote) != 0:
        return list_quote
    else:
        raise IndexError


if __name__ == '__main__':

    client = MongoClient(conn)
    db = client.mongo_db
    client.close()
