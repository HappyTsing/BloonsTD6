# 免注册调用方法
import ctypes
import os
from comtypes.client import CreateObject
import win32com.client

try:
    dm = win32com.client.Dispatch('dm.dmsoft')
    print('本机系统中已经安装大漠插件，版本为:', dm.ver())
except:
    print('本机并未安装大漠，正在免注册调用')
