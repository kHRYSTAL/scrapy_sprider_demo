#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: BlogSpider.py
@time: 16/6/16 下午10:56
"""
import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader, Identity

from items import Website


class BlogSpider(scrapy.Spider):
    name = "baladuu"
    allowed_domains = ["baladuu.com"]
    start_urls = (
        'http://www.baladuu.com/',
    )

    def parse(self, response):
        sel = Selector(response)
        for link in sel.xpath('//h2/a/@href').extract():
            request = scrapy.Request(link, callback=self.parse_item)
            yield request

        pages = sel.xpath("//div[@class='navigation']/div[@id='wp_page_numbers']/ul/li/a/@href").extract()
        print('pages: %s' % pages)
        if len(pages) > 2:
            page_link = pages[-2]
            page_link = page_link.replace('/a/', '')
            request = scrapy.Request('http://www.meizitu.com/a/%s' % page_link, callback=self.parse)
            yield request

    def parse_item(self, response):
        l = ItemLoader(item=Website(), response=response)
        l.add_xpath('name', '//h2/a/text()')
        l.add_xpath('tags', "//div[@id='maincontent']/div[@class='postmeta  clearfix']/div[@class='metaRight']/p")
        l.add_xpath('image_urls', "//div[@id='picture']/p/img/@src", Identity())

        l.add_value('url', response.url)
        return l.load_item()