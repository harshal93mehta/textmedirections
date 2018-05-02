import json
import urllib.request, json
import re

api_file = "/app/google-key"
api_keys = {}
with open(api_file,'r') as f:
	api_keys = json.loads(f.read())
google_key = api_keys['GOOGLE_KEY']

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
def get_directions(sms_input):
	origin,destination = sms_input.split('*')
	origin = origin.lstrip().rstrip().replace(' ','+')
	destination = destination.lstrip().rstrip().replace(' ','+')
	nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,google_key)
	request = endpoint+nav_request
	response = urllib.request.urlopen(request).read()
	raw_response = json.loads(response)
	routes = raw_response['routes'][0]['legs'][0]['steps']
	instructions_all = ''
	for i in range(len(routes)):
		instructions_all+=routes[i]['html_instructions']+'('+routes[i]['distance']['text']+')'+'\n'
	p = re.compile(r'<.*?>')
	directions = p.sub('',instructions_all)
	return directions

def smsServiceHandler(sms_input):
	if '*' in sms_input:
		return get_directions(sms_input)
	else:
		message = "To get directions on texts, type your query in following format. 'start_point * end_point'. Do not forget the '*' sign. An example query would be 'Dallas,TX * San Antonio,TX' without the quotes."
		return message
