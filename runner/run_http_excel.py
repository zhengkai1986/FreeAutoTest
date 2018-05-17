#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 21:34
# @author :zhengkai
# @File :run_http_excel.py

from common.report_excel import create
import os,datetime
from testcase.httpcase import testInterface
from utils.parse_excel import dataexcel

def start_excel_report_http():
    m = datetime.datetime.now().strftime("%Y%m%d")
    basedir = os.getcwd()+'\\test_data\\httpcase.xls'
    listid,listname,listkey,listparams,listurl,listmethod,listexpect =dataexcel(basedir)
    listresult,list_fail,list_pass,list_json,list_expection,list_unkown =testInterface()
    filepath = os.path.join(basedir + '\\test_report\\%s-result.xls'%m)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s'% filepath)
    create(filename=filepath,list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey,listparams=listparams, listmethods=listmethod, listexpects=listexpect,
           listids=listid,listresults=listresult, listnames=listname)
    contec = 'dubbo接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
        list_pass, list_fail, list_expection, list_unkown, filepath)
if __name__ =='__main__':
    start_excel_report_http()