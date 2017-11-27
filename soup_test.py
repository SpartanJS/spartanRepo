import requests
import bs4
import pandas as pd

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
print(page.status_code)
print('\n')
#print(r.content)
#print(r.text)

soup=bs4.BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

print('\n'+'**********')
seven_day=soup.find(id='seven-day-forecast')
#print(seven_day.prettify())
tombstone_container=seven_day.find_all(class_="tombstone-container")
#print(tombstone_container)
#print(type (tombstone_container))
#print(tombstone_container[0])

period=tombstone_container[0].find(class_="period-name").get_text()
description=tombstone_container[0].find(class_="short-desc").get_text()
temperature=tombstone_container[0].find(class_="temp temp-high").get_text()
img=tombstone_container[0].find("img")
desc=img['title']

period_tag=seven_day.select(".tombstone-container .period-name")
periods=[pt.get_text() for pt in period_tag ]
#print(periods)
short_descs=[sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps=[t.get_text() for t in seven_day.select(".tombstone-container .temp") ]
descs=[d["title"] for d in seven_day.select(".tombstone-container img")]

weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temp": temps,
        "desc":descs
    })
print(weather)
