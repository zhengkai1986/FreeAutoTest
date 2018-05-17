#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 18:04
# @author :zhengkai
# @File :httpEnclosure.py

"""
封装http接口
"""

from .test_requests import request
class TestHttpAPI(object):
    def __init__(self,url,key,params,method):
        self.url = url
        self.key = key
        self.params = params
        self.method = method

    def testHttpApi(self):
        if self.method =='POST':
            self.param = {'key':self.key,'info':self.params}
            self.response = request.post(self.url,self.param)
        elif self.method =='GET':
            self.param = {'key':self.key,'info':self.params}
            self.response = request.get(url=self.url,params=self.param)
        elif self.method =='DEL':
            self.param = {'key': self.key, 'info': self.params}
            self.response = request.delete(url=self.url,params=self.param)
        elif self.method =='PUT':
            self.param = {'key': self.key, 'info': self.params}
            self.response = request.put(url=self.url,params=self.param)
        return self.response
    def getjson(self):
        json_data = self.testHttpApi()
        return json_data
