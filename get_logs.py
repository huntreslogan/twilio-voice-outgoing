from twilio.rest import TwilioRestClient

#add your account sid

account_sid = "ACXXXXXXXXXXXXXXXXX"

#add your auth token
auth_token = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(account_sid, auth_token)

for call in client.calls.list():
	print "From " + call.from_formatted + "To: " + call.to_formatted