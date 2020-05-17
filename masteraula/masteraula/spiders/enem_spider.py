# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
import requests

# Disciplinas - Para rodar: trocar o 'cat' pelo id certo.
#   2	Português
#   6	Biologia
#   11	Filosofia
#   10	Física
#   5	Geografía
#   1	História
#   12	Literatura
#   3	Matemática
#   4	Química
#   236	Sociologia
#   9	Espanhol
#   7	Inglês
#   241	Arte

class EnemspiderSpider(scrapy.Spider):
    name = 'enemspider'
    allowed_domains = ['enem.estuda.com']
    start_urls = ['https://enem.estuda.com/questoes/?cat=2&subcat[]=2678&subcat2[]=844&q=&ignorar=1']

    def __init__(self):
        self.page = 1
        self.BASE_URL = 'https://enem.estuda.com/questoes'

    def start_requests(self):
        params = {
            'cat': 12,
            'inicio': self.page,
        }
        # como pegar o total de paginas??
        for i in range(1,2):
            params['inicio']=i
           # url = f'{self.BASE_URL}/?{urllib.parse.urlencode(params)}'
            url = "%s/?%s" % (self.BASE_URL, urllib.parse.urlencode(params))
            request = scrapy.Request(url, callback=self.parse)
            request.meta['params'] = params
            yield request

    def parse(self, response):
        if response.css('.dificuldade0'):
            questoes = response.css('.dificuldade0')
        elif response.css('.dificuldade1'):
            questoes = response.css('.dificuldade1')
        elif response.css('.dificuldade2'):
            questoes = response.css('.dificuldade2')
       # questoes = response.css('[class^="dificuldade"]')

        for questao in questoes:
            id_enem = questao.css('.panel-title-box h3::text').get().strip().split(' ')[-1]
            tags = [x.strip() for x in questao.css('.list-tags li a::text').getall()]
            alternativas = [x.strip() for x in questao.css('.respostas label p').getall()]
            resposta = requests.get('https://enem.estuda.com/questoes/?acao=resposta&id='+id_enem+'&resposta=0&resposta_discursiva=&tempo=23&resolver=&prova=&_=1555438465883', 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'},
                cookies={'usuario': '1989904','usuario_chave':   '67e205bb7042a4200f26c52d224af0f7','usuario_cid': '1'})
            yield { 'object_text':questao.xpath('.//div[@class = "pergunta pergunta_base"]/*').getall(),
                    'object_image':questao.xpath('.//div[@class ="imagem imagem_pre"]').getall(),
                    'statement_p1':questao.xpath('.//div[@class = "pergunta pergunta_pre"]').getall(),
                    'statement_p2':questao.xpath('.//div[@class = "pergunta"]').getall(),
                    'difficulty':questao.css('.dificuldade::attr(title)').get().strip().split(': ')[1],
                    'source':questao.css('.panel-title-box span::text').get().strip(),
                    'tags': tags,
                    'alternatives':alternativas,
                    'id_enem':id_enem
                }