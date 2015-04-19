import random

class Orc(object):
  def __init__(self, location, type ='Strongman'):
    self.location = location
    self.type = type
    self.priority = 'low'
    self.speed = random.randint(1, 5)

  def id(self):
    return id(self)
