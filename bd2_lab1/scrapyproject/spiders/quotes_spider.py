import scrapy
from ..items import DataItem


class DataSpider(scrapy.Spider):
    name = "data"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapyproject.pipelines.DataPipeline': 300,
        },
        'CLOSESPIDER_PAGECOUNT': 20
    }

    def start_requests(self):
        urls = [
            'http://www.posolstva.org.ua/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = DataItem()
        item["url"] = response.url
        item["texts"] = response.xpath('//p/text()').getall()
        item["images"] = response.xpath('//img/@src').getall()
        yield item

        for href in response.xpath('//a[contains(@href, "/ru/node") or contains(@href, "/ru/news")]/@href').getall():
            yield response.follow(href, self.parse)
