import wx
from modules.TaskPage import *

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="ToDo It!", size=(1200, 800))

        # create the panel and the notebook
        panel = wx.Panel(self)
        self.notebook = wx.Notebook(panel)

        # create page windows as notebook children
        task_page = TaskPage(self.notebook)
        #TODO timer_page = TimerPage(self.notebook)
        #TODO habit_page = HabitPage(self.notebook)
        #TODO statistics_page = StatisticsPage(self.notebook)

        # add pages to the notebook with labels
        self.notebook.AddPage(task_page, "Tasks")
        #TODO self.notebook.AddPage(timer_page, "Timer")
        #TODO self.notebook.AddPage(habit_page, "Habits")
        #TODO self.notebook.AddPage(statistcs_page, "Stats")

        # put notebook in a sizer
        sizer = wx.BoxSizer()
        sizer.Add(self.notebook, 1, wx.EXPAND)
        panel.SetSizer(sizer)

