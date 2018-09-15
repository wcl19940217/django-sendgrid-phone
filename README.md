# django-sendgrid-phone
python

sendgrid：
#帮助文档https://github.com/sendgrid/sendgrid-python
https://sendgrid.com/docs/ui/account-and-settings/
https://sendgrid.api-docs.io/v3.0/mail-send/v3-mail-send

1、注册
https://sendgrid.com/注册账号，选择语言类型，创建api-keys。

2、开发环境keys值设定
把创建的keys值放进去。开发环境的shell
Mac
Update the development environment with your SENDGRID_API_KEY (more info here), for example:
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
Sendgrid also supports local environment file .env. Copy or rename .env_sample into .env and update SENDGRID_API_KEYwith your key.
Windows
Temporarily set the environment variable(accesible only during the current cli session):
set SENDGRID_API_KEY=YOUR_API_KEY
Permanently set the environment variable(accessible in all subsequent cli sessions):
setx SENDGRID_API_KEY "YOUR_API_KEY"
Install Package
pip install sendgrid



3、测试代码
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *


def verification():
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("604603701@qq.com")
    to_email = Email("18804928235@163.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


if __name__ == '__main__':
    verification()

# import sendgrid
# import os
# sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
# data = {
#   "personalizations": [
#     {
#       "to": [
#         {
#           "email": "test@example.com"
#         }
#       ],
#       "subject": "Sending with SendGrid is Fun"
#     }
#   ],
#   "from": {
#     "email": "test@example.com"
#   },
#   "content": [
#     {
#       "type": "text/plain",
#       "value": "and easy to do anywhere, even with Python"
#     }
#   ]
# }
# response = sg.client.mail.send.post(request_body=data)
# print(response.status_code)
# print(response.body)
# print(response.headers)


4、Plan
 
Plan分为三类：
1）、email api
2）、marketing campaigns（营销活动）
3）、email api 和marketing campaigns（两者一起）

5、SMTP
简单邮件传输协议(Simple Mail Transfer Protocol,SMTP) 是在Internet传输email的事实标准

6、SendGridAPIClient参数情况
继承自object。

初始化参数：
apikey: sendgrid需要使用的key。如果未提供的话，会在环境变量中查找。
api_key: sendgrid需要使用的key,提供后面的版本兼容，5.3，后就会被弃用。
impersonate_subuser：模仿subuser账号，底层客户端。

Host：api调用的基本的URL。

Opts：弃用参数的调度员。后面兼容的版本用path参数，在6以后的版本会移除。

7、mail参数
（1）from_email   来自邮箱
（2）subject  主题
（3）to_email   给谁发送
（4）content   正文
（5）get方法

方法里面有多个条件。
字典形式存储邮箱，正文和主题等。

Keys为：personalizations，个性化(里面是元组，元组里面是字典，里面是主题，给谁发送消息),from（来自哪个邮箱）,content（正文消息）。

8、email参数
（1）email 邮箱
（2）name 名字

 https://sendgrid.api-docs.io/v3.0/mail-send/v3-mail-send

9、headers
Authorization ，string ，1 ，validations，required

10、request body
 

 

 

 

 

 

 

 

11、response
Stats：400、
 
401：
 
413：
 
202：
成功状态。

安装：pip install celery  
pip install eventlet

需要提前安装redis。
（Download, extract and compile Redis with:
$ wget http://download.redis.io/releases/redis-4.0.11.tar.gz
$ tar xzf redis-4.0.11.tar.gz
$ cd redis-4.0.11
$ make
The binaries that are now compiled are available in the src directory. Run Redis with:
启动服务
$ src/redis-server
You can interact with Redis using the built-in client:
）
运行redis，rebitmq或者其他。src/redis-server redis.conf



创建一个tasks.py文件。
from celery import Celery
import time


app = Celery('tasks', broker='redis://192.168.118.130:6379/0',
             backend="redis://192.168.118.130:6379/0")


@app.task
def send_mail():
    print('hello world')

创建一个需要执行的文件。T1.py
from tasks import send_mail

if __name__ == '__main__':
    send_mail.delay() #括号里面可以放参数，把要要发送的邮件的地址放进去。

pycharm里面命令行执行：

celery -A tasks worker --loglevel=info -P eventlet

执行需要执行的文件，然后会收到相关问题。返回的问题等。


send_mail.delay()  可以送参数，把参数直接放进去。邮箱地址。





