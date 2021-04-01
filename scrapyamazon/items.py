# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyamazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_title = scrapy.Field()
    product_imagelink = scrapy.Field()
    product_author = scrapy.Field()
    price_hardcover = scrapy.Field()
    price_kindle = scrapy.Field()
    price_audible = scrapy.Field()
    pass

