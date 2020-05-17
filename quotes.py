# Queremos obter todas as informações disponíveis sobre as citações nessa página:
# - citação, nome do autor, URL para detalhes do autor e lista de tags da citação

scrapy startproject quotes
cd quotes

citação
print(quote.css('span.text').get())

nome do author
print(quote.css('small.author::text').get())

url para detalhes do DefaultQuotesSpider
print(quote.css('span a::attr(href)').get())

lista de tags
print(quote.css('meta.keywords').get())
