import scrapy
from ..items import ThealexandrianArticle


class ThealexandrianSpider(scrapy.Spider):
    name = "thealexandrian"
    allowed_domains = ["thealexandrian.net"]
    start_urls = ["https://thealexandrian.net"]

    def parse(self, response):
        articles = response.css("div.item")
        for article in articles:

            article_link = article.css("div.itemhead").xpath("h3/a").attrib["href"]
            article_id = article_link.split("/")[4]

            article_obj = ThealexandrianArticle(
                _id=article_id,
                title=article.css("div.itemhead").extract_first().strip(),
                content=article.css("div.storycontent").extract_first().strip(),
            )

            yield article_obj
