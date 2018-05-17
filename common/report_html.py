#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 15:50
# @author :zhengkai
# @File :report_html.py

titles='接口测试'
def title(titles):
    title = '''<!DOCTYPE html>
    	<html lang="en">
    	<head>
    		<meta charset="UTF-8">
    		<title>%s</title>
    		<style type="text/css">
    			td{ width:40px; height:50px;}
    		</style>
    	</head>
    	<body>
    	''' % (titles)
    return title
content='''<div style='width: 1170px;margin-left: 15%'>
<h1>接口测试的结果</h1>'''
def homepage(starttime,endtime,passge,fail,exceptions,unkownError):
    background='''
    <p><strong>开始时间:</strong> %s</p>
		<p><strong>结束时间:</strong> %s</p>
		<p><strong>耗时:</strong> %s</p>
		<p><strong>结果:</strong>
			<span >Pass: <strong >%s</strong>
			Fail: <strong >%s</strong>
			       exception: <strong >%s</strong> 
			       unkown: <strong >%s</strong></span></p>                  
			    <p ><strong>测试详情如下</strong></p>  </div> '''%(starttime,endtime,(endtime-starttime),passge,fail,exceptions,unkownError)
    return background
shanghai = '''
            <p>&nbsp;</p>
            <table border='2'cellspacing='1' cellpadding='1' width='1100'align="center" >
    		<tr >
                <td ><strong>用例ID&nbsp;</strong></td>
                <td><strong>用例名字</strong></td>
                <td><strong>key</strong></td>
                <td><strong>请求内容</strong></td>
                <td><strong>url</strong></td>
                <td><strong>请求方式</strong></td>
                <td><strong>预期</strong></td>
                <td><strong>实际返回</strong></td>  
                <td><strong>结果</strong></td>
            </tr>
        '''
def passfail(tend):
    if tend =='pass':
        htl = ' <td bgcolor="green">pass</td>'
    elif tend == 'fail':
        htl = ' <td bgcolor="fail">fail</td>'
    elif tend == 'weizhi':
        htl = '<td bgcolor="red">error</td>'
    else:
        htl = '<td bgcolor="#9300">error</td>'
    return htl

def ceshixiangqing(id, name, key, param, url, meth, expect, json, result):
        xiangqing = '''
            <tr>
                <td>%s</td>
                <td>%s</td>

                <td>%s</td>
                <td>%s
               </td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                %s
            </tr>

        ''' % (id, name, key, param, url, meth,expect, json, passfail (result))
        return xiangqing

weibu = '''
    </table>
    </body>
    </html>'''

def result(titles, starttime, endtime, passge, fail, id, name, key, param, url, meth, expect, json, result,
               exceptions, unkown):
    if type (name) == list:
        relus = ' '
        for i in range (len (name)):
            relus += (
                    ceshixiangqing (id[i], name[i], key[i], param[i], url[i], meth[i], expect[i], json[i], result[i]))
            text = title (titles) + content + homepage (starttime, endtime, passge, fail, exceptions,
                                                      unkown) + shanghai + result + weibu
        else:
            text = title (titles) + content + homepage (starttime, endtime, passge, fail, exceptions,
                                                      unkown) + shanghai + ceshixiangqing (id, name, key, param, url,
                                                                                           meth, expect, json,
                                                                                           result) + weibu
        return text

def createHtml(filepath, titles, starttime, endtime, passge, fail, id, name, key, param, url, meth, expect, json,
                   results, exceptions, unkown):
    texts = result (titles, starttime, endtime, passge, fail, id, name, key, param, url, meth, expect, json,
                        results, exceptions, unkown)
    with open (filepath, 'wb') as f:
        f.write (texts.encode ())

