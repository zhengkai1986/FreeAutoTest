#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 15:27
# @author :zhengkai
# @File :create_report.py

from .log import LOG,logger
@logger('保存测试结果')
def save_result(testtime,total,passnum,failnum):
    try:
        f = open('result.txt','a')
        f.write("%s=%s=%s=%s \n"%(testtime,total,passnum,failnum))
        f.close()
    except Exception as e:
        LOG.info('保存测试结果出错，原因：%s' % e)
 