#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 19:34
# @author :zhengkai
# @File :httpcase.py

from common.httpEnclosure import TestHttpAPI
from utils.parse_excel import dataexcel
from common.log import LOG,logger
import os
from common.asserts import assert_in

path = os.getcwd()+'\\test_data\\case.xlsx'
listid,listname,listkey,listparams,listurl,listmethod,listexpect=dataexcel(path)
@logger('测试')
def testInterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listresult = []
    list_unkown = []
    list_exception = []
    for i in range(len(listurl)):
        api = TestHttpAPI(url=listurl[i],key=listkey[i],params=listparams[i],method=listmethod[i])
        apijson = api.getjson()
        if apijson['code']==0:
            LOG.info('inputdata>参数:%s,url:%s,返回:%s,预期:%s'%(listparams[i],listurl[i],apijson,listexpect[i]))
            assert_re = assert_in(assert_expect=listexpect[i],response_json=apijson)
            if assert_re['code']==0:
                list_json.append(apijson['result'])
                listresult.append('pass')
                list_pass +=1
            elif assert_re['code']==1:
                list_fail +=1
                listresult.append('fail')
                list_json.append(apijson['result'])
            elif assert_re['code']==2:
                list_exception +=1
                listresult.append('exception')
                list_json.append(assert_re['result'])
            else:
                list_unkown +=1
                listresult.append('unkown')
                list_json.append(assert_re['unkown'])
        else:
            list_exception +=1
            listresult.append('exception')
            list_json.append(apijson['result'])
            continue
    return listresult,list_fail,list_pass,list_exception,list_unkown