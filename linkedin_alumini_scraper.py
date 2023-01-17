import os, time 
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import json
driver = webdriver.Chrome('chromedriver')

driver.get("https://www.linkedin.com/login/")


elementID = driver.find_element_by_id('username')
#type your email
elementID.send_keys("")
elementID = driver.find_element_by_id('password')
#type your password
elementID.send_keys("")
elementID.submit()

driver.get('https://www.linkedin.com/school/um5rabat/people/')


#scrool the page
rep = 2 #determine the rep enough to scroll all the page
last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(rep):
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
  time.sleep(5)
  new_height = driver.execute_script("return document.body.scrollHeight")
  if new_height == last_height:
    break
  new_height = last_height

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

uls=soup.find('ul', {'class': 'display-flex list-style-none flex-wrap'})
pr=[]
for li in uls.findAll('li'):
    try:
        r =li.find('a', {'class':'app-aware-link'}).get('href')
        pr.append(r)
    except:
        pass

#number of persons
numP=10
c=0
out = []
for p in pr:
    try:
        driver.get(p)
        time.sleep(2)
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
        dom = etree.HTML(str(soup))
        name = soup.find('h1', {'class' :  'text-heading-xlarge inline t-24 v-align-middle break-words'}).get_text().strip()
        title=soup.find('div', {'class' :  'text-body-medium break-words'}).get_text().strip()
        location=soup.find('span', {'class': 'text-body-small inline t-black--light break-words'}).get_text().strip()
        det= soup.find('span', {'class' :  'pv-text-details__right-panel-item-text hoverable-link-text break-words text-body-small t-black'})
        company=det.find('div').get_text().strip()
        exp=soup.find_all('div', {'class' :  'pvs-list__outer-container'})[1]
        expriences=[i.get_text().strip() for i in exp.find_all('span', {'class' :  'mr1'})]
        person={}
        person["name"]=name
        person["title"]=title
        person["location"]=location
        person["company"]=company
        person["experiences"]=expriences
        out.append(person)
    except:
        continue
    c+=1
    if(c>10):
        break




with open("personUm5.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(out, indent=5, ensure_ascii=False))

driver.close()
driver.quit()

