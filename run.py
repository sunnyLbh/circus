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
from MyApp import app
from optparse import OptionParser
from MyApp.Config.StaticFunc import ErrorCode
from MyApp.Config.MyExecption import ApiException
from MyApp.Controls.DbHandler import DB_Handler
#程序使用方法信息
def main():
    try:
        path = None
        usage = "python %prog -c <confpath>"
        parser = OptionParser(usage)

        parser.add_option('-c','--conf',action='store',
                          dest='confpath',
                          default=None,
                          help='You custom configuration file path')

        (options,args) = parser.parse_args()
        if options.confpath:
            try:
                path = options.confpath
            except:
                raise ApiException(ErrorCode.WithoutConfPath)

        app.db = DB_Handler(path)
        app.myapp.run(host='0.0.0.0')

    except ApiException as e:
        print (e.forUser)

if __name__ == '__main__':
    main()
    # app.run(host='0.0.0.0')

