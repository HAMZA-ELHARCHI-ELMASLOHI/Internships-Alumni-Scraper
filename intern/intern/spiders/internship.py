import scrapy
from scrapy.loader import ItemLoader
from ..items import InternItem

class InternshipSpider(scrapy.Spider):
    name = 'internship'
    allowed_domains = ['stagiaires.ma']
    start_urls = ['https://www.stagiaires.ma/offres-stages/']
    nbr_stagiaire=""
    domaine=""
    def parse(self, response):
        ir=response.css('div.feed-activity-list div.offer-container')
        for i in response.css('div.feed-activity-list div.offer-container'):
            il=ItemLoader(item=InternItem(), selector=i)

            il.add_css('name', '.offer-title strong')
            il.add_css("startDate", '.detail-container small')
            il.add_css("periode", ".pull-right span")
            il.add_css("company", "div.actions small")
            il.add_css("location", "div.actions small")

            # go to offer page
            detail_next=ir.css('a::attr(href)').get()
            print(detail_next)
            if(detail_next is not None):
                detail_next=response.urljoin(detail_next)
                yield response.follow(detail_next, callback=self.parse_detail)
            
            il.add_value('nbr_stagiaire', self.nbr_stagiaire)
            il.add_value('domaine', self.domaine)
            nil=il.load_item()
            yield nil
            
        next_page=response.css('ul.pagination li.next a::attr(href)').get()

        if(next_page is not None):
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self,response):
        t=response.xpath('//*[@id="wrapper"]/div/div[2]/div[1]/div/div/div[3]/div/div[1]/div/div/div/div[1]/strong').get()
        print(t)
        self.nbr_stagiaire=t
        self.domaine=response.xpath('//*[@id="wrapper"]/div/div[2]/div[1]/div/div/div[3]/div/div[1]/div/div/div/div[8]/strong').get()
        yield t




 