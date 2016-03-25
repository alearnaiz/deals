# -*- coding: utf-8 -*-
import scrapy
from deals.items import DealItem


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
        item = DealItem()
        # main
        main_deal = response.xpath('//div[@id="hero-tile"]')
        item['title'] = main_deal.xpath('.//h2[contains(@class, "hero-tile-title")]/a/text()').extract_first()
        item['original_price'] = main_deal.xpath('.//s[@class="original-price"]/text()').extract_first()
        item['original_discount'] = main_deal.xpath('.//s[@class="discount-price"]/text()').extract_first()
        item['link'] = response.urljoin(main_deal.xpath('.//h2[contains(@class, "hero-tile-title")]/a/@href').extract_first())

        items.append(item)
        # others
        deals = response.xpath('//a[@class="deal-tile-inner"]')
        for deal in deals:
            item = DealItem()
            item['title'] = deal.xpath('.//p[contains(@class, "deal-title")]/text()').extract_first()
            item['original_price'] = deal.xpath('.//s[@class="original-price"]/text()').extract_first()
            item['original_discount'] = deal.xpath('.//s[@class="discount-price"]/text()').extract_first()
            item['link'] = response.urljoin(deal.xpath('@href').extract_first())
            items.append(item)

        return items
