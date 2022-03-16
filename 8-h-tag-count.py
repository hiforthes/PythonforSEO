from email.mime import image
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.searchenginejournal.com/post-sitemap21.xml'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [myurl.text for myurl in sitemapurls]
count = 0
for websiteurls in xml_urls:
    source = BeautifulSoup(requests.get(websiteurls).text , 'html.parser')
    h1 = len(source.find_all('h1'))
    h2 = len(source.find_all('h2'))
    h3 = len(source.find_all('h3'))
    h4 = len(source.find_all('h4'))
    h5 = len(source.find_all('h5'))
    h6 = len(source.find_all('h6'))
    print(websiteurls)
    print(h1)
    print(h2)
    print(h3)
    print(h4)
    print(h5)
    print(h6)