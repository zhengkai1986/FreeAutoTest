#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/5 10:33
# @author :zhengkai
# @File :configEmail.py

import os,smtplib,datetime
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.readConfig import readconfig
import zipfile,glob
from common.log import logger

localconfig = readConfig.readconfig()

class Email:
    def __init__(self):
        global host,user,password,port,sender,title
        host = localconfig.get_email("mail_host")
        user = localconfig.get_email("mail_user")
        password = localconfig.get_email("mail_pass")
        port = localconfig.get_email("mail_port")
        sender = localconfig.get_email("sender")
        title = localconfig.get_email("subject")

        # 获取接收对象列表
        self.value = localReadConfig.get_email("receiver")
        self.receiver =[]
        for m in str(self.value).split('/'):
            self.receiver.append(m)

        #定义邮件主题
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = "接口测试报告" + " " + date


        self.logger =self.get_logger()
        self.msg = MIMEMultipart('related')

    def config_header(self):
        #定义邮件头部包含主题、发送方、接收方
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        #定义邮件内容
        f = open(os.path.join(readConfig.proDir,'test_data','emailStyle.txt'))
        content = f.read()
        f.close()
        content_plain = MIMEText(content,'html','UTF-8')
        self.msg.attach(content_plain)
        self.config_image()


