#crypto.py

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def checkprice(name='bitcoin',start='20200101',end='20200131'):

	url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start={}&end={}'.format(name,start,end)

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = soup(page_html,'html.parser')
	table = data.findAll('tr')

	list_days = []
	list_dict = {}
	for row in table[3:]:
		rw = row.findAll('div')
		days = []
		for i,r in enumerate(rw):
			if i > 0 and i < 5:
				days.append(float(r.text.replace(',','')))
			elif i > 4:
				days.append(int(r.text.replace(',','')))
			else:
				days.append(r.text.replace(',',''))

		list_days.append(days)
		list_dict[days[0]] = days

	return (list_days,list_dict)

if __name__ == '__main__':
	L,D = checkprice('xrp',start='20200105',end='20200131')
	print(D['Jan 31 2020'])