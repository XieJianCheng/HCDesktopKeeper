# coding: utf-8

# 去年五一，我写了个破坏性质的UDkeeper
# 嗯……今年写点实用的东西了

# 六班通，是陪伴了我整个编程之路的项目
# 刚入门时，仿制了个六班通1.0
# 刚开始写算法时，翻新了个六班通4.0
# 那个项目真的是非常庞大复杂，将近2k行代码，至今我仍为之感到佩服
# 而现在，我也从学习阶段进入了实用项目阶段
# 那么，就让六班通5.0开始这个时代吧!

# 开始时间: 2023.4.29 14:08

import wx

from random import randint
import os
import datetime

from mod import launcher, BSOD

version = 'v1.0'


def getTimer():
    # 读取当前时间
    time = datetime.datetime.now()
    today = f'{time.year}-{time.month}-{time.day}'

    # 读取计时器文件
    with open('data/timer.txt', 'r', encoding='utf-8') as fo_r:
        read = fo_r.readlines()
        yesterday = read[0].strip().split(' ')[0]  # 上一次记录的时间
        total = int((read[0].strip().split(' ')[1]))  # 总天数
        past = int(read[0].strip().split(' ')[2])  # 过去了的天数

    # 如果今天和上次记录的不是同一天
    if yesterday != today:
        new_yesterday = today  # 改为今天
        new_past = past + 1  # 过去的天数+1
    else:  # 否则不变
        new_yesterday = yesterday
        new_past = past

    # 新的文件内容
    new_text = f'{new_yesterday} {total} {new_past}'
    with open('data/timer.txt', 'w+', encoding='utf-8') as fo_w:
        fo_w.write(new_text)

    # 计算剩余天数
    left = total - new_past
    return left


