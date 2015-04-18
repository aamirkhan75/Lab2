import unittest 
from ..src.castle import *
from ..src.orc import *

class CastleTest(unittest.TestCase):

  def test_castle_safe(self):
    castle = Castle([0, 0])
    orc    = Orc([100, 100])

    message = castle.check_orcs([orc])
    self.assertEqual(message,None)

  def test_castle_warning(self):
    castle = Castle ([0,0])
    orc    = Orc ([0,14])

    message = castle.check_orcs([orc])
    self.assertEqual(message,"warning")

  def test_castle_breach(self):
    castle = Castle([0,0])
    orc    = Orc([0,10])

    message = castle.check_orcs ([orc])
    self.assertEqual(message,"breach")

if __name__ == '__main__':
    unittest.main()
