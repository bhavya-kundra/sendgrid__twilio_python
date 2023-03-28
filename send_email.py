import os

from dotenv import load_dotenv

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

message = Mail(
    from_email='Enter your email here', # Enter your or that mail through which you have created the api key token and service account
    to_emails='Enter the list of emails', # Enter the list of emails to which you want to send the mails
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>Sending with Twilio SendGrid is Fun with Python</strong>')

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.send(message)
print(response.status_code, response.body, response.headers)
