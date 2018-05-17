#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 20:09
# @author :zhengkai
# @File :httpcase.py

from common.httpEnclosure import TestHttpAPI
from utils.parse_excel import makedata
from common.log import LOG,logger
from common.asserts import assert_in
import ddt,unittest

data_test = makedata()
@ddt.ddt
class runTest(unittest.TestCase):
    def setUp(self):
        LOG.info('测试用例开始执行')
    def tearDown(self):
        LOG.info('测试用例执行完毕')
    @ddt.data(*data_test)
    def test_api(self,data_test):
        api = TestHttpAPI(url=data_test['url'],key=data_test['key'],params=data_test['params'],method=data_test['method'])
        LOG.info('输入参数：url:%s,key:%s,参数:%s,请求方式：%s'%(data_test['url'],data_test['key'],data_test['params'],
        LOG.info ('输入参数：url:%s,key:%s,参数:%s,请求方式：%s' % (
        data_test['url'], data_test['key'], data_test['params'],data_test['method']))))
        apijson = api.getjson()
        LOG.info('返回结果:%s'%apijson)
        expect = assert_in(assert_expect=data_test['expect'])
        self.assertNotEqual(dict(expect),dict(apijson),msg='预期和返回不一致')
