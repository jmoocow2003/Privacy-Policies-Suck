import fastText
import bs4
import requests
from bs4 import BeautifulSoup
import re
from summa import summarizer

def parse(url):
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')

    paragraph = str(soup.find_all('p'))
    #x = "".join(paragraph)
    for link in soup.find_all('a', attrs={'href': re.compile("^http://")}):
        print (link.get('href'))
    newlist = re.sub('<[^>]+>', '', paragraph)
    return newlist[0]

def main():
    model = fastText.train_supervised('..\Data\Gerard.txt')
    print(parse("https://www.example.com"))
    print(model.predict(parse("https://www.example.com")))

main()