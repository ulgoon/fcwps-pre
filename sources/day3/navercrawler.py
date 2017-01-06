import urllib.request
from bs4 import BeautifulSoup

query = input("What do you wanna find in naver??")
url = "https://search.naver.com/search.naver?where=post&query=" + query + "&ie=utf8&sm=tab_nmr&nso="
html = urllib.request.urlopen(url)
source = html.read()
html.close()

soup = BeautifulSoup(source, "html.parser")

result = soup.find(id="elThumbnailResultArea")

all_li = result.find_all("li")

for li in all_li:
    dt = li.find("dt")
    title = dt.a.get('title')
    link = dt.a.get('href')
    print(title, link)
