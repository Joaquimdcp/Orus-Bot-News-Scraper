# -*- coding: utf-8 -*-
import scrapy


class QuotesspiderSpider(scrapy.Spider):
    name = "QuotesSpider"
    allowed_domains = ["QuotesSpider.co"]
    start_urls = (
        'http://www.QuotesSpider.co/',
    )

    def parse(self, response):
        pass
