# -*- coding: utf-8 -*-
import scrapy


class EnemspiderSpider(scrapy.Spider):
    name = 'enemspider'
    allowed_domains = ['enem.estuda.com']
    start_urls = ['https://enem.estuda.com/questoes/?cat=2&subcat[]=2678&subcat2[]=844&q=&ignorar=1']

    def parse(self, response):
        questoes = response.css('.dificuldade0')
        for questao in questoes:
            tags=''
            #tags = [x.get() for x in questao.css('.list-tags li').get_all()]
            respostas = [x.css('p').get() for x in questao.css('.respostas label').get_all()]
            print(respostas)
            yield {#'base':questao.css('.pergunta_base').get(),
                    #'pre':questao.css('.pergunta_pre').get(),
                    #'pergunta':questao.xpath('//div[@class = "pergunta"]').get(),
                    'dificuldade':questao.css('.dificuldade::attr(title)').get(),
                    'prova':questao.css('.panel-title-box span::text').get(),
                    'tags': tags,
                    'respostas':repostas
                    }