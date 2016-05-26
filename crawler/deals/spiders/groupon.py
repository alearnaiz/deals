# -*- coding: utf-8 -*-
import scrapy
from crawler.deals.items import DealItem


class GrouponSpider(scrapy.Spider):
    name = "groupon"
    allowed_domains = ["groupon.es"]

    def __init__(self, query='spa', location='palma_de_mallorca'):
        queries = query.split(',')
        self.start_urls = []
        for query in queries:
            url = 'https://www.groupon.es/browse/%s?query=%s' % (location, query)
            self.start_urls.append(url)

    def parse(self, response):
        items = []
        deals = response.xpath('//div[@class="cui-content"]')
        for deal in deals:
            item = DealItem()
            item['title'] = deal.xpath('.//p[contains(@class, "cui-deal-title")]/text()').extract_first()
            item['original_price'] = deal.xpath('.//s[@class="cui-price-original"]/text()').extract_first()
            item['original_discount'] = deal.xpath('.//span[contains(@class, "cui-price-discount")]/text()').extract_first()
            item['link'] = response.urljoin(deal.xpath('.//a/@href').extract_first())
            items.append(item)

        return items
