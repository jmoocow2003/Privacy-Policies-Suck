import bs4
from bs4 import BeautifulSoup
import requests
import re
import fastText
from summa import summarizer

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

    contact = []
    collection = []
    use = []
    disclosure = []
    retention = []
    access = []
    cookies = []

    for g in range(len(paralist)):
        print (paralist[g])
        prediction = ft.label(paralist[g].replace("\n", ""))
        print (type(prediction[0][0]))
        print (prediction)
        if prediction[0][0] == "__label__contact":
            contact.append(summarizer.summarize(paralist[g]))
        elif prediction[0][0] == "__label__collection":
            collection.append(summarizer.summarize(paralist[g]))
        elif prediction[0][0] == "__label__use":
            use.append(summarizer.summarize(paralist[g]))
        elif prediction[0][0] == "__label__disclosure":
            disclosure.append(summarizer.summarize(paralist[g]))
        elif prediction[0][0] == "__label__retention":
            retention.append(summarizer.summarize(paralist[g]))
        elif prediction[0][0] == "__label__access":
            access.append(summarizer.summarize(paralist[g]))
        elif prediction[0][0] == "__label__cookies":
            cookies.append(summarizer.summarize(paralist[g]))

    print (contact)
    print (collection)
    print (use)
    print (disclosure)
    print (retention)
    print (access)
    print (cookies)

main()
