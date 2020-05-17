#Spider básico

class MySpider( scrapy.Spider):
    name = 'spider_name'

    def start_requests(self):
        yield [
            scrapy.Request(
                'http://example.com'
                callback=self.parse #Fila
            )
        ]

    #Scrapy é assincrono
    #yield é um return
    #Quando vc define um request, tem que definir um callback senão por default vai chamar ao "parse"
    #só vai ser executado quando a resposta do request estiver pronta
    #Se o request tem código 303

    #o scrapy nao faz request duplicada, vc pode pegar todos os links e o scrappy filtra os repetidos automaticamente

    #a responsa do request tem que cumprir a estrutura definida
    def parse(self, response):
        self.logger.info('Passei por aqui! ')
