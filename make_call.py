from twilio.rest import TwilioRestClient

#add your account sid
account_sid = "ACXXXXXXXXXXXXXXXXX"
#add your auth token
auth_token = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account_sid, auth_token)
#add a number to call for the to param and your twilio number for the from_ param
call = client.calls.create(to="+14085551234", from_="+12125551234", url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

print call.sid