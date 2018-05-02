from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from get_google_directions import get_directions, smsServiceHandler

app = Flask(__name__)

@app.route('/sms', methods=['GET','POST'])
def sms():
    if request.method == 'POST':
	    message_body = request.form['Body']
	    resp = MessagingResponse()
	    directions = smsServiceHandler(message_body)
	    if(len(directions)>1600):
	    	directions = directions[:1500] + '...'
	    resp.message(directions)
	    return str(resp)
    else:
	    return '<h1>This is a web app with POST method, so there is nothing to show on this page here. See you later.</h1>'