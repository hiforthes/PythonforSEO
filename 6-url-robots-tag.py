import requests
from bs4 import BeautifulSoup

url = 'https://forthes.com/sitemap.xml'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [myurl.text for myurl in sitemapurls]
count = 0
for websiteurls in xml_urls:
    source = BeautifulSoup(requests.get(websiteurls).text , 'html.parser')
    x = 0
    try:
        count += 1
        print(websiteurls)
        print(source.find("meta", {"name": "robots"})['content'])
        print(count)
    except:
        print(websiteurls)
        print(x)