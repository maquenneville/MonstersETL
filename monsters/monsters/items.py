# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MonstersItem(scrapy.Item):
    # define the fields for your item here like:
    info = scrapy.Field()
    name = scrapy.Field()
    size = scrapy.Field()
    Type = scrapy.Field()
    alignment = scrapy.Field()
    HP = scrapy.Field()
    AC = scrapy.Field()
    languages = scrapy.Field()
    chall = scrapy.Field()
    speed = scrapy.Field()
    Str = scrapy.Field()
    Dex = scrapy.Field()
    Con = scrapy.Field()
    Int = scrapy.Field()
    Wis = scrapy.Field()
    Cha = scrapy.Field()
    dvuln = scrapy.Field()
    res = scrapy.Field()
    senses = scrapy.Field()
    dimmun = scrapy.Field()
    cimmun = scrapy.Field()
