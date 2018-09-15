from celery import Celery
import time
import sendgrid
import os
from sendgrid.helpers.mail import *


app = Celery('tasks', broker='redis://192.168.118.130:6379/0',
             backend="redis://192.168.118.130:6379/0")


@app.task
def send_mail(email):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("18804928235@163.com")
    to_email = Email(email)
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
