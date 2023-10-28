from celery import shared_task

from decouple import config
from twilio.rest import Client

account_sid = config("TWILIO_ACCOUNT_SID", default="")
auth_token = config("TWILIO_AUTH_TOKEN", default="")

client = Client(account_sid, auth_token)


@shared_task
def send_phone_message(phone, message):
    print("Start messaging")
    message = client.messages.create(body=message, from_="+19516662166", to=phone)
    print(message.sid)
    return message.sid
