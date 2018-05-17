#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 21:02
# @author :zhengkai
# @File :readConfig.py

import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir,'config.ini')

class readconfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        if data[0:3] ==codecs.BOM_UTF8:
            data =data[3:]
            file = codecs.open(configPath,'w')
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self,name):
        value = self.cf.get('EMALL',name)
        return value

    def get_http(self,name):
        value = self.cf.get('HTTP',name)
        return value

    def get_headers(self,name):
        value = self.cf.get('HEADERS',name)
        return value

    def set_headers(self,name,value):
        self.cf.set('HEADERS',name,value)
        with open(configPath,'w+') as f:
            self.cf.write(f)

    def get_url(self,name):
        value = self.cf.get('URL',name)
        return value

    def get_db(self,name):
        value = self.cf.get('DATABASE',name)
        return value

 