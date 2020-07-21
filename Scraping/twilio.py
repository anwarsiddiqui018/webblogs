import twilio
import twilio.rest

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client



# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACa8b979cad79ae0ac1f8243ba299fe1ce'
auth_token = '5f5f74f2a08ce9cc8ca5506e23321025'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the test message from Anwar',
         from_='+12057720438',
         to='+918617240290'
     )

print(message.sid)