# textmedirections
	textmedirections is a web-app designed to get map directions from one place to other in plain text using text messages. The purpose is to get quick and simplified directions over SMS in the absence of internet services on one's phone. 
	
# How it works
	User sends an SMS to a twilio based phone number with programmable SMS capability. The phone number is linked with a webhook to a heroku web server link where the web-app is deployed. The web-app is a python based flask app that receives SMS from twilio phone number. Using Google's direction API, the directions are fetched into json format and is then filtered to get the plain text directions. It is then sent back to twilio phone number using a message response and in turn sent it to user as a text message on the phone.
	
	Currently this app is running on a heroku server.
	
# How to use it for yourself
	--> Clone the repo
	--> Open a google devolopers account and get an access key and save it in a file named "google-key" in the same directory
	--> Get a twilio phone number
	--> The requirements file has list of dependencies needed for heroku servers
	--> Deploy to heroku and get set the twilio number SMS webhook to the heroku app's link
	--> Test sending a message to twilio number.