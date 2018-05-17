#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 17:09
# @author :zhengkai
# @File :test_requests.py
import json
import requests
from .log import LOG,logger
@logger('requests封装')
class request():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
    #get请求消息
    def get(self,url,params):
        try:
            r = request.get(url,params=params,headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            return {'code':0,'result':json_response}
        except Exception as e:
            LOG.info('get请求出错，出错原因：%s'%e)
            return {'code':1,'result':'get请求出错，出错原因：%s'%e}
    #post请求消息
    def post(self,url,params):
        data = json.dumps(params)
        try:
            r = request.post(url,params=data,headers=self.headers)
            json_response = json.loads(r.text)
            return {'code':0,'result':json_response}
        except Exception as e:
            LOG.info ('post请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}
    #delete请求消息
    def delete(self,url,params):
        try:
            del_data = request.delete(url,params=params,headers=self.headers)
            json_response = json.loads(del_data.text)
            return {'code':0,'result':json_response}
        except Exception as e:
            LOG.info ('delete请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'delete请求出错，出错原因:%s' % e}
    #put请求消息
    def put(self,url,params):
        try:
            data = json.dumps(params)
            me = request.put(url,data)
            json_response = json.loads(me.text)
            return {'code':0,'result':json_response}
        except Exception as e:
            LOG.info ('put请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}








 