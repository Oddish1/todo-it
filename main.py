import wx
from modules.MainView import *

items = [['20240228', 'the task', False, ['a tag'], 1],
        ['20240227', 'another task', False, ['tags', 'b tag', 'a tag'], 2]]

if __name__ == '__main__':
  app = wx.App()
  MainFrame().Show()
  app.MainLoop()
