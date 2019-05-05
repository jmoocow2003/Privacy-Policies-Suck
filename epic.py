import bs4
from bs4 import BeautifulSoup
import requests

def main(url):
	r = requests.get(url)
	c = r.content
	soup = BeautifulSoup(c, 'html.parser')

	paragraph = str(soup.find_all('p'))
	x = "".join(paragraph)
	a = x.replace ("<p>", "").replace ("</p>", "")
	print (a)

main(input())
