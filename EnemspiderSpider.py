# -*- coding: utf-8 -*-
import scrapy
import urllib.parse

class EnemspiderSpider(scrapy.Spider):
    name = 'enemspider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        json_dict = json.loads(response.text)
        has_next= json_dict['has_next']
        page = json_dict['page']
        for quote in json_dict['quotes']:
            yield {
                'quote': quote['text'],
                'autor': quote['author']['name']
            }
        if has_next:
            page+=1
            #temos que fazer um novo request
            yield scrapy.Request('http://quotes.toscrape.com/api/quotes?page='+ str(page))