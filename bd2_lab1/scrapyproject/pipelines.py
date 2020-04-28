from lxml import etree
from .items import DataItem, ProductItem


class DataPipeline(object):
    def __init__(self):
        self.root = etree.Element("data")
        self.count = 0

    def process_item(self, item, spider):
        if isinstance(item, DataItem):
            if self.count < 20:
                page = etree.SubElement(self.root, "page", url=item['url'])

                for image in item['images']:
                    fragment = etree.SubElement(page, "fragment", type="image")
                    fragment.text = image

                for text in item['texts']:
                    fragment = etree.SubElement(page, "fragment", type="text")
                    fragment.text = text

                self.count += 1

            return item

    def close_spider(self, spider):
        doc = etree.ElementTree(self.root)
        doc.write('results/data.xml', xml_declaration=True, encoding='utf-8', pretty_print=True)


class ProductPipeline(object):
    def __init__(self):
        self.root = etree.Element("products")

    def process_item(self, item, spider):
        if isinstance(item, ProductItem):
            product = etree.SubElement(self.root, "product")

            name = etree.SubElement(product, "name")
            name.text = item['name']

            price = etree.SubElement(product, "price")
            price.text = item['price']

            description = etree.SubElement(product, "description")
            description.text = item['description']

            image = etree.SubElement(product, "image")
            image.text = item['image']

            return item

    def close_spider(self, spider):
        doc = etree.ElementTree(self.root)
        doc.write('results/products.xml', xml_declaration=True, encoding='utf-8', pretty_print=True)
