#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/16 14:54
# @author :zhengkai
# @File :errors.py

"""
 自定义异常类

"""
class TokenException(Exception):
    """
    gettoken失败时抛出此异常
    """
    pass

class LoginException(Exception):
    """
    登录失败时抛出此异常
    """
    pass
