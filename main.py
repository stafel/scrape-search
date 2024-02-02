import sys
from pymongo import MongoClient

MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_UNAME = "root"
MONGO_PASSWORD = "specialW0rdNow376"
MONGO_DB = "scse"

#client = MongoClient(MONGO_HOST, MONGO_PORT, username=MONGO_UNAME, password=MONGO_PASSWORD)

#db = client.get_database(MONGO_DB)

def _setup_db(root_uname, root_pwd):
    """Creates database and user"""

    client = MongoClient(MONGO_HOST, MONGO_PORT, username=root_uname, password=root_pwd)
    db = client.get_database(MONGO_DB)
    client.add_user(MONGO_UNAME, MONGO_PASSWORD, roles= [ { "role": "readWrite", "db": MONGO_DB } ])

def setup_db():
    """Interactive creates database and user"""

    _setup_db(input("Root username: "), input("Root password: "))

#print(db.posts.insert_one({"author": "me"}).inserted_id)