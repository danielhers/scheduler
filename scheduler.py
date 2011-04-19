# import DateTime class
#import wx.DateTime

# A class describing a person, with schedule preferences and assignments
class Person:

  def __init__(self, name):
    self.name = name
    self.unavailableDates = set()
