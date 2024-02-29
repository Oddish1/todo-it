import wx
from modules.MainView import *

items = [['20240228', 'the task', 'is it done?', 'a tag', 1],
        ['20240227', 'another task', 'not done', 'tags', 2]]

if __name__ == '__main__':
  app = wx.App()
  MainFrame().Show()
  app.MainLoop()
