from twilio.rest import Client
import os
import smtplib

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUM = os.environ.get("TWILIO_PHONE_NUM")
MY_PHONE_NUM = os.environ.get("MY_PHONE_NUM")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


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

    def send_emails(self, emails, item, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{item}\n{google_flight_link}".encode('utf-8')
                )


