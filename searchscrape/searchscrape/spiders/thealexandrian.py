import scrapy
from ..items import ThealexandrianArticle

class ThealexandrianSpider(scrapy.Spider):
    name = "thealexandrian"
    allowed_domains = ["thealexandrian.net"]
    start_urls = ["https://thealexandrian.net"]

    def parse(self, response):
        articles = response.css("div.item")
        for article in articles:
            article_obj = ThealexandrianArticle(
                _id="djaflkjfkjslkfl",
                title=article.css("div.itemhead").extract_first().strip(),
                content=article.css("div.storycontent").extract_first().strip()
            )

            yield article_obj
