import bs4
from bs4 import BeautifulSoup
import requests
import re

import ft

def main():
    #setup
    linkDict = {}

    r = requests.get(input("Enter a website here: "))
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
