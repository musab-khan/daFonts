# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FontprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    font_name = scrapy.Field()
    font_author = scrapy.Field()
    font_image = scrapy.Field()
    font_download = scrapy.Field()
    font_main_category = scrapy.Field()
    font_sub_category = scrapy.Field()
