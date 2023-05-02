# coding: utf-8

# 很简陋

from os import system
import webbrowser
import threading
from multiprocessing import Process


def read_path():
    with open('data/app_path.txt', 'r', encoding='utf-8') as fo_r:
        read = fo_r.readlines()
        path_seewo = read[0].strip().split(':', 1)[1]
        path_wechat = read[1].strip().split(':', 1)[1]
        return path_seewo, path_wechat


path = read_path()


# 这微信会把主线程钩住，所以就新建进程了
def new_process(app):
    from os import getpid
    print(getpid())
    system(path[app])


# 希沃白板
def open_seewo():
    open_process = Process(target=new_process, args=(0, ))
    open_process.start()


# 微信
def open_wechat():
    open_process = Process(target=new_process, args=(1,))
    open_process.start()


# 微信文件传输助手
def open_filer():
    webbrowser.open('https://filehelper.weixin.qq.com/')
