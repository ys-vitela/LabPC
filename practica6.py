from bs4 import BeautifulSoup as bs 
import requests, sys, os, errno, argparse

def scrap():

	description = """ Modo de uso:
		prueba3.py --link "url: """

	parser = argparse.ArgumentParser(description = 
		"Port scannig", epilog = description, 
		formatter_class = argparse.RawDescriptionHelpFormatter)

	parser.add_argument("--link", metavar = "LINK", dest = "link",
		help = "link", required = True)

	params = parser.parse_args()
	xoxo = params.link

	
	try:
		os.system("mkdir images")
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
            
	def make_soup(url):
		
		page = requests.get(url)

		sdata = bs(page.content, "html.parser")
		return sdata

	soup = make_soup(xoxo) 
	for img in soup.findAll("img"):
		temp = img.get("src")
		if temp [:1] == "/":
			image = xoxo + temp
		else:
			image = temp
		print(image)

		r = requests.get(image)
		imagefile = open('images/%s'%image.split('/')[-1], "wb")
		imagefile.write(r.content)
		imagefile.close()	
       
scrap()