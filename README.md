# What is scrape-search

Scrape-search is a simple full text web search engine on top of MongoDB and Python.

Inspiration from [this tutorial on logrocket.com](https://blog.logrocket.com/scrape-website-python-scrapy-mongodb/)

# Setup containers

Create a network

```
podman network create scse
```

Start a MongoDB container with podman

```
podman run -d --name scse-db --network scse -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=specialW0rdNow376 registry.hub.docker.com/library/mongo
```

You need to set up a new user to use the correct database setup in main.py

Create the necessary user and db with the python script from the searchscrape/searchscrape subfolder

```
python3 -c 'from .config import setup_db; setup_db()'
```

Alternative: Connect to the db container and use *mongosh* to create the necessary user and db.

```
mongosh
db.auth("root")
use scse
db.createUser({ user: "scrapeUser", pwd: passwordPrompt(), roles: [ { role: "readWrite", db: "scse" } ]})
```

Then set the same data in the searchscrape/searchscrape/config.py constants