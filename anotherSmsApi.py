import requests
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('number', type=int)
parser.add_argument('message', type=str)

url = "http://textbelt.com/text"
args = parser.parse_args()


def send_sms2(number, message):
	data = {
		"number": number,
		"message": message,
	}

	r = requests.post(url, data=data)

	print(r.status_code)
	print(r.text)

send_sms2(args.number, args.message)