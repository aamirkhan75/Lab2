import math

class Castle(object):

  def __init__(self, location): # addes width in constructor
    self.location = location
    self.warning_distance = 15
    self.breach_distance =  10
    #setting up the width of the castle

  def orc_distance(self, orc, unit='metric'):
    x = abs(self.location[0] - orc.location[0])
    y = abs(self.location[1] - orc.location[1])

    return self.convert(math.sqrt((x ** 2) + ((y ** 2))), unit)
    # need to try to write fucntion for orc velocity and deploy defecne fucntion

  def convert(self, metric_distance, unit):
    if unit == 'imperial':
      return metric_distance * 3.28084
    elif unit == 'parsec':
      return metric_distance * 0.032408 # x 10^-15
    elif unit == 'nautical':
      return metric_distance * 0.00053996
    else:
      return metric_distance

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
