# -*- coding: utf-8 -*-
import scrapy

class DefaultQuotesSpider(scrapy.Spider):
    name= 'default_quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls= ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('.quote'):
            yield {
                'citacao': quote.css('span.text::text').get(),
                'autor': quote.css('small.author::text').get(),
                'url': quote.css('span a::attr(href)').get(),
                'tags':quote.css('a.tag *::text').getall()
            }

####
            author_url: response.urljoin(
                quote.css('.author a::attr(href)').get() ),
            )


            yield srapy.Request(
                response.urljoin(
                    response.css(.next a)
                )
            )
