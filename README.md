# Internship Scraper

-An internship scraper in morocco using Scrapy from diffrent websites (indeed, stagiaires etc ..)
with a simple data analysis

-Linkedin Alumini Scraper for UM5 University using selenuim and BeautifulSoup

## Setup

```
pip install -r requirements.txt 
```

## Run

#### Spider
```
cd intern

#run spider
scrapy runspider [name of spider]

#example
scrapy runspider indeed -o data.csv
```

#### Selenium + BeautifulSoup

```
python linkedin_alumini_scraper.py
```