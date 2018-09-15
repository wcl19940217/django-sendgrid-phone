# With Mail Helper Class
# 使用这个库之前需要先去官网注册账号和app。然后把keys值设置到开发环境中。
# 在readme 中进行讲解
import sendgrid
import os
from sendgrid.helpers.mail import *


def verification():
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("******@163.com")
    to_email = Email("****@qq.com@qq.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


if __name__ == '__main__':
    verification()
