#requests, urlopen, beautifulsoup
from bs4 import BeautifulSoup
from urllib2 import urlopen

response = urlopen('https://www.naver.com/')
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("new.txt", 'w')
for anchor in soup.find_all('span.ah_k'):
    data = str(i) + "위 : " + anchor.get_text() + "\n"
    i = i + 1
    f.write(data)
f.close()