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
from configparser import ConfigParser
import os
from datetime import datetime

class DB_Handler():
    def __init__(self,path):
        #如果用户没指定绝对路径则默认相对位置
        if path:
            self.root = path        #要遍历的目录
        else:
            self.root = "circus.conf"  #要遍历的目录

        self.projectIni = ConfigParser()
        self.projectIni.read(self.root)
        self.projectStatic = dict()
        self.SetProjectStartMore()

    def GetProject(self):
        sections = self.projectIni.sections()
        result = dict()
        now = datetime.now()
        for name in sections:
            project = ConfigParser()
            path = self.projectIni.get(name,'PATH')
            project.read(path)
            projectName = project.sections()
            result[name[8:]] = dict()
            result[name[8:]]['project'] = list()
            result[name[8:]]['circus'] = dict()

            for name2 in projectName:
                tempDict = dict()
                #项目内容
                if name2.startswith('watcher') and name2[8:] != 'myproject':
                    tempDict['name'] = name2[8:]
                    tempDict['port'] = project.get(name2,'PORT')
                    tempDict['state'] = self.projectStatic[tempDict['port']]['state']
                    pt = self.projectStatic[tempDict['port']]['date']
                    rt = now - pt
                    tempDict['runTime'] = rt
                    try:
                        tempDict['pid'] = self.GetProcess(tempDict['port'])
                    except:
                        tempDict['pid'] = ''
                        if tempDict['state'] == '1':
                           tempDict['state'] = '2'

                    result[name[8:]]['project'].append(tempDict)
                #circus内容
                elif name2 == 'circus':
                    pubsub_endpoint = project.get(name2,"pubsub_endpoint").split(':')[2]
                    endpoint = project.get(name2,"endpoint").split(':')[2]
                    result[name[8:]]['circus']['pubsub_endpoint'] = pubsub_endpoint
                    result[name[8:]]['circus']['endpoint'] = endpoint
                    #组装键名
                    key = pubsub_endpoint + endpoint
                    result[name[8:]]['circus']['state'] = self.projectStatic[key]['state']
                    pt = self.projectStatic[key]['date']
                    rt = now - pt
                    result[name[8:]]['circus']['runTime'] = rt
                    result[name[8:]]['circus']['path'] = path
                    result[name[8:]]['circus']['pid'] = list()
                    try:
                        p1,p2 = self.GetProcess(pubsub_endpoint)
                        result[name[8:]]['circus']['pid'].append(p1)
                        result[name[8:]]['circus']['pid'].append(p2)
                    except:
                        if result[name[8:]]['circus']['state'] == '1':
                           result[name[8:]]['circus']['state'] = '2'
        return result

    #初始化所有程序
    def SetProjectStartMore(self):
        sections = self.projectIni.sections()
        for name in sections:
            path = self.projectIni.get(name,'PATH')
            self.SetProjectStartOne(path)


    #初始化单个程序
    def SetProjectStartOne(self,path):
        result = list()
        now = datetime.now()
        project = ConfigParser()
        project.read(path)
        projectName = project.sections()
        for name2 in projectName:
            if name2.startswith('watcher') and name2[8:] != 'myproject':
                #端口唯一所以不需要很复杂的数据结构
                self.projectStatic[project.get(name2,'PORT')] = {'date':now,'state':'1'}

            elif name2 == 'circus':
                pubsub_endpoint = project.get(name2,"pubsub_endpoint").split(':')[2]
                endpoint = project.get(name2,"endpoint").split(':')[2]
                key = pubsub_endpoint + endpoint
                self.projectStatic[key] = {'date':now,'state':'1'}
        #初始化开启项目
        try:
            os.system("circusd {} &".format(path))
        except:
            pass

        return result

    #获取程序PID
    def GetProcess(self,port):
        ret = os.popen("lsof -i:{}".format(port))
        str_list = ret.read()
        ret_list = str_list.split(' ')
        #若是circus的PID，则有2个，否则普通程序都是只有一个端口
        process_pid = ret_list[16]

        if process_pid == '':
            process_pid = ret_list[17]
            return process_pid
        else:
            return process_pid,ret_list[53]

    #获取所有PID
    def GetAllPID(self,path):
        project = ConfigParser()
        project.read(path)
        sections = project.sections()
        result = list()
        portList = list()
        for name in sections:
            if name.startswith('watcher') and name[8:] != 'myproject':
                #端口唯一所以不需要很复杂的数据结构
                try:
                    port = project.get(name,'PORT')
                    result.append(self.GetProcess(port))
                    portList.append(port)
                except:
                    pass
            elif name == 'circus':
                pubsub_endpoint = project.get(name,"pubsub_endpoint").split(':')[2]
                endpoint = project.get(name,"endpoint").split(':')[2]
                #组装键名
                key = pubsub_endpoint + endpoint
                portList.append(key)
                try:
                    p1,p2 = self.GetProcess(pubsub_endpoint)
                    result.append(p1)
                    result.append(p2)
                except:
                    pass

        return result,portList


