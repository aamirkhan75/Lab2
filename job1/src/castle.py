import math

class Castle(object):

  def __init__(self, location): # addes width in constructor
    self.location = location
    self.warning_distance = 15
    self.breach_distance =  10
    #setting up the width of the castle

  def orc_distance(self, orc):
    x = abs(self.location[0] - orc.location[0])
    y = abs(self.location[1] - orc.location[1])

    return math.sqrt((x ** 2) + ((y ** 2)))
    # need to try to write fucntion for orc velocity and deploy defecne fucntion

  def deploy_defence(self):
    return

  def check_orcs(self, orcs):
    #return True
    for orc in orcs:
      distance = self.orc_distance(orc)
      if distance <= self.breach_distance:
        return "breach"
      elif distance <= self.warning_distance:
        return "warning"
