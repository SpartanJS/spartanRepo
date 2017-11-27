import requests
import bs4


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)
print('\n')
#print(r.content)
#print(r.text)

soup=bs4.BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print('\n')


#print(list(soup.children))

print('\n'+'Type of soup.children')
print([type (item) for item in list(soup.children)])

#Soup.children : lecture du code en HTML
html=list(soup.children)[2]
print('\n'+'*****************'+'Soup.html')
print(html.prettify())
print('\n'+'Type of soup.html')
print([type (item) for item in list(soup.html)])

#Soup.body : lecture du body
print('\n'+'**************'+'body')
body=list(html.children)[3]
print(body.prettify())

print(list(body.children))
print([type (item) for item in list(body.children)])

print('\n'+'**************'+'contenu de la page')
p=list(body.children)[1]
print(p.prettify())
text=p.get_text()
print(text)
print(ok)
