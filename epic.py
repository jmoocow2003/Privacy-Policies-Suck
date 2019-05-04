import bs4
from bs4 import BeautifulSoup
import requests

def main(url):
	r = requests.get(url)
	c = r.content
	soup = BeautifulSoup(c, 'html.parser')

	print (soup.prettify)

main(input())