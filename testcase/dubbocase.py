#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 20:37
# @author :zhengkai
# @File :dubbocase.py

from common.dubboEnclosure import testDubboInterface
from common.log import LOG,logger
from common.asserts import assert_in
from utils.parse_excel import dataexcel
import os

path = os.getcwd()+'\\test_data\\dubbocase.xls'
listid,listurl,listinterface,listmethod,listobject,listparam,listassert=dataexcel(path)
@logger('dubbo接口测试')
def testdubboInterface():
    list_pass = 0
    list_fail = 0
    list_json = 0
    listresult = 0
    list_unkown = 0
    list_exception = 0
    for i in range(len(listid)):
        dubboapi = testDubboInterface(url=listurl,interface=listinterface[i],method=listmethod[i],param=listobject[i],**(eval(listparam[i])))
        dubboapiresult = dubboapi.getresult()
        if dubboapiresult['code'] ==0:
            LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s' % (listparam[i], listurl[i], dubboapiresult, listassert[i]))
            assert_out = assert_in(assert_expect=listassert[i],response_json=dubboapiresult)
            if assert_out['code'] ==0:
                list_json.append(dubboapiresult['result'])
                listresult.append('pass')
                list_pass +=1
            elif assert_out['code'] ==1:
                list_fail +=1
                listresult.append('fail')
                list_json.append(dubboapiresult['result'])
            elif assert_out['code'] ==2:
                list_exception +=1
                listresult.append('exception')
                list_json.append(dubboapiresult['result'])
            else:
                list_unkown +=1
                listresult.append('未知错误')
                list_json.append('未知错误')
        else:
            list_exception +=1
            listresult.append('exception')
            list_json.append(dubboapiresult['result'])
            continue
        return listresult,list_fail,list_pass,list_json,list_exception,list_unkown