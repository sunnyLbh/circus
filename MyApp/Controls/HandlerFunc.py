# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '9/6/2016'

                ┏┓     ┏┓
              ┏┛┻━━━┛┻┓
             ┃     ☃     ┃
             ┃ ┳┛  ┗┳  ┃
            ┃     ┻     ┃
            ┗━┓     ┏━┛
               ┃     ┗━━━┓
              ┃  神兽保佑   ┣┓
             ┃　永无BUG！  ┏┛
            ┗┓┓┏━┳┓┏┛
             ┃┫┫  ┃┫┫
            ┗┻┛  ┗┻┛
"""
import os
from MyApp.app import db
def StopCircus(path):
    pidList,portList = db.GetAllPID(path)
    for pid in pidList:
        os.system("kill -9 {}".format(pid))
    for port in portList:
        db.projectStatic[port]['state'] = '0'

def StartCircus(process_pid,port,path):
    db.SetProjectStartOne(path)
    # os.system("circusd {} &".format(path))
    # db.projectStatic[port]['date'] = datetime.now()
    # db.projectStatic[port]['state'] = '1'
