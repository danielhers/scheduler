#!/usr/bin/python

# import the wxPython GUI package
import wx
import wx.calendar

# import project packages
import scheduler

people = []

# Create a new frame class, derived from the wxPython Frame.
class MyFrame(wx.Frame):

    def __init__(self, parent, id, title):
        # First, call the base class' __init__ method to create the frame
        wx.Frame.__init__(self, parent, id, title)

        # Add a panel and some controls to display and add people
        panel = wx.Panel(self, -1)
        label1 = wx.StaticText(panel, -1, "Add person:")
        label2 = wx.StaticText(panel, -1, "People:")
        self.addPersonCtrl = wx.TextCtrl(panel, -1, "",
            style=wx.TE_PROCESS_ENTER)
        self.peopleCtrl = wx.ListBox(panel, -1,
            style=wx.LB_EXTENDED,
            size=wx.Size(120,200))
        self.removeCtrl = wx.Button(panel, -1, "Remove")
        self.selectAllCtrl = wx.Button(panel, -1, "Select All")
        self.selectNoneCtrl = wx.Button(panel, -1, "Select None")
        self.setUnavailableCtrl = wx.Button(panel, -1, "Set Unavailable")
        self.calCtrl = wx.calendar.CalendarCtrl(panel, -1)
        self.panel = panel

        # Use some sizers for layout of the widgets
        peopleSizer = wx.FlexGridSizer(5, 2, 5, 5)
        peopleSizer.Add(label1)
        peopleSizer.Add(self.addPersonCtrl, 1, wx.EXPAND)
        peopleSizer.Add(label2)
        peopleSizer.Add(self.peopleCtrl, 1, wx.EXPAND)
        peopleSizer.AddSpacer(1)
        peopleSizer.Add(self.removeCtrl, 1, wx.EXPAND)
        peopleSizer.AddSpacer(1)
        peopleSizer.Add(self.selectAllCtrl, 1, wx.EXPAND)
        peopleSizer.AddSpacer(1)
        peopleSizer.Add(self.selectNoneCtrl, 1, wx.EXPAND)

        calSizer = wx.FlexGridSizer(2, 1, 5, 5)
        calSizer.Add(self.calCtrl)
        calSizer.Add(self.setUnavailableCtrl)

        border = wx.FlexGridSizer(1,2,10,10)
        border.Add(peopleSizer, 1, wx.ALIGN_LEFT | wx.ALIGN_CENTRE_VERTICAL | wx.ALL, 5)
        border.Add(calSizer, 1, wx.ALIGN_RIGHT | wx.ALIGN_CENTRE_VERTICAL | wx.ALL, 5)
        panel.SetSizerAndFit(border)
        self.Fit()

        self.addPersonCtrl.SetFocus()

        # Events
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterPerson, self.addPersonCtrl)
        self.Bind(wx.EVT_BUTTON, self.OnRemove, self.removeCtrl)
        self.Bind(wx.EVT_BUTTON, self.OnSelectAll, self.selectAllCtrl)
        self.Bind(wx.EVT_BUTTON, self.OnSelectNone, self.selectNoneCtrl)
        self.Bind(wx.EVT_BUTTON, self.OnAddUnavailable, self.setUnavailableCtrl)

    # This method is called when enter is pressed when in the Add Person box:
    def OnEnterPerson(self, event):
      self.peopleCtrl.Insert(event.GetString(), 0)
      self.addPersonCtrl.Clear()
      people.append(scheduler.Person())
      print "added %s. now there are %d people." % \
        (event.GetString(), self.peopleCtrl.GetCount())
    def OnRemove(self, event):
      while self.peopleCtrl.GetSelections():
        self.peopleCtrl.Delete(self.peopleCtrl.GetSelections()[0])
    def OnSelectAll(self, event):
      for item in range(self.peopleCtrl.GetCount()):
        self.peopleCtrl.SetSelection(item)
    def OnSelectNone(self, event):
      for item in range(self.peopleCtrl.GetCount()):
        self.peopleCtrl.Deselect(item)
    def OnAddUnavailable(self, event):
      for item in self.peopleCtrl.GetSelections():
        people[item].addUnavailableDate(self.calCtrl.GetDate())




# Every wxWidgets application must have a class derived from wx.App
class MyApp(wx.App):

    # wxWindows calls this method to initialize the application
    def OnInit(self):

        # Create an instance of our customized Frame class
        frame = MyFrame(None, -1, "Scheduler")
        frame.Show(True)

        # Tell wxWindows that this is our main window
        self.SetTopWindow(frame)

        # Return a success flag
        return True



app = MyApp(0)     # Create an instance of the application class
app.MainLoop()     # Tell it to start processing events
