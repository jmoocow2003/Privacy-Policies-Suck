import bs4
from bs4 import BeautifulSoup
import requests
import re

def main():
    r = requests.get('https://www.example.com')
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    paragraph = soup.find_all('p')
    paralist = []
    for p in paragraph:
        paralist.append(re.sub('<[^>]+>', '', str(p)))
    print(type(paralist[0]))
    print(paralist[0])
    print(paralist[1])

    links = soup.find_all('a')
    linklist = []
    for a in links:
        linklist.append(re.sub('<[^>]+>', '', str(a)))
    print(type(paralist[0]))
    print(paralist[0])
    print(paralist[1])

main()