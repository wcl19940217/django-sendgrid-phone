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


