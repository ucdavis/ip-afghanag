import urllib2
import requests
from bs4 import BeautifulSoup
import json
import sys

site= sys.argv[1]
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')
#print soup

def main():
	listNames = soup.find_all('a', class_='internal-link')
	linksNotWorking = ""

	for names in listNames:
		if "pdf" in names.get('href'):
			#print names
		  	link = names.get('href')
			print link
		  	name = names.get('href').split("/")[-1]
		  	print name
			try:
				req = urllib2.Request(link, headers={'User-Agent' : "Magic Browser"})
		  		response = urllib2.urlopen(req)
		  		html = response.read()
		  		filename = name
		  		file_ = open(filename, 'w')
		  		file_.write(html)
		  		file_.close()
			except:
				print "not working: " + link
				linksNotWorking += link + "\n"

	print "LINKS NOT WORKING\n"
	print linksNotWorking






if __name__ == '__main__': main()
