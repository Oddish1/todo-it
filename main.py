import wx
import wx.adv

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='ToDo It!')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        # date picker
        self.date_picker = wx.adv.DatePickerCtrl(panel,
                                                style=wx.adv.DP_DROPDOWN)
        my_sizer.Add(self.date_picker, 0, wx.ALL | wx.CENTER, 5)

        # text box
        self.text_ctrl = wx.TextCtrl(panel, value="Task Name", size=(250,30),
                                    style=wx.TE_PROCESS_ENTER)
        self.text_ctrl.SetForegroundColour(wx.LIGHT_GREY)
        self.text_ctrl.Bind(wx.EVT_SET_FOCUS, self.on_focus)
        self.text_ctrl.Bind(wx.EVT_KILL_FOCUS, self.on_focus_lost)
        self.text_ctrl.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.CENTER, 5)
        
        # button
        btn = wx.Button(panel, label='Create Task')
        btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)
        
        panel.SetSizer(my_sizer)
        self.Show()

    def on_focus(self, event):
        if self.text_ctrl.GetValue() == "Task Name":
            self.text_ctrl.Clear()
            self.text_ctrl.SetForegroundColour(wx.BLACK)

    def on_focus_lost(self,event):
        if self.text_ctrl.GetValue() == "":
            self.text_ctrl.SetValue("Task Name")
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


if __name__ == '__main__':
    # items stores [todo item date, todo item, priority, done boolean]
    items = []
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
