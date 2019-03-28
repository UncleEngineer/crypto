# pip install beautifulsoup4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from datetime import datetime


dt = datetime.now().strftime('%Y%m%d')

def Checkprice(name='bitcoin',sttime='20171201',etime=dt):

	url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start={}&end={}'.format(name,sttime,etime)

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = soup(page_html,'html.parser')

	table = data.findAll('tr',{'class':'text-right'})

	update = []
	open_price = []
	close_price = []

	dictdata = {}

	for row in table:
		column = row.findAll('td')

		update.append(column[0].text)
		open_price.append(float(column[1].text))
		close_price.append(float(column[4].text))

		dictdata[column[0].text] = {'open':float(column[1].text),'close':float(column[4].text)}

	update.reverse()
	open_price.reverse()
	close_price.reverse()

	return dictdata


if __name__ == '__main__':
	bitcoin = Checkprice('bitcoin','20170115')
	print(bitcoin['Jan 01, 2019']['close'])
