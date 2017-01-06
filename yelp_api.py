import requests
from requests_oauthlib import OAuth1


consumer_key = "Consumer Key"
consumer_secret = "Consumer Secret"
token = "Token"
token_secret = "Token Secret Key"


def yelp_search(term="Food", location="San Fransisco", limit=10):
	url = "https://api.yelp.com/v2/search"
	params = {
		"term": term,
		"location": location,
		"limit": limit,
	}
	auth = OAuth1(consumer_key,consumer_secret, token, token_secret)
	r = requests.get(url, auth=auth, params=params)
	if r.status_code == 200:
		print("Successfull...")
		return r.json()
	return None



search1 = yelp_search()
i = 1
for search1 in data["businesses"]:
	print(i, biz["name"])
	print(", ".join(biz["location"]["display_address"]))
	print(biz["display_phone"])
	print("Rating: ", biz.get("rating"))
	print()
	i += 1


search2 = yelp_search(term="restaurants", location="fremont, CA", limit=30)
i = 1
for search1 in data["businesses"]:
	print(i, biz["name"])
	print(", ".join(biz["location"]["display_address"]))
	print(biz["display_phone"])
	print("Rating: ", biz.get("rating"))
	print()
	i += 1
