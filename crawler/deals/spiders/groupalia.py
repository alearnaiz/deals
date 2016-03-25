# -*- coding: utf-8 -*-
import scrapy
from deals.items import DealItem


class GrouponSpider(scrapy.Spider):
    name = "groupalia"
    allowed_domains = ["groupalia.com"]

    def __init__(self, query='spa', location='mallorca'):
        queries = query.split(',')
        self.start_urls = []
        for query in queries:
            url = 'http://es.groupalia.com/descuentos-%s?q=%s' % (location, query)
            self.start_urls.append(url)

    def parse(self, response):
        items = []

        # deals
        deals = response.xpath('//li[@itemtype="http://schema.org/Product"]')
        for deal in deals:
            item = DealItem()
            item['title'] = deal.xpath('./div[@class="dealTitle"]/a/text()').extract_first()
            item['original_price'] = deal.xpath('./p[@class="price_grp"]/span[@class="original"]/text()')\
                .extract_first()
            item['original_discount'] = deal.xpath('./p[@class="price_grp"]/span[@class="price txt-mb"]/text()')\
                .extract_first()
            item['link'] = response.urljoin(deal.xpath('./a/@href').extract_first())
            items.append(item)

        return items
