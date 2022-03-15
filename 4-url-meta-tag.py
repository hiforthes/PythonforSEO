import requests
from bs4 import BeautifulSoup

url = 'https://forthes.com/sitemap.xml'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [myurl.text for myurl in sitemapurls]
for websiteurls in xml_urls:
    source = BeautifulSoup(requests.get(websiteurls).text , 'html.parser')
    x = 0
    try:
        print(source.find("meta", {"name": "description"}).attrs['content'])
        print(source.find("meta", {"name": "keywords"}).attrs['content'])
    except:
        print(websiteurls)
        print(x)