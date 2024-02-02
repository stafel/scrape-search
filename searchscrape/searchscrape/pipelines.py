# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .config import get_collection
from .items import ThealexandrianArticle

class SearchscrapePipeline:
    def process_item(self, item, spider):
        return item

class MongoDBPipeline:
    def __init__(self):
        self.collection = get_collection()

    def process_item(self, item, spider):
        if isinstance(item, ThealexandrianArticle):
            self.collection.update_one(filter={"_id": item["_id"]}, update={"$set": dict(item)}, upsert=True)

        return item