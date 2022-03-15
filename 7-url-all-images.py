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
    imagesfinder = source.find_all('img')
    imagelist = []
    print(websiteurls)
    for images in imagesfinder:
        try:
            foundedimages = images['src']
        except:
            foundedimages = "We don't have image here"
        images = foundedimages
        imagelist.append(images)
    print(json.dumps(imagelist))