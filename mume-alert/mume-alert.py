#!/usr/bin/env python3
from sys import argv
from twilio.rest import Client

script, msg = argv

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'YOUR_SID_HERE'
auth_token = 'YOUR_TOKEN_HERE'

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="MUME ALERT!: " + msg,
                     from_='+15555555555',
                     to='+15555555554'
                 )

print(message.sid)
