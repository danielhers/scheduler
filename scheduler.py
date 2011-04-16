# import DateTime class
#import wx.DateTime

# A class describing a person, with schedule preferences and assignments
class Person:

  def __init__(self):
    self.unavailableDates = []

  def addUnavailableDate(self, date):
    self.unavailableDates.append(date)
    print date
