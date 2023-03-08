from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUM = os.environ.get("TWILIO_PHONE_NUM")
MY_PHONE_NUM = os.environ.get("MY_PHONE_NUM")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, item):
        message = self.client.messages.create(
            body=item,
            from_=TWILIO_PHONE_NUM,
            to=MY_PHONE_NUM,
        )

        print(message.sid)


