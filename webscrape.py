import requests
from bs4 import BeautifulSoup


def call_Yelp(desc=None, loc=None, nos=11):
	base_url = "https://www.yelp.com/search?find_desc={0}&find_loc={1}".format(desc,loc)
	current_page = 0
	print(base_url)

	while current_page < nos:
		url = base_url + "&start=" + str(current_page)

		yelp_r = requests.get(url)

		try:
			if yelp_r.status_code != 200:
				raise FetchError()

			yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

			# print(yelp_soup.prettify())
			# print(yelp_soup.get_text())
			# print(yelp_soup.findAll('h3', {'class': 'search-result-title'}))
			buziness = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
			# print(buziness)
			for biz in buziness:
				# print(biz.text)
				print(desc,biz.findAll('a', {'class': 'biz-name'})[0].text)
				try:
					address = biz.findAll('address')[0].contents
					for items in address:
						if "br" in str(items):
							print(items.getText(), end='')
						else:
							print("Address: ",items.strip(' \n\t\r'), end=', ')
				except:
					print(None)
				print("Phone: ",biz.findAll('span', {'class': 'biz-phone'})[0].text.strip(' \n\t\r'))
		except FetchError:
			print('Error Fetching Data from url =', url)
		current_page += 10