class mainWindow(wx.Frame):
    size = (500, 450)
    pos = (660, 280)
    title = f'HCDesktopKeeper-{version}'

    def __init__(self, parent=None, id=-1):
        wx.Frame.__init__(self, parent, id, self.title, size=self.size)
        self.Centre()
        self.pnl = wx.Panel(self)

        # 控件
        title_all = wx.StaticText(self.pnl, label=f'六班通-{version}')
        title_offset = wx.StaticText(self.pnl, label='(中考特供版)')
        timer = wx.StaticText(self.pnl, label=f'中考倒计时{getTimer()}天！')

        title_basic = wx.StaticText(self.pnl, label='基本功能')
        bt_random = wx.Button(self.pnl, label='随机抽号', size=(80, 30))
        bt_grade = wx.Button(self.pnl, label='每日荔枝', size=(80, 30))
        bt_get = wx.Button(self.pnl, label='计算科平', size=(80, 30))
        bt_exit = wx.Button(self.pnl, label='退出', size=(80, 30))
        self.output = wx.StaticText(self.pnl, label='输出内容')

        title_function = wx.StaticText(self.pnl, label='其他功能')
        bt_seewo = wx.Button(self.pnl, label='希沃白板', size=(100, 45))
        bt_wechat = wx.Button(self.pnl, label='打开微信', size=(100, 45))
        bt_wxfiler = wx.Button(self.pnl, label='文件传输助手', size=(100, 45))
        bt_saver = wx.Button(self.pnl, label='屏保', size=(100, 45))
        bt_bsod = wx.Button(self.pnl, label='蓝屏关机', size=(100, 45))
        bt_about = wx.Button(self.pnl, label='关于本软件', size=(100, 45))

        # 颜色
        timer.SetForegroundColour((255, 0, 0))

        # 绑定事件
        bt_random.Bind(wx.EVT_BUTTON, self.randomChoose)
        bt_grade.Bind(wx.EVT_BUTTON, self.randomGrade)
        bt_get.Bind(wx.EVT_BUTTON, self.getGrade)
        bt_exit.Bind(wx.EVT_BUTTON, self.exit)
        bt_seewo.Bind(wx.EVT_BUTTON, self.openSeewo)
        bt_wechat.Bind(wx.EVT_BUTTON, self.openWechat)
        bt_wxfiler.Bind(wx.EVT_BUTTON, self.openFiler)
        bt_saver.Bind(wx.EVT_BUTTON, self.saver)
        bt_bsod.Bind(wx.EVT_BUTTON, self.BSOD)
        bt_about.Bind(wx.EVT_BUTTON, self.showAbout)
        self.pnl.Bind(wx.EVT_LEFT_DOWN, self.changeBG)

        # 字体
        font_title = wx.Font(pointSize=32, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, underline=False,
                             faceName='SimHei')
        font_offset = wx.Font(pointSize=12, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL, underline=False,
                              faceName='SimHei')
        font_timer = wx.Font(pointSize=22, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL, underline=False,
                             faceName='STXinwei')
        font_tip = wx.Font(pointSize=17, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL, underline=False,
                           faceName='FZShuTi')
        font_output = wx.Font(pointSize=15, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL, underline=False,
                              faceName='STKaiti')
        title_all.SetFont(font_title)
        title_offset.SetFont(font_offset)
        timer.SetFont(font_timer)
        title_basic.SetFont(font_tip)
        title_function.SetFont(font_tip)
        self.output.SetFont(font_output)

        # 布局
        sizer_h_basic = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_basic.Add(bt_random, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)
        sizer_h_basic.Add(bt_grade, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)
        sizer_h_basic.Add(bt_get, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)
        sizer_h_basic.Add(bt_exit, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)

        sizer_h_function_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_function_1.Add(bt_seewo, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)
        sizer_h_function_1.Add(bt_wechat, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)
        sizer_h_function_1.Add(bt_wxfiler, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)
        sizer_h_function_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_function_2.Add(bt_saver, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)
        sizer_h_function_2.Add(bt_bsod, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)
        sizer_h_function_2.Add(bt_about, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=3)

        sizer_v_all = wx.BoxSizer(wx.VERTICAL)
        sizer_v_all.Add(title_all, proportion=1, flag=wx.ALIGN_CENTER | wx.TOP, border=20)
        sizer_v_all.Add(title_offset, proportion=1, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        sizer_v_all.Add(timer, proportion=1, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=8)
        sizer_v_all.Add(title_basic, proportion=1, flag=wx.ALIGN_LEFT | wx.LEFT, border=100)

        sizer_v_all.Add(sizer_h_basic, proportion=0, flag=wx.ALIGN_CENTER)

        sizer_v_all.Add(self.output, proportion=1, flag=wx.ALIGN_CENTER | wx.TOP, border=5)

        sizer_v_all.Add(title_function, proportion=0, flag=wx.ALIGN_LEFT | wx.LEFT, border=100)

        sizer_v_all.Add(sizer_h_function_1, proportion=1, flag=wx.ALIGN_CENTER)
        sizer_v_all.Add(sizer_h_function_2, proportion=1, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=20)

        # 应用sizer
        self.pnl.SetSizer(sizer_v_all)

        # 图标
        icon_path = 'data/HCDKeeper.ico'
        try:
            open(icon_path, 'rb')
        except FileNotFoundError:
            print('icon file not found')
        else:
            icon = wx.Icon(name=icon_path, type=wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon)

    def randomChoose(self, evt):
        rng = randint(1, 40)
        self.output.SetLabel(f'{rng}号')

    def randomGrade(self, evt):
        rng = randint(10, 250)
        self.output.SetLabel(f'我要荔枝考进前{rng}名！')

    @staticmethod
    def getGrade(evt):
        os.system(f'python "{os.getcwd()}\\mod\\getGrade.py"')

    @staticmethod
    def exit(evt):
        from sys import exit
        exit()

    @staticmethod
    def openSeewo(evt):
        launcher.open_seewo()

    @staticmethod
    def openWechat(evt):
        launcher.open_wechat()

    @staticmethod
    def openFiler(evt):
        launcher.open_filer()

    @staticmethod
    def saver(evt):
        import mod.saver

    @staticmethod
    def BSOD(evt):
        BSOD.start_run()

    @staticmethod
    def showAbout(evt):
        msg = """
        软件作者: 谢建城(HaroldHC)
        代码量: 约600行
        开发时间: 约4小时
        
        更新日志:
        v1.0
        第一个版本……彩蛋？"""
        wx.MessageBox(msg, 'sth to say')

    # 嗯……半成品，不想改了（
    def changeBG(self, evt):
        color_r = randint(0, 255)
        color_g = randint(0, 255)
        color_b = randint(0, 255)
        color = (color_r, color_g, color_b)
        print(color)
        self.SetBackgroundColour(color)


if __name__ == '__main__':
    app = wx.App()
    frame = mainWindow()
    frame.Show()
    app.MainLoop()
