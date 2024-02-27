import wx
from modules.MainView import *

if __name__ == '__main__':
    # items stores [todo item date, todo item, priority, done boolean]
    items = []
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
