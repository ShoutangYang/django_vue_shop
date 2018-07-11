# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'

import requests
import  json

class YunPian(object):
    def __init__(self,api_key):
        self.api_key=api_key
        self.single_send_url= 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_ms(self,code,mobile):
        params ={
            "apikey":self.api_key,
            "mobile":mobile,
            "text":"【杨寿堂】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code),
        }
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }
        response = requests.post(self.single_send_url,data=params)
        re_dict = json.loads(response.text)
        return  re_dict


if __name__ == '__main__':

    yunpian = YunPian("18a39ccdf3c590373d2f5dc8571a3a34")
    yunpian.send_ms(123456,'18616741206')