from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#Ne pas oublier de lancer le geckodrive
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)
driver=webdriver.Firefox()


url = 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=magasins%20bio&ou=Paris%20%2875%29&idOu=L07505600&page=1&contexte=Gx3GObmd2gPGhZLzdMUmfQxISMRndNFsTX8Pg%2Byl0iE%3D&proximite=0&tri=PERTINENCE-ASC&quoiQuiInterprete=magasins%20bio'
#url='https://www.pagesjaunes.fr'
response=driver.get(url)

page=driver.page_source
soup=BeautifulSoup(page, 'html.parser')

page_container=soup.find('section', class_="results")
#a renommer pour N
#shop_container=page_container.find('article', class_="bi-bloc blocs clearfix bi-pro")
all_shop_container=page_container.find_all('article', class_="bi-bloc blocs clearfix bi-pro")

######################################
# Pour un article
#######################################
# title=shop_container.find(class_="row-denom").h2.a['title']
# print(title)
# hours=shop_container.find('div',class_="zone-horaire").a.span.get_text().strip()
# print(hours)
# #adress_container=shop_container.find('div', class_="adresse-container noTrad")
# adress=shop_container.find('a', class_="adresse pj-lb pj-link").get_text().strip()
# print(adress)
# desc_gen=shop_container.find('div',class_="description ").a.get_text().strip()
# print(desc_gen)
# prest_title=shop_container.find_all("p",class_='cviv cris')[0].strong.get_text()
# prest=list(shop_container.find_all("p",class_='cviv cris')[0].children)[2].strip()
# print(prest_title)
# print(prest)
# product_title=shop_container.find_all("p",class_='cviv cris')[1].strong.get_text()
# product=list(shop_container.find_all("p",class_='cviv cris')[1].children)[2].strip()
# print(product_title)
# print(product)

######################################
# Pour toute une page
#######################################

#s'occuper du téléphone apres
title_list=[]
hours_list=[]
adress_list=[]
desc_gen_list=[]
prest_title_list=[]
prest_list=[]
product_title_list=[]
product_list=[]


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
    if not shop_container.find_all("p",class_='cviv cris'):
        prest_title=""
        prest=""
        product_title=""
        product=""
    else :
        prest_title=shop_container.find_all("p",class_='cviv cris')[0].strong.get_text()
        prest=list(shop_container.find_all("p",class_='cviv cris')[0].children)[2].strip()
        product_title=shop_container.find_all("p",class_='cviv cris')[1].strong.get_text()
        product=list(shop_container.find_all("p",class_='cviv cris')[1].children)[2].strip()
    prest_title_list.append(prest_title)
    prest_list.append(prest)
    product_title_list.append(product_title)
    product_list.append(product)

print(title_list)
print(hours_list)
print(adress_list)
print(desc_gen_list)
print(prest_title_list)
print(prest_list)
print(product_title_list)
print(product_list)

commerces_bio=pd.DataFrame({'nom':title_list,
                            'heures':hours_list,
                            'adresse':adress_list,
                            'type':desc_gen_list,
                            'prestation':prest_list,
                            'produits':product_list})
# for i in range(0,20):
#     if not all_shop_container[i].find_all("p",class_='cviv cris'):
#         prest_title=""
#     else :
#         prest_title=all_shop_container[i].find_all("p",class_='cviv cris')[0].strong.get_text()
#     print(prest_title)

commerces_bio.to_CSV('commerces_bio.csv', sep=';',float_format=',encoding='utf-16')
