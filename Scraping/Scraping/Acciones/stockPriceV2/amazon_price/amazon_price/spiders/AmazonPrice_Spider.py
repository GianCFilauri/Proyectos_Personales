
#*Link guia: https://www.datasciencecentral.com/how-to-scrape-amazon-product-data/

from pandas import to_datetime
import scrapy


class AmazonpriceSpiderSpider(scrapy.Spider):
    name = 'AmazonPrice_Spider'
    allowed_domains = ['google.com']
    start_urls = ['https://www.google.com/finance/quote/AMZN:NASDAQ',
                'https://www.google.com/finance/quote/BTC-USD',
                'https://www.google.com/finance/quote/DIS:NYSE',
                'https://www.google.com/finance/quote/MELI:NASDAQ',
                'https://www.google.com/finance/quote/GOOG:NASDAQ',
                'https://www.google.com/finance/quote/AAPL:NASDAQ']

    def parse(self, response):
        #Fecha = to_datetime
        Nombre_Empresa = response.xpath('.//*[@class="zzDege"]/text()').extract_first()
        Index = response.xpath('.//*[@class="PdOqHc"]/text()').extract_first()
        price = response.xpath('.//*[@class="YMlKec fxKbKc"]/text()').extract_first()
        #yield { 'Fecha': Fecha, 'Nombre_Empresa': Nombre_Empresa, 'Index' : Index, 'price': price }
        yield {'Nombre_Empresa': Nombre_Empresa, 'Index' : Index, 'price': price }
