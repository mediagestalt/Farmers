import scrapy
from scrapy.item import Item, Field


class FarmersItem(Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    name = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    location = scrapy.Field()
    website = scrapy.Field()
    markets = scrapy.Field()
    #pass
