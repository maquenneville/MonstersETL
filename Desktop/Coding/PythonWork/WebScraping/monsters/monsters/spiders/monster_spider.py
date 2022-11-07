# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 00:27:33 2022

@author: marca
"""

import scrapy
from monsters.items import MonstersItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import lxml.html


class MonsterSpider(CrawlSpider):
    name = "monster"

    start_urls = ["https://www.dandwiki.com/wiki/5e_Monsters"]

    rules = (Rule(LinkExtractor(allow=("/.+((\de_Creature))\)")), callback="parse"),)

    def parse(self, response):

        monster = MonstersItem()
        monster["info"] = ""
        xml = response.xpath(
            '//*[@id="mw-content-text"]/div/table/tbody/tr/td[1]'
        ).get()

        tree = lxml.html.fromstring(xml)
        monster["info"] = tree.text_content()

        monster["name"] = response.css("span.mw-headline::text").get()
        # =============================================================================
        #         monster['hp'] = response.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr/td[1]/p[2]/text()[2]').get()
        #         monster['ac'] = response.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr/td[1]/p[2]/text()[1]').get()
        #         monster['chall'] = response.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr/td[1]/p[3]/text()[22]').get()
        #
        #
        #
        #         monster['Str'] = response.css('#mw-content-text > div > table:nth-child(3) > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(1)::text').get()
        #         monster['Dex'] = response.css('#mw-content-text > div > table:nth-child(3) > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(2)::text').get()
        #         monster['Con'] = response.css('#mw-content-text > div > table:nth-child(3) > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(3)::text').get()
        #         monster['Int'] = response.css('#mw-content-text > div > table:nth-child(3) > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(4)::text').get()
        #         monster['Wis'] = response.css('#mw-content-text > div > table:nth-child(3) > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(5)::text').get()
        #         monster['Cha'] = response.css('#mw-content-text > div > table:nth-child(3) > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(6)::text').get()
        #         monster['desc'] = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr/td[1]/p[1]/i').get()
        #         monster['dvuln'] = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr/td[1]/p[3]/text()[4]').get()
        #         monster['dres'] = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr/td[1]/p[3]/text()[5]').get()
        #         monster['dimmun'] = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr/td[1]/p[3]/text()[6]').get()
        #         monster['cimmun'] = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr/td[1]/p[3]/text()[7]').get()
        #         monster['speed'] = response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td[1]/p[2]/text()[3]').get()
        # =============================================================================
        yield monster
