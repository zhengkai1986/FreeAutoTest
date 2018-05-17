#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 14:56
# @author :zhengkai
# @File :asserts.py

from .log import LOG,logger
@logger('断言测试结果')
def assert_in(assert_expect,response_json):
    if len(assert_expect.split('=')) > 1:
        data = assert_expect('&')
        result = dict([(item.split('=')) for item in data])
        value1 = ([(str(response_json[key])) for key in result.keys()])
        value2 = ([(str(value)) for value in result.values()])
        if value1 == value2:
            return {'code':0,"result":'pass'}
        else:
            return {'code':1,"result":'fail'}
    else:
        LOG.info('填写测试期望值')
        return {'code':2,"result":'填写测试期望值'}
@logger('断言测试结果')
def assert_out(assert_expect):
    if len(assert_expect.split('=')) > 1:
        data = assert_expect.split('&')
        result = dict([(item.split('='))for item in data])
        return  result
    else:
        LOG.info('填写测试期望值')
        raise {'code':1,'result':'填写测试期望值'}

