import wx
import wx.adv
from main import items

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
    task_main_sizer.Add(add_task_sizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

    # task list
    self.col_names = ['Date', 'Task', 'Done', 'Tags']
    self.task_display_list = wx.ListCtrl(self, style=wx.LC_REPORT)
    for i in range(4):
        self.task_display_list.InsertColumn(i, self.col_names[i])
    task_main_sizer.Add(self.task_display_list, 1, wx.EXPAND | wx.ALL, 5)

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
