from re import U
from typing import List
import requests
from bs4 import BeautifulSoup


# scraping function
def bbc_newsfeed_rss(_categories: List):
    for _category in _categories:
        if _category is 'sport':
            url = f'https://feeds.bbci.co.uk/sport/rss.xml'
        else:
            url = f'http://feeds.bbci.co.uk/news/{_category}/rss.xml'
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, features = 'xml')
            print(soup)
        except Exception as e:
            print(f'The Scraping job failed for {_category}. See exception: ')
            print(e)

# different document categories for the BBC news RSS feeds
categories = ['business','technology','science_and_environment','entertainment_and_arts','sport']

print('Starting scraping')
bbc_newsfeed_rss(categories)
print('Finished scraping')