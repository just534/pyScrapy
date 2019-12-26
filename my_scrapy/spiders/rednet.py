# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RednetSpider(CrawlSpider):
    name = 'rednet'
    allowed_domains = ['rednet.cn']
    start_urls = ['https://news.rednet.cn/channel/8394.html']

    rules = (
        Rule(LinkExtractor(allow=r'/channel/8394'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
