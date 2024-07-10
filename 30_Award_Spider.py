# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:02:38 2022

@author: anilk
"""

import scrapy
import time
import requests

class AwardSpider(scrapy.Spider):
    name="awards"
    start_urls=['https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture']
    
    def parse(self,response):
        '''
        data={}
        data['title']=response.css("title::text").extract()
        yield data
        '''
        for ln in response.css(r"tr[style='background:#FAEB86'] a[href*='film)']::attr('href')").extract():
            url=response.urljoin(ln)
            print(url)
            req=scrapy.Request(url,callback=self.parse_titles)
            time.sleep(5)
            yield req
            
    def parse_titles(self,response):
        for sel in response.css('html').extract():
            data={}
            #data['title']=response.xpath(r"//*[@id='firstHeading']/span").extract()
            data['title']=response.css(r"h1[id='firstHeading'] i::text").extract()
            data['directedby']=response.css(r"tr:contains('Directed by') a[href*='/wiki/']::text").extract()
            #data['starring']=-----
            data['releasedate']=response.css(r"tr:contains('Release dates') li::text").extract()
            yield data
            
            '''
            #If we want to get html node
response.xpath("/html").extract()

#If we want to get body node, which is the child of html node
response.xpath("/html/body").extract()

#If you want to get all div descendant of this html
response.xpath("/html//div").extract()

#we can also drill down without having to start with /html, this expression would extract all div nodes
response.xpath("//div").extract()
         '''
    