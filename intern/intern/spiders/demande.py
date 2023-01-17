import scrapy
from scrapy.loader import ItemLoader
from ..items import DemandeItem

class DemandeSpider(scrapy.Spider):
    name = 'demande'
    allowed_domains = ['stagiaires.ma']
    start_urls = ['https://www.stagiaires.ma/demandes-stages/']
    sil=""
    count=0
    def parse(self, response):
        ir=response.css('div.feed-activity-list div.demand-container')
        for i in response.css('div.feed-activity-list div.demand-container'):
            il=ItemLoader(item=DemandeItem(), selector=i)

            il.add_css('name', '.demand-title strong')
            il.add_css('formation', '.demand-title small')
            il.add_css("startDate", '.detail-container small')
            il.add_css("periode", ".pull-right span")
            il.add_css("location", "div.actions small")

            nil=il.load_item()
            yield nil
            
        next_page=response.css('ul.pagination li.next a::attr(href)').get()
        
        if(next_page is not None and self.count<50):
            self.count+=1
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
 