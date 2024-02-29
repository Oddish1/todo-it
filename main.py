import wx
from modules.MainView import *

items = [['date of task', 'the task', 'is it done?', 'a tag'],
        ['another date', 'another task', 'not done', 'tags']]

if __name__ == '__main__':
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
