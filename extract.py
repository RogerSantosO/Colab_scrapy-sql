import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import logging
from scrapy.crawler import CrawlerRunner


class Cripto(scrapy.Spider):
    name = 'cripto'
    allowed_domains = ['coinmarketcap.com']
    start_urls = [
        'https://coinmarketcap.com/currencies/terra-luna/',
        'https://coinmarketcap.com/currencies/ethereum/',
        'https://coinmarketcap.com/currencies/flow/',
        'https://coinmarketcap.com/currencies/polygon/',
        'https://coinmarketcap.com/currencies/avalanche/',
        'https://coinmarketcap.com/currencies/terra-luna-v2/',
        'https://coinmarketcap.com/currencies/bitcoin/',
        'https://coinmarketcap.com/currencies/solana/',
        'https://coinmarketcap.com/currencies/bnb/',
        'https://coinmarketcap.com/currencies/dogecoin/',
        'https://coinmarketcap.com/currencies/cardano/',
        'https://coinmarketcap.com/currencies/ethereum-classic/',
        'https://coinmarketcap.com/currencies/litecoin/',
        'https://coinmarketcap.com/currencies/ethereum/',
    ]
    #tira mensagens de log do output
    #logging.getLogger('scrapy').propagate = False
    
    def parse(self, response):
        cripto = response.xpath('//span[@class="sc-169cagi-0 kQxZxB"]/text()').get()
        if cripto == None:
            cripto = response.xpath('//span[@class="sc-169cagi-0 kQxZxB small"]/text()').get()
        yield{
            'cripto':cripto,
            'valor':response.xpath('//div[@class="priceValue "]/span/text()').get().replace('$','').replace(',','')
        }
    

def run():
    process = CrawlerProcess(settings= {
            'USER_AGENT' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            "FEEDS": {"cripto.csv": {"format": "csv", "overwrite": True}},
        })
    process.crawl(Cripto)
    process.start()

if __name__ == "__main__":
    run()
