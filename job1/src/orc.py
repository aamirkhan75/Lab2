import random
 
class Orc(object):
  def __init__(self, location):  # addes orc type to the constructor
    self.location = location
    self.speed = random.randint(1, 5)
