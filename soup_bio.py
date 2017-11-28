from requests import get
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)
driver=webdriver.Firefox()

url = 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=magasins%20bio&ou=Paris%20%2875%29&idOu=L07505600&page=1&contexte=Gx3GObmd2gPGhZLzdMUmfQxISMRndNFsTX8Pg%2Byl0iE%3D&proximite=0&tri=PERTINENCE-ASC&quoiQuiInterprete=magasins%20bio'
#url='https://www.pagesjaunes.fr'
response=driver.get(url)

soup=BeautifulSoup(response, 'html.parser')

#contenu=soup.find('section', class_="results")
#item=contenu.find('article', class_="bi-bloc blocs clearfix bi-pro")
#vcard=item.header

#Titre de la boutique
#vcard.find(class_="row-denom").h2.a['title']
#re.sub('[\n]','',string_toregex)
