from __future__ import with_statement
from flask import Flask, render_template, request
from twilio.util import TwilioCapability
import twilio.twiml
import re

app = Flask(__name__)

#add a twilio phone number or number verified with twilio as the caller id
caller_id = "+12125551234"
default_client = "jessica"

@app.route('/voice', methods=["GET", "POST"])
def voice():

	dest_number = request.values.get("PhoneNumber", None)

	resp = twilio.twiml.Response()

	# nest <Client> TwiML inside of a <Dial> verb
	with resp.dial(callerId=caller_id) as r:
		if dest_number and re.search('^[\d\(\)\- \+]+$', dest_number):
			r.number(dest_number)
		else:
			r.client(default_client)

	return str(resp)

@app.route("/client", methods=["GET", "POST"])
def client():

	   # Find these values at twilio.com/user/account
    account_sid = "AC123123aaaaaaaaaaaaaaaaaa"
    auth_token = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

	#this is a special quick-start application sid
	application_sid = "APabe7650f654fc34655fc81ae71caa3ff" # Twilio Application Sid
	capability = TwilioCapability(account_sid, auth_token)
	capability.allow_client_outgoing(application_sid)
	capability.allow_client_incoming("jessica")
	token = capability.generate()

	return render_template('client.html', token=token)

if __name__ == "__main__":
	app.run(debug=True)