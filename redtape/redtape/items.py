# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import  Item,Field


class RedtapeItem(Item):

    name = Field()
    mrp  = Field()
    price = Field()
    colour = Field()
    sizes = Field()
    brand = Field()
    model = Field()
    symbol = Field()

