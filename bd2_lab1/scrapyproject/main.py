from lxml import etree
from scrapy import cmdline


def find_max_texts_el(xml_filename):
    tree = etree.parse(xml_filename)
    root = tree.getroot()
    pages = root.xpath('/data/page')
    max_texts_el = pages[0]
    for i in range(1, len(pages)):
        if pages[i].xpath('count(fragment[@type="text"])') > max_texts_el.xpath('count(fragment[@type="text"])'):
            max_texts_el = pages[i]
    print(etree.tostring(max_texts_el, method='xml', encoding='utf-8', pretty_print=True))


def process_xsl(xml_filename, xsl_filename, html_filename):
    dom = etree.parse(xml_filename)
    xslt = etree.parse(xsl_filename)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    newdom.write(html_filename, xml_declaration=True, encoding='utf-8', pretty_print=True)


def parse_data():
    cmdline.execute("scrapy crawl data".split())


def parse_products():
    cmdline.execute("scrapy crawl eshop".split())


def gui():
    while True:
        print("1.Crawl data website\n"
              "2.Find page with max amount of text elements\n"
              "3.Crawl eshop\n"
              "4.Process XML to HTML\n"
              "5.Quit\n")
        op = input("Choose option: ")
        if op == '1':
            parse_data()
        elif op == '2':
            find_max_texts_el("results/data.xml")
        elif op == '3':
            parse_products()
        elif op == '4':
            process_xsl("results/products.xml", "xsl/products.xsl", "results/products.html")
        elif op == '5':
            break
        else:
            print("Unsopported operation")


if __name__ == '__main__':
    gui()


