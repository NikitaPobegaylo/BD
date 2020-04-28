import scrapy
from ..items import ProductItem


class EshopSpider(scrapy.Spider):
    name = "eshop"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapyproject.pipelines.ProductPipeline': 300,
        },
        'CLOSESPIDER_PAGECOUNT': 20
    }

    def start_requests(self):
        urls = [
            'https://www.bookclub.ua/catalog/books/psychology'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = response.xpath('//section[@class="mproddopinfo"]').get(0)
        if item is not 0:
            product = ProductItem()
            product['name'] = str(response.xpath('//article[@class="prd-m-info-block"]/header/h1/text()')
                                  .get(0)).strip()
            product['image'] = 'https://www.bookclub.ua' + str(response.xpath('//img[@class="imgprod"]/@src')
                                                               .get(0)).strip()
            product['price'] = str(response.xpath('//div[@class="prd-enov-pr-numb"]/text()').get(0)).strip()
            product['description'] = str("".join(response.xpath('//div[@class="proddesc"]/text()').getall())).strip()
            yield product

        for href in response.xpath('//div[@class="book-inlist-img"]/a/@href').getall():
            yield response.follow(href, self.parse)
