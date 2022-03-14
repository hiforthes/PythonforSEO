import requests
from bs4 import BeautifulSoup

url = 'https://forthes.com/sitemap.xml'
soup = BeautifulSoup(requests.get(url).content, 'lxml')
allurls = soup.find_all("loc")
xml_urls = [myurl.text for myurl in allurls]
for websiteurls in xml_urls:
    print(websiteurls)