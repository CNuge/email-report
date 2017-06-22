import urllib
from urllib.request import urlopen, build_opener
from bs4 import BeautifulSoup
import json


def get_XPS_13_price():
	"""check out the price of a dell XPS 13 with the configuration I like"""
	link = 'http://www.dell.com/ca/business/p/xps-13-9360-laptop/pd?oc=xps9360ubvpro1801_5158usca&model_id=xps-13-9360-laptop'
	dell_web = urlopen(link)
	dell_bs = BeautifulSoup(dell_web,'lxml')

	#grabe the product description
	description = dell_bs.find('span', {'class':'pDesc'}).next_sibling
	#grab price from product description
	price_of_comp = description.find('span', {'class':'price'})

	return 'Today the Dell XPS 13 Developer edition you like is $%s.\n\tlink: %s\n' % (price_of_comp.get_text(), link)

def parse_model_name(url_of_page):
	product_split = url_of_page.split('product=')[1]
	model_name = product_split.split('/')[0]
	return model_name

def get_macbook_pro_price(macbook_model_page, model):
	#the following line gets the url while handling the cookies
	mac_data = build_opener(urllib.request.HTTPCookieProcessor).open(macbook_model_page)
	mac_bsObj = BeautifulSoup(mac_data, 'lxml')
	#data is within a json object
	price_of_comp = mac_bsObj.find('script', {'type':'application/ld+json'}).get_text()
	json_dat = json.loads(price_of_comp)
	for i in json_dat['offers']:
		if i['sku'] == model:
			return i['price']

def get_mac_15_price():

	mac_web_15 ='https://www.apple.com/ca_edu_93120/shop/buy-mac/macbook-pro?product=MPTR2LL/A&step=config#'
	price = get_macbook_pro_price(mac_web_15, 'MPTR2LL/A')

	return 'Today the 15 inch Macbook Pro you\'re interested in is $%s.\n\tlink: %s\n' % (price, mac_web_15)

def get_mac_13_price():

	mac_web_13 = 'https://www.apple.com/ca_edu_93120/shop/buy-mac/macbook-pro?product=MPXV2LL/A&step=config#'
	price = get_macbook_pro_price(mac_web_13,'MPXV2LL/A')

	return 'Today the 13 inch Macbook Pro you\'re interested in is $%s.\n\tlink: %s\n' % (price, mac_web_13)

