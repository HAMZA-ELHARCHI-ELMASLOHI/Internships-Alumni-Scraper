import scrapy
from scrapy.loader import ItemLoader

class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    page=0
    allowed_domains = ['ma.indeed.com']
    start_urls = [f"https://ma.indeed.com/emplois?l=Maroc&sc=0kf%3Ajt%28internship%29%3B&vjk="]
    def parse(self, response):
        for i in response.css('ul.jobsearch-ResultsList li'):    
            name=i.css("h2.jobTitle span::text").get()
            company=i.css("span.companyName::text").get()
            location=i.css("div.companyLocation::text").get()
            contrat=i.css("div.attribute_snippet::text").get()
            if name is None:
                continue
            yield {
                "name":name,
                "company":company,
                "location": location,
                "contrat": contrat,
            }
        
        self.page=self.page+10
        next_page=f"https://ma.indeed.com/jobs?q=&l=Maroc&sc=0kf%3Ajt%28internship%29%3B&start={self.page}"
        
        if(self.page<200):
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,  meta={'dont_merge_cookies': True},callback=self.parse)

 