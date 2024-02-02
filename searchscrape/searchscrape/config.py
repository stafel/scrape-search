import sys
from pymongo import MongoClient

__doc__ = """Contains db settings"""

MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_UNAME = "scse"
MONGO_PASSWORD = "geheim"
MONGO_DB = "scse"
MONOG_COLLECTION = "scrape"

def get_db():
    """Returns mongo db with default settings"""

    client = MongoClient(MONGO_HOST, MONGO_PORT, username=MONGO_UNAME, password=MONGO_PASSWORD)
    return client.get_database(MONGO_DB)

def get_collection():
    """Returns mongo collection for scraper"""

    return get_db()[MONOG_COLLECTION]

def _setup_db(root_uname, root_pwd):
    """Creates database and user"""

    client = MongoClient(MONGO_HOST, MONGO_PORT, username=root_uname, password=root_pwd)
    db = client.get_database(MONGO_DB)

    db.command(
    'createUser', MONGO_UNAME, 
    pwd=MONGO_PASSWORD,
    roles=[{ "role": "readWrite", "db": MONGO_DB }]
)


def setup_db():
    """Interactive creates database and user"""

    _setup_db(input("Root username: "), input("Root password: "))

if __name__ == '__main__':
    setup_db()