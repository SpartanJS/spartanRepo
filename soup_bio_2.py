from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from time import sleep
from time import time
from random import randint
from IPython.core.display import clear_output

from warnings import warn

#Ne pas oublier de lancer le geckodrive
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)
driver=webdriver.Firefox()

# Preparing the monitoring of the loop
start_time = time()
requests = 0
pages = [str(i) for i in range(1,14)]

title_list=[]
hours_list=[]
adress_list=[]
desc_gen_list=[]
prest_title_list=[]
prest_list=[]
product_title_list=[]
product_list=[]


for page in pages:

    url = 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=magasins%20bio&ou=Paris%20%2875%29&idOu=L07505600&page='+page+'&contexte=Gx3GObmd2gPGhZLzdMUmfQxISMRndNFsTX8Pg%2Byl0iE%3D&proximite=0&tri=PERTINENCE-ASC&quoiQuiInterprete=magasins%20bio'
    #url='https://www.pagesjaunes.fr'
    response_1=driver.get(url)

    #c'est ma request
    response=driver.page_source

    # Pause the loop
    sleep(randint(5,15))

    # Monitor the requests
    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)

    # # Throw a warning for non-200 status codes
    # if response.status_code != 200:
    #     warn('Request: {}; Status code: {}'.format(requests, response.status_code))

    # Break the loop if the number of requests is greater than expected
    if requests > 20:
        warn('Number of requests was greater than expected.')
        break

    soup=BeautifulSoup(response, 'html.parser')
    page_container=soup.find('section', class_="results")
    #a renommer pour N
    #shop_container=page_container.find('article', class_="bi-bloc blocs clearfix bi-pro")
    all_shop_container=page_container.find_all('article', class_="bi-bloc blocs clearfix bi-pro")

    for shop_container in all_shop_container:
        title=shop_container.find(class_="row-denom").h2.a['title']
        title_list.append(title)
        if not shop_container.find('div',class_="zone-horaire"):
            hours=""
        else :
            hours=shop_container.find('div',class_="zone-horaire").a.span.get_text().strip()
        hours_list.append(hours)
        #adress_container=shop_container.find('div', class_="adresse-container noTrad")
        adress=shop_container.find('a', class_="adresse pj-lb pj-link").get_text().strip()
        adress_list.append(adress)
        desc_gen=shop_container.find('div',class_="description ").a.get_text().strip()
        desc_gen_list.append(desc_gen)
        #if the list is empty
        # if not shop_container.find_all("p",class_='cviv cris'):
        #     #prest_title=""
        #     prest=""
        #     #product_title=""
        #     product=""
        # else :
        #     #prest_title=shop_container.find_all("p",class_='cviv cris')[0].strong.get_text()
        #     prest=list(shop_container.find_all("p",class_='cviv cris')[0].children)[2].strip()
        #     #product_title=shop_container.find_all("p",class_='cviv cris')[1].strong.get_text()
        #     if len(shop_container.find_all("p",class_='cviv cris')==1):
        #         product=list(shop_container.find_all("p",class_='cviv cris')[0].children)[2].strip()
        #     else :
        #         product=list(shop_container.find_all("p",class_='cviv cris')[1].children)[2].strip()
        # #prest_title_list.append(prest_title)
        # prest_list.append(prest)
        # #product_title_list.append(product_title)
        # product_list.append(product)

# commerces_bio=pd.DataFrame({'nom':title_list,
#                             'heures':hours_list,
#                             'adresse':adress_list,
#                             'type':desc_gen_list,
#                             'prestation':prest_list,
#                             'produits':product_list})

commerces_bio=pd.DataFrame({'nom':title_list,
                            'heures':hours_list,
                            'adresse':adress_list,
                            'type':desc_gen_list})
print(commerces_bio.info())
