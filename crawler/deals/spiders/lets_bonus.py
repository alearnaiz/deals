# -*- coding: utf-8 -*-
import scrapy
from deals.items import DealItem


class LetsBonusSpider(scrapy.Spider):
    name = "lets_bonus"
    allowed_domains = ["letsbonus.com"]

    def __init__(self, query='', location='mallorca'):
        queries = query.split(',')
        self.start_urls = []
        for query in queries:
            url = 'http://es.letsbonus.com/s/%s:%s' % (query, location)
            self.start_urls.append(url)

    def parse(self, response):
        items = []

        # deals
        deals = response.xpath('//ul[@class="listSeachContent"]/li/a')
        for deal in deals:
            item = DealItem()
            item['title'] = deal.xpath('./div/h4/text()').extract_first()
            item['original_price'] = None
            item['original_discount'] = deal.xpath('./div/span[@class="price"]/text()').extract_first()
            item['link'] = response.urljoin(deal.xpath('@href').extract_first())
            items.append(item)

        return items
