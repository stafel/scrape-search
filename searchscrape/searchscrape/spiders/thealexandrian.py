import scrapy


class ThealexandrianSpider(scrapy.Spider):
    name = "thealexandrian"
    allowed_domains = ["thealexandrian.net"]
    start_urls = ["https://thealexandrian.net"]

    def parse(self, response):
        pass
