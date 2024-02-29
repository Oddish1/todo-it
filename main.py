import wx
from modules.MainView import *

items = [['date of task', 'the task', 'is it done?', 'a tag', 1],
        ['another date', 'another task', 'not done', 'tags', 2]]

if __name__ == '__main__':
  app = wx.App()
  MainFrame().Show()
  app.MainLoop()
