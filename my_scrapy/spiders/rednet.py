# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RednetSpider(CrawlSpider):
    name = 'rednet'
    allowed_domains = ['rednet.cn']
    start_urls = ['https://news.rednet.cn/channel/8394.html']

    rules = (
        Rule(LinkExtractor(allow=r'/channel/8394'), follow=True),
        Rule(LinkExtractor(allow=r'/content/2019/12'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print("-"*50)
        data_dic={}
        data_dic['title']=response.xpath('//section[@class="box_left f_left"]/h1[@class="detail_title"]/text()').extract_first()
        data_dic['author']=response.xpath('//section[@class="box_left f_left"]/div[@class="m_b_25"]/span[@class="p_l_10"][2]/text()').extract_first()

        return data_dic
