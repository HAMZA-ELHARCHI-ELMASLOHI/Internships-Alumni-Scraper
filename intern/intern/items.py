# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import  MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
import re
from datetime import datetime

def location(text :str):
    l=text.split("-")[1]
    return l

def company(text :str):
    l=text.split("-")[0]
    return l
def name(text :str):
    l=text.split("(")[0]
    return l

def periode(values):
    for value in values:
            if  value != '' and value[0].isdigit():
                return value
def demande_location(text :str):
    return re.sub(r'habite à', '', text).split("-")[1]

class InternItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags, name),
                        output_processor=TakeFirst())

    startDate=scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())

    periode=scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=periode)

    location=scrapy.Field(input_processor=MapCompose(remove_tags, location),
                        output_processor=TakeFirst())

    company=scrapy.Field(input_processor=MapCompose(remove_tags, company) ,
                        output_processor=TakeFirst())

    nbr_stagiaire=scrapy.Field(input_processor=MapCompose(remove_tags) ,
                        output_processor=TakeFirst())

    domaine=scrapy.Field(input_processor=MapCompose(remove_tags) ,
                        output_processor=TakeFirst())


class DemandeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags, name),
                        output_processor=TakeFirst())

    formation=scrapy.Field(input_processor=MapCompose(remove_tags, company) ,
                        output_processor=TakeFirst())

    location=scrapy.Field(input_processor=MapCompose(remove_tags, demande_location),
                        output_processor=TakeFirst())                    
    startDate=scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())

    periode=scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=periode)

    

"""

class RekruteItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags, name),
                        output_processor=TakeFirst())

    company=scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())

    secteur=scrapy.Field(input_processor=MapCompose(remove_tags), 
                        output_processor=TakeFirst())

    fonction=scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())

    experience=scrapy.Field(input_processor=MapCompose(remove_tags) ,
                        output_processor=TakeFirst())
    experience=scrapy.Field(input_processor=MapCompose(remove_tags) ,
                        output_processor=TakeFirst())


class OptionItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())

    
    location=scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())

    company=scrapy.Field(input_processor=MapCompose(remove_tags) ,
                        output_processor=TakeFirst())
"""