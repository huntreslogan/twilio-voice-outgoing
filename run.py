from flask import Flask, render_template
from twilio.util import TwilioCapability

app = Flask(__name__)

@app.route("/client", methods=["GET", "POST"])
def client():

	#add your account sid
	account_sid = "AC0bcd7ce3b4dfef5983ee48a0189618d8"
	#add your auth token
	auth_token = "c3c87709f501e8018bae7275d929db6f"

	#this is a special quick-start application sid
	application_sid = "APabe7650f654fc34655fc81ae71caa3ff"

	capability = TwilioCapability(account_sid, auth_token)
	capability.allow_client_outgoing(application_sid)

	token = capability.generate()

	return render_template('client.html', token=token)

if __name__ == "__main__":
	app.run(debug=True)