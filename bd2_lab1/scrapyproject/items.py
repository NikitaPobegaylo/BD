import scrapy


class DataItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    images = scrapy.Field()
    texts = scrapy.Field()


class ProductItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()
