# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import  Item ,Field




class AldoshoesItem(Item):
    '''creating required field for fetching
    product details in spider'''

    product_url = Field()
    product_id = Field()
    product_name = Field()
    product_brand = Field()
    image_urls = Field()
    mrp = Field()
    price = Field()
    product_sizes = Field()
    category = Field()
    gender  = Field()
    importer_address = Field()
    size_country = Field()
    currency = Field()
#
#
#
#