import requests
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('number', type=int)
parser.add_argument('text_msg', type=str)
parser.add_argument('--media',)

username = 'Account SID'  # acc_sid
password = 'Authentication Token Key'   # auth_token

base_url = 'https://api.twilio.com/2010-04-01/Accounts/'

twilio_number = '+15104586271'   # 510 458 1194


def xml_pritify(xml_str):
	import xml.dom.minidom
	xml = xml.dom.minidom.parseString(xml_str)
	pritify_str = xml.toprettyxml()
	return pritify_str


def twilio_send_sms(number, text_msg=None, media_url=None):
	message_url = base_url + username + '/Messages'
	auth(username, password)
	data = {
		"From": twilio_number,
		"To": number,
		"Body": text_msg,
		"MediaUrl": media_url,
	}
	r = requests.post(message_url, data=data, auth=auth)
	return xml_pritify(r.text)

