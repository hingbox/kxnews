# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderNewsGovItem(scrapy.Item):
    gov_name = scrapy.Field()
    type1 = scrapy.Field()
    title = scrapy.Field()
    day = scrapy.Field()
    year = scrapy.Field()
    num = scrapy.Field()
    key_words = scrapy.Field()
    article = scrapy.Field()
    gov_others = scrapy.Field()
    attachments = scrapy.Field()
