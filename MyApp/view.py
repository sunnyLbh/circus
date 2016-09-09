# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '8/31/2016'

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
from flask import render_template,request
from MyApp.app import myapp,datetime
import json
from MyApp.Config.StaticFunc import ErrorCode,Set_return_dicts_admin
from MyApp.Config.MyExecption import ApiException
import os

@myapp.route('/', methods=['GET'])
def getProject():
    from MyApp.app import db
    result = db.GetProject()
    return render_template('project_list.html',result=result)

#子进程重启
@myapp.route('/restart', methods=['POST'])
def restart():
    try:
        from MyApp.app import db
        process_pid = request.form.get('pid')
        if not process_pid:
            raise ApiException(ErrorCode.ParameterMiss)
        else:
            os.system("kill -9 {}".format(process_pid))
            port = request.form.get('port')
            db.projectStatic[port]['date'] = datetime.now()
            # db.projectStartDate[port]['state'] = '2'

        return Set_return_dicts_admin({'value':'success'})

    except ApiException as e:
        return Set_return_dicts_admin(forWorker=e.forWorker,
                                      code=e.errorCode,
                                      forUser=e.forUser)
#父进程开启
@myapp.route('/circus/start',methods=['POST'])
def circus_start():
    try:
        from MyApp.Controls.HandlerFunc import StartCircus
        process_pid = json.loads(request.form.get('pid'))
        port = request.form.get('port')
        path = request.form.get('path')
        try:
            StartCircus(process_pid,port,path)
        except:
            raise ApiException(ErrorCode.QueryLangFormatError)

        return Set_return_dicts_admin({'value':'success'})

    except ApiException as e:
        return Set_return_dicts_admin(forWorker=e.forWorker,
                                      code=e.errorCode,
                                      forUser=e.forUser)

#父进程重启
@myapp.route('/circus/restart', methods=['POST'])
def circus_restart():
    from MyApp.Controls.HandlerFunc import StopCircus,StartCircus
    try:
        path = request.form.get('path')
        port = request.form.get('port')
        try:
            StopCircus(path)
            StartCircus('',port,path)
        except:
            raise ApiException(ErrorCode.QueryLangFormatError)

        # os.system("circusd {} &".format(path))

        # db.projectStatic[port]['date'] = datetime.now()
        # db.projectStartDate[port]['state'] = '1'

        return Set_return_dicts_admin({'value':'success'})

    except ApiException as e:
        return Set_return_dicts_admin(forWorker=e.forWorker,
                                      code=e.errorCode,
                                      forUser=e.forUser)

#父进程停止
@myapp.route('/circus/stop', methods=['POST'])
def circus_stop():
    from MyApp.Controls.HandlerFunc import StopCircus
    try:
        path = request.form.get('path')
        # try:
        StopCircus(path)
        # except:
        #     raise ApiException(ErrorCode.QueryLangFormatError)
        return Set_return_dicts_admin({'value':'success'})
    except ApiException as e:
        return Set_return_dicts_admin(forWorker=e.forWorker,
                                      code=e.errorCode,
                                      forUser=e.forUser)






