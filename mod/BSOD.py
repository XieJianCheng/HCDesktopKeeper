# coding: utf-8

# 这是复刻蓝屏的等比例缩小版
# 只支持复刻win10蓝屏
# 可以在图片资源存在的情况下自由内嵌

# 兼容1680*1050和1920*1080下125%、150%、175%缩放
# 兼容1680*1050分辨率以下各种缩放
# 1680*1050及以上分辨率的100%缩放在完整版兼容更好
# 800*600完全不兼容

import os
import wx
import ctypes
import random

shutdown_state = True


class blue_screen_win10(wx.Frame):
    winapi = ctypes.windll.user32
    screen_x = winapi.GetSystemMetrics(0)
    screen_y = winapi.GetSystemMetrics(1)

    size = (screen_x+18, screen_y+43)

    # 加载百分比
    load_num = 0
    stop_state = False

    def __init__(self, parent=None, id=-1):
        # 初始化
        super().__init__(parent, id, 'BSOD', pos=(-8, -35))
        wx.Frame.SetMinSize(self, size=self.size)
        wx.Frame.SetMaxSize(self, size=self.size)
        wx.Frame.SetSize(self, size=self.size)
        pnl = wx.Panel(self)

        # 文字控件
        self.word_face = wx.StaticText(pnl, label=':(', pos=(100, 50))
        self.word_contents_1 = wx.StaticText(pnl, label='你的设备遇到问题，需要关机。\n我们只收集某些错误信息，然后为你关闭电脑。', pos=(100, 200))
        self.word_contents_2 = wx.StaticText(pnl, label='90%完成', pos=(100, 325))
        img = wx.Image('data/QR.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()                  # 假二维码
        wx.StaticBitmap(pnl, -1, img, (100, 400), (img.GetWidth(), img.GetHeight()))    # 假二维码
        self.word_more_1 = wx.StaticText(pnl, label='有关此问题的详细信息和可能的解决方法，请访问\nhttps://www.microsoft.com/', pos=(325, 405))
        self.word_more_2 = wx.StaticText(pnl, label=f'如果致电支持人员，请向他们提供以下信息：\n终止代码：unknown error\n失败的操作：explorer.exe', pos=(325, 485))

        # 事件
        pnl.Bind(wx.EVT_LEFT_DOWN, self.onClick)

        # 字体
        font_face = wx.Font(pointSize=81, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False,
                            faceName='Microsoft YaHei')
        font_contents = wx.Font(pointSize=25, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False,
                                faceName='Microsoft YaHei')
        font_more = wx.Font(pointSize=16, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False,
                            faceName='Microsoft YaHei')
        self.word_face.SetFont(font_face)
        self.word_contents_1.SetFont(font_contents)
        self.word_contents_2.SetFont(font_contents)
        self.word_more_1.SetFont(font_more)
        self.word_more_2.SetFont(font_more)

        # 颜色
        color_background = (0, 124, 224)
        color_contents = (255, 255, 255)
        pnl.SetBackgroundColour(color_background)
        self.word_face.SetForegroundColour(color_contents)
        self.word_contents_1.SetForegroundColour(color_contents)
        self.word_contents_2.SetForegroundColour(color_contents)
        self.word_more_1.SetForegroundColour(color_contents)
        self.word_more_2.SetForegroundColour(color_contents)

        self.ctrl_loading()


    def onClick(self, evt):
        # 改变文字
        self.word_face.SetLabel(':)')
        self.word_contents_1.SetLabel('你的设备遇到问题，机密即将泄露。\n我们只收集某些错误信息，然后为你启动自毁程序')
        self.word_more_1.SetLabel('有关此问题的详细信息和没什么用的解决方法，请访问\nhttps://xiejiancheng.github.io/')
        self.word_more_2.SetLabel('如果致电支持人员，那么你基本无法得到帮助(\n终止代码：your PC is not happy\n失败的操作：shutdown -s -t 0')

        # 改变关机状态
        self.stop_state = True
        wx.CallLater(3000, self.exitBSOD)

    def exitBSOD(self):
        blue_screen_win10.Close(self)


    def ctrl_loading(self):
        if shutdown_state is True and self.load_num >= 100:  # 关机条件：1、shutdown_state是True 2、百分比到了100
            self.shutdown()
        else:
            rand_load = random.randint(84, 98)
            if self.load_num >= rand_load and shutdown_state is False:  # 停止加载条件
                self.stop_state = True
            else:  # 否则继续加大数字
                rand_time = random.randint(5, 200)
                wx.CallLater(rand_time, self.ctrl_load)  # 这里和下面……

    def ctrl_load(self):
        self.load_num += 1
        self.word_contents_2.SetLabel(f'{self.load_num}%完成')

        if self.stop_state is False:
            self.ctrl_loading()  # ……这里和上面组成迭代

    @staticmethod
    def shutdown():
        os.system('shutdown -s -t 0')


def start_run():
    # 假蓝屏窗口
    app_blue = wx.App()

    frame_blue = blue_screen_win10(parent=None, id=-1)

    frame_blue.Show()
    # 运行到这里就会进入窗口循环
    app_blue.MainLoop()


if __name__ == '__main__':
    start_run()
# 这其实主要是为了教室电脑而打造的hhh
