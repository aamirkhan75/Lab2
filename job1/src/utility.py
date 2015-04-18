import logging

class Utility(object):

  def __init__(self, name, level):
    self.logger = logging.getLogger(name)
    self.logger.setLevel(level)

    self.stream = logging.StreamHandler()
    self.stream.setLevel(level)
    self.formatter = logging.Formatter('%(levelname)s: %(message)s')
    self.stream.setFormatter(self.formatter)
    self.logger.addHandler(self.stream)

  def set_level(self, level):
    self.logger.setLevel(level)
    self.stream.setLevel(level)

  def warning(self, message):
    self.logger.warning(message)

  def info(self, message):
    self.logger.info(message)
