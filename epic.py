import bs4
from bs4 import BeautifulSoup
import requests
import re
from summa import summarizer

def main(url):
	r = requests.get(url)
	c = r.content
	soup = BeautifulSoup(c, 'html.parser')

	paragraph = str(soup.find_all('p'))
	x = "".join(paragraph)
	print (re.sub('<[^>]+>', '', x))
main(input())
