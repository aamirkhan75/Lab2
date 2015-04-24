from locatable import *

class City(Locatable):
  def __init__(self, name, speed, location):
    self.name = name
    self.speed = speed
    self.location = location
