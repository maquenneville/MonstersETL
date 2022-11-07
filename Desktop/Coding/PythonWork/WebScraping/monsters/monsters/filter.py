# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 16:13:41 2022

@author: marca
"""


from scrapy.extensions.feedexport import ItemFilter


class MonsterFilter(ItemFilter):
    def __init__(self, feed_options):
        self.feed_options = feed_options

    def accepts(self, item):
        if "info" in item and item["info"] != None:
            return True
        return False
