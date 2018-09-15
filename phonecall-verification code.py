# 接口类型：互亿无线语音验证码接口。
# 账户注册：请通过该地址开通账户http://user.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请仔细阅读接口文档；
# （2）请使用 APIID 及 APIKEY来调用接口，可在会员中心获取；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client
from urllib import parse
import random

host = "api.voice.ihuyi.com"
sms_send_uri = "/webservice/voice.php?method=Submit"

# 查看用户名 登录用户中心->语音验证码>产品总览->API接口信息->APIID
account = "*******"
# 查看密码 登录用户中心->语音验证码>产品总览->API接口信息->APIKEY
password = "******"


def send_sms(text, mobile):
    params = parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = "17"
    text = "1125"
    print(text)
    print(send_sms(text, mobile))