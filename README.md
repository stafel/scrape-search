# What is scrape-search

Scrape-search is a simple full text web search engine on top of MongoDB and Python.

Inspiration from [this tutorial on logrocket.com](https://blog.logrocket.com/scrape-website-python-scrapy-mongodb/)

# Setup python environment

In VSCode activate the command pallete, select command "Create environment", set it to use Python 3.10 or higher and use the requirements.txt in the root directory.

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
python3 -c 'from config import setup_db; setup_db()'
```

Alternative: Connect to the db container and use *mongosh* to create the necessary user and db.

```
mongosh
db.auth("root")
use scse
db.createUser({ user: "scrapeUser", pwd: passwordPrompt(), roles: [ { role: "readWrite", db: "scse" } ]})
```

Then set the same data in the searchscrape/searchscrape/config.py constants

# Run scraper to index

In the searchscrape directory run the program with 

```
scrapy crawl thealexandrian
```

# Run query

Work in Progress

The current way to retrieve the data is to logon to *mongosh* and use a text query.

Create a text index first with:

```
db.scrape.createIndex( { content: "text" } )
```

Then start a search with find

```
db.scrape.find( { $text: { $search: "your word here" } } )
```

[See the mongodb manual for further information](https://www.mongodb.com/docs/manual/reference/operator/query/text/)

# Architecture

## Scraping

All the scraping happens in the searchscrape/searchscrape directory:

Individual spiders are located in *spiders* which contain the crawling instructions.

The data is then transformed into items defined in *items.py* .

According to the definition in *settings.py* the data pipelines in *pipelines.py* are called with the items. There the item is transformed into a mongodb entry.

The database settings and helper functions are located in *config.py*.
TODO: Refactor config.py into *settings.py* and a provider class.

## Searching

TODO