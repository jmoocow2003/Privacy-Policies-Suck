import bs4
from bs4 import BeautifulSoup
import requests
import re

def main():
    #setup
    linkDict = {}

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
    for a in links:
        linkDict[re.sub('<[^>]+>', '', str(a))] = str(a.get('href'))

    for g in range(len(paralist)):
        print (paralist[g])
        ft.label(paralist[g].replace("\n", ""))

main()
