
#* Ejecucion xpath en el shell: scrappy shell 'https://es.pornhub.com/pornstars?performerType=pornstar'
#*                              response.xpath('//*[@id="popularPornstars"]')

#* Ejecucion Spider en el Shell: scrapy runspider Spider.py -o EstrellasAAAAMMDD.json

#* Instalar libreria scrapy: pip install scrapy

import scrapy

from scrapy.spiders import Spider
from scrapy.selector import Selector

class ActrizSpider(Spider):
    name = 'SpiderP'
    start_urls = ['https://es.pornhub.com/pornstars?performerType=pornstar']
    
    def parse(self, response):
        #datos = response.xpath('//div[@id="pornstarsFilterContainer"]/div/h2/text()').extract_first()
        #yield {'Res': datos}
        
        datos = response.xpath('//*[@id="popularPornstars"]') #ok

        for dato in datos:
            titulo = dato.xpath('//div[@id="pornstarsFilterContainer"]/div/h2/text()').extract_first() #ok
            rank = dato.xpath('.//*[@class="rank_number"]/text()').extract() #ok
            nombre = dato.xpath('.//*[@class="pornStarName"]/text()').extract() #ok
            apellido = dato.xpath('.//*[@class="lastName"]/text()').extract() #ok
            info = dato.xpath('.//*[@class="videosNumber"]/text()').extract() #ok
            image_url = dato.xpath('.//img/@data-thumb_url').extract()
            yield { 'Titulo': titulo, 'Rank' : rank, 'Nombre': nombre, 'Apellido' : apellido, 'Info' : info, 'photo': image_url }