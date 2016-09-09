# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '4/15/2016'

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
import json

class ErrorCode():
    QueryLangFormatError = 1000      #查询语言语法出错
    NoneData = 1002                  # 没有数据
    DataUnSave = 1003                # 数据无法保存
    JsonError = 1004                 #接收的JSON格式出错
    MethodError = 1006               #错误的请求方式
    OpenAgain = 1007                 #程序已经开启

    ParameterError = 1100            #参数错误
    ParameterMiss = 1101             #参数缺失
    ErrorRequest = 1102              #错误的请求

    UserMore = 1202                  #已有此用户
    AutomaticLogoError = 1203        #自动登陆出错

    ErrorFindCode = 2000             #未识别错误码

    WithoutConfPath = 1300           #运行时没有设置配置文件路径

    ERROR_MESSAGE = {

        QueryLangFormatError: {'forWorker':u"查询语言语法出错,请检查语法",
                                      'forUser':u"查询语言语法出错,请检查语法"},

        OpenAgain:{
                    'forWorker':u"启动端口冲突",
                    'forUser':u"有程序正在运行，请关闭后重试"
                    },

        NoneData: {'forWorker':u"没有数据",
                   'forUser':u"没有数据"},

        DataUnSave: {'forWorker':u"数据无法保存",
                     'forUser':u"数据无法保存"},

        JsonError : {'forWorker':u"接收的JSON格式出错",
                     'forUser':u"请求错误"},

        MethodError : {'forWorker':u"请求方式出错",
                             'forUser':u"请求错误"},

        UserMore : {'forWorker':u"已有此用户",
                    'forUser':u"已有此用户"},

        AutomaticLogoError : {'forWorker':u"该用户在其他设备上登录过，因此自动登录失效",
                             'forUser':u"登录超时"},

        ParameterError: {'forWorker':u"不合法的参数",
                         'forUser':u"请求错误"},
        ParameterMiss: {'forWorker':u"参数缺失",
                        'forUser':u"请求错误"},
        ErrorRequest : {'forWorker':u"请求错误",
                        'forUser':u"请求错误"},

        ErrorFindCode : {'forWorker':u"未识别错误码",
                          'forUser':u"请求错误"},

        #---------------------启动错误---------------------------------
        WithoutConfPath : {
                            'forWorker':u"please write you path after -c/--conf",
                            'forUser':u"please write you path after -c/--conf"
                           },
    }

#设置返回值
#forUser是显示给用户看的文字，forWorker是显示提供给后台程序员看的字段
#ret代表成功或者失败，data代表返回值，result代表错误代码
def Set_return_dicts_admin(data={},forUser='',forWorker='',result=0,code=None,ret=None,Json=False):
    if not ret:
        if forUser != '':
            ret = 'failure'
        else:
            ret = 'success'

    return_dicts = {
        'data' : data,
        'forUser' : forUser,
        'forWorker' : forWorker,
        'code' : code,
        'result' : result,
        'ret' : ret,
        'Json' : Json
    }
    return json.dumps(return_dicts)

