from parsel import Selector

with open('product_list.html') as f:
    response= Selector(text=f.read())

response.get()

#DE CLASE PRODUCTO, QUERO TODOS OS <a>
response.css('.product a::attr(href)').getall()
response.css('ul#offers').getall()


#agora com XPATH
#desde o root, pegar todos os H1
# É indexado em 1
response.xpath('//h1')

#todos os li que dentro tem todos os a y luego todos los href
response.xpath('//li/a/@href')
response.xpath('//li/text()').getall()


# todos los ULS com id offers e todos os li com classe product
#extamente o nombre da clase, por isso se buscar com classes, melhor com .css
response.xpath('//ul[@id="offers"]//li[@class="product"]').getall()

response.xpath('//ul[@id="offers"]//li[contains(@class, "product")]').getall()
