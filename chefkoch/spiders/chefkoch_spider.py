# -*- coding: utf-8 -*-
import scrapy


class ChefkochSpiderSpider(scrapy.Spider):
    name = 'chefkoch_spider'
    allowed_domains = ['chefkoch.de']
    start_urls = ['http://chefkoch.de/']

    def parse(self, response):
        pass
