#!/usr/bin/env python
# author:zhengkai
# -*- coding:utf-8 -*-
#__author__ = 'zhengkai'
# @Time :2018/5/4 18:02
# @author :zhengkai
# @File :configDB.py
import pymysql
import readConfig as readconfig
from common.log import logger

localconfig = readConfig.readconfig()

class MyDB:
    global host, username, password, port, database, config
    host = localconfig.get_db("host")
    username = localconfig.get_db("username")
    password = localconfig.get_db("password")
    port = localconfig.get_db("port")
    database = localconfig.get_db("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql, params):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        return value

    def closeDB(self):
        """
        close database
        :return:
        """
        self.db.close()
        print("Database closed!")


