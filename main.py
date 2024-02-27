import wx
import wx.adv


class TaskPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # define sizers to be used
        task_main_sizer = wx.BoxSizer(wx.VERTICAL)
        add_task_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # date picker
        self.date_picker = wx.adv.DatePickerCtrl(self,
                                                style=wx.adv.DP_DROPDOWN)
        add_task_sizer.Add(self.date_picker, 0, wx.ALL, 5)

        # text box
        self.text_ctrl = wx.TextCtrl(self, value="Task Name", size=(250,30),
                                    style=wx.TE_PROCESS_ENTER, name="Task Name")
        self.text_ctrl.SetForegroundColour(wx.LIGHT_GREY)
        self.text_ctrl.Bind(wx.EVT_SET_FOCUS, self.on_focus)
        self.text_ctrl.Bind(wx.EVT_KILL_FOCUS, self.on_focus_lost)
        self.text_ctrl.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        add_task_sizer.Add(self.text_ctrl, 0, wx.ALL, 5)
        
        # button
        btn = wx.Button(self, label='Create Task')
        btn.Bind(wx.EVT_BUTTON, self.on_press)
        add_task_sizer.Add(btn, 0, wx.ALL, 5)
        
        # add horizontal add task sizer to main sizer
        task_main_sizer.Add(add_task_sizer, wx.ALIGN_CENTER_HORIZONTAL)
        
        # set the panel sizer
        self.SetSizer(task_main_sizer)

    def on_focus(self, event):
        if self.text_ctrl.GetValue() == self.text_ctrl.GetName():
            self.text_ctrl.Clear()
            self.text_ctrl.SetForegroundColour(wx.BLACK)

    def on_focus_lost(self, event):
        if self.text_ctrl.GetValue() == "":
            self.text_ctrl.SetValue(self.text_ctrl.GetName())
            self.text_ctrl.SetForegroundColour(wx.LIGHT_GREY)

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        date = self.date_picker.GetValue()
        self.text_ctrl.SetValue("")
        if (value and date):
            # automatically sets priority to order items are added in and sets
            # done-state boolean to False
            items.append([date, value.strip(), len(items), False])
            print(f'Items: {items}')

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


if __name__ == '__main__':
    # items stores [todo item date, todo item, priority, done boolean]
    items = []
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
