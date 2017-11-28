from requests import get
import bs4
import pandas as pd

from time import sleep
from time import time
from random import randint
from IPython.core.display import clear_output

from warnings import warn

#Gestion aleatoire du temps
# start_time = time()
# requests = 0
#
# url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
#
# response = requests.get(url)
# soup=bs4.BeautifulSoup(response.content, 'html.parser')
# print(response.status_code)

#
# movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')
#
# ###############################
# ########## first movie ########
# ##############################
# first_movie = movie_containers[0]
# #Pour avoir le titre
# first_movie.h3.a.get_text()
# #pour avoir la date
# first_movie.find('span', class_="lister-item-year text-muted unbold").get_text()
# #Pour avoir le rating
# float(first_movie.find('div', class_="inline-block ratings-imdb-rating").strong.get_text())
#  #Pour avoir le metascore
# float(first_movie.find('span', class_="metascore favorable").get_text())
# #Pour avoir les votes
# first_votes = first_movie.find('span', attrs = {'name':'nv'})
# first_votes['data-value']
# #ceux qui ont pas de metascore
# movie_containers[16].find('span', class_="metascore favorable")
# if type(movie_containers[16].find('span', class_="metascore favorable")) is not None:
#     print('lol')


#######################################
########## all  movie in1 page ########
#######################################

# Redeclaring the lists to store data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
headers = {"Accept-Language": "en-US, en;q=0.5"}

# Preparing the monitoring of the loop
start_time = time()
requests = 0
pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2000,2018)]

# For every year in the interval 2000-2017
for year_url in years_url:

    # For every page in the interval 1-4
    for page in pages:

        # Make a get request
        response = get('http://www.imdb.com/search/title?release_date=' + year_url +
        '&sort=num_votes,desc&page=' + page, headers = headers)

        # Pause the loop
        sleep(randint(8,15))

        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
        if requests > 72:
            warn('Number of requests was greater than expected.')
            break

        # Parse the content of the request with BeautifulSoup
        page_html = bs4.BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        # For every movie of these 50
        for container in mv_containers:
            # If the movie has a Metascore, then:
            if container.find('div', class_ = 'ratings-metascore') is not None:

                # Scrape the name
                name = container.h3.a.text
                names.append(name)

                # Scrape the year
                year = container.h3.find('span', class_ = 'lister-item-year').text
                years.append(year)

                # Scrape the IMDB rating
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)

                # Scrape the Metascore
                m_score = container.find('span', class_ = 'metascore').text
                metascores.append(int(m_score))

                # Scrape the number of votes
                vote = container.find('span', attrs = {'name':'nv'})['data-value']
                votes.append(int(vote))



movie_ratings = pd.DataFrame({'movie': names,
                              'year': years,
                              'imdb': imdb_ratings,
                              'metascore': metascores,
                              'votes': votes})
print(movie_ratings.info())
