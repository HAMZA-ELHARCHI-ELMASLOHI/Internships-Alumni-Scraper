import scrapy

import re
class RekruteSpider(scrapy.Spider):
    name = 'rekrute'
    allowed_domains = ['rekrute.com']
    start_urls = ['https://www.rekrute.com/offres-emploi-stage.html']
    p=[]
    def parse(self, response):
        for i in response.css('ul.job-list li'):    
            name=self.clean(i.css("a.titreJob::text").get())
            if len(i.css("a.titreJob::text").extract())==0 :
                continue

            company=i.css("img.photo::attr(title)").get()
            l=i.css("div.holder div.info ul li ")
            if len(l.extract())==0 :
                continue
            for j in l:
                self.p.append(self.clean(j.css('a::text').get()))
            
            yield{
                "name":self.clean(i.css("a.titreJob::text").get().split("|")[0]),
                "company":i.css("img.photo::attr(title)").get(),
                "location":self.clean(i.css("a.titreJob::text").get()).split("|")[1],
                "secteur":self.p[0],
                "fonction":self.p[1],
                "experience":self.p[2],
                "niveau":self.p[3],
            }
            self.p=[]
        
        next_page=response.css('div.section a.next::attr(href)').get()

        if(next_page is not None):
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
    def clean(self, text):
        return re.sub(r'\r\n', '',re.sub(' +', ' ', str(text)))
        