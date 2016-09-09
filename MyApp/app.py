# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '9/1/2016'

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
from flask import Flask
from datetime import datetime

db = None
startTime = datetime.now()

myapp = Flask(__name__)
myapp.config.update(
        DEBUG = False,
        TESTING = False,
        SECRET_KEY='my_circus_control',
        CSRF_ENABLED = True,
)
