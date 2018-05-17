#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 15:34
# @author :zhengkai
# @File :parse_excel.py
import os
import xlrd
from common.log import LOG,logger
@logger('解析测试用例文件')
def dataexcel(filepath):
    try:
        file = xlrd.open_workbook(filepath)
        me = file.sheets()[0]
        nrows = me.nrows
        listid=[]
        listname=[]
        listkey=[]
        listparams=[]
        listurl=[]
        listmethod=[]
        listexpect=[]
        listresult=[]
        for i in range(1,nrows):
            listid.append(me.cell(i,0).value)
            listname.append (me.cell (i, 1).value)
            listkey.append (me.cell (i, 2).value)
            listparams.append (me.cell (i, 3).value)
            listurl.append(me.cell(i,4).value)
            listmethod.append (me.cell (i, 5).value)
            listexpect.append (me.cell (i, 6).value)
        return listid,listname,listkey,listparams,listurl,listmethod,listexpect
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s'%e)

@logger('生成数据驱动测试数据')
def makedata():
    path = os.getcwd() + '\\test_case\\case.xlsx'
    listid,listname,listkey,listparams,listurl,listmethod,listexpect =dataexcel(path)
    make_data=[]
    for i in range(len(listid)):
        make_data.append({'url':listurl[i],'key':listkey[i],'params':listparams[i],'method':listmethod[i],'expect':listexpect[i]})
        i+=1
    return make_data

