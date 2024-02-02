import scrapy


class ThealexandrianSpider(scrapy.Spider):
    name = "thealexandrian"
    allowed_domains = ["thealexandrian.net"]
    start_urls = ["https://thealexandrian.net"]

    def parse(self, response):
        articles = response.css("div.item")
        for article in articles:
            print(article.css("div.itemhead").extract_first().strip())
            print(article.css("div.storycontent").extract_first().strip())
