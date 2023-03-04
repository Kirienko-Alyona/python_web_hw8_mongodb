import json
from pymongo import MongoClient

from models import Author, Quote
from connect import conn

filenames = ["authors", "quotes"]


def create_collection():
    all_id = []
    all_author_fullname = []
    for filename in filenames:
        db[filename]
        path = r"./hw_8/hw_8/" + filename + ".json"

        with open(path, encoding="utf-8") as f:
            text = f.read()
            myList = json.loads(text)
            for jsonObj in myList:
                if filename == "authors":
                    author = Author(fullname=jsonObj['fullname'], born_date=jsonObj["born_date"],
                                     born_location=jsonObj["born_location"], description=jsonObj["description"])
                    author.save()
                    author_id = author.id
                    author_fullname = author.fullname
                    all_id.append(author_id)
                    all_author_fullname.append(author_fullname)
                elif filename == "quotes":
                    for one_id, author_fullname in zip(all_id, all_author_fullname):
                        if author_fullname == jsonObj["author"]:
                            quote = Quote(
                                tags=jsonObj["tags"], author=one_id, quote=jsonObj["quote"])
                            quote.save()
    return


if __name__ == '__main__':

    client = MongoClient(conn)
    db = client.mongo_db
    create_collection()
    client.close()
