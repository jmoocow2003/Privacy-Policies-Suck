import bs4
from bs4 import BeautifulSoup
import requests
import re
from summa import summarizer

def parse(url):
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')

    paragraph = str(soup.find_all('p'))
    x = "".join(paragraph)
    for link in soup.find_all('a', attrs={'href': re.compile("^http://")}): #look into attrs
        print (link.get('href'))
    return re.sub('<[^>]+>', '', x)

print(parse(input("Enter a website here: ")))
