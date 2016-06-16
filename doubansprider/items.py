# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspriderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 导演
    movie_director = scrapy.Field()
    # 编剧
    movie_writer = scrapy.Field()
    # 演员
    movie_roles = scrapy.Field()
    # 语言
    movie_language = scrapy.Field()
    # 上映时间
    movie_date = scrapy.Field()
    # 时长
    movie_long = scrapy.Field()
    # 电影描述
    movie_description = scrapy.Field()


class MeizituItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    tags = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()


class Website(scrapy.Item):
    headTitle = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
