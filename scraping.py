from typing import List
import requests
from bs4 import BeautifulSoup


# scraping function
def bbc_newsfeed_rss(_categories: List):
    articles_dict = dict.fromkeys(_categories)
    for _category in _categories:
        articles_dict[_category] = []
        if _category is 'sport':
            url = f'https://feeds.bbci.co.uk/sport/rss.xml'
        else:
            url = f'http://feeds.bbci.co.uk/news/{_category}/rss.xml'
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, features = 'xml')
            articles  = soup.findAll('item')
            for a in articles:
                title = a.find('title').text
                link = a.find('link').text
                published = a.find('pubDate').text
                description = a.find('description').text
                article = {
                    'title':title,
                    'link':link,
                    'published': published,
                    'description': description
                }
                articles_dict[_category].append(article)
            
            print(articles_dict)
        except Exception as e:
            print(f'The Scraping job failed for {_category}. See exception: ')
            print(e)

# different document categories for the BBC news RSS feeds
categories = ['business','technology','science_and_environment','entertainment_and_arts','sport']

print('Starting scraping')
bbc_newsfeed_rss(categories)
print('Finished scraping')