#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 21:34
# @author :zhengkai
# @File :run_http_html.py

import os,datetime,time
from testcase.httpcase import testInterface
from common.report_html import createHtml
from utils.parse_excel import dataexcel

def start_interface_html_http():
    starttime = datetime.datetime.now()
    day = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
    basdir = os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd()+'\\test_data\\httpcase.xls'
    listid,listname,listkey,listparams,listurl,listmethod,listexpect= dataexcel(path)
    listresult, list_fail, list_pass, list_json, list_exception, list_unkown = testInterface ()
    filepath = os.path.join(basdir+'\\test_report\\%s-result.html'%day)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s'%filepath)
    endtime = datetime.datetime.now()
    createHtml(titles='http接口自动化测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,param=listparams,url=listurl,meth=listmethod,
               expect=listexpect,json=list_json,results=listresult,unkown=list_unkown,exceptions=list_exception)
    contec = 'http接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
        list_pass, list_fail, list_exception, list_unkown, filepath)
    # send_ding (content=contec)

if __name__ == '__main__':
    start_interface_html_http ()


 