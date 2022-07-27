from typing import List
import csv
import requests
from bs4 import BeautifulSoup


# scraping function
def bbc_newsfeed_rss(_categories: List):
    articles_list = []
    for _category in _categories:
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
                    'description': description,
                    'category': _category
                }
                articles_list.append(article)
            
            field_names = articles_list[0].keys()
            save_data(articles_list, field_names)
        except Exception as e:
            print(f'The Scraping job failed for {_category}. See exception: ')
            print(e)

def save_data(article_list, field_names, file_path = 'article.csv'):
    with open(file_path, 'w', newline = '', encoding = 'utf-8') as output_file:
        writer = csv.DictWriter(output_file, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(article_list)

# different document categories for the BBC news RSS feeds
categories = ['business','technology','science_and_environment','entertainment_and_arts','sport']

print('Starting scraping')
bbc_newsfeed_rss(categories)
print('Finished scraping')