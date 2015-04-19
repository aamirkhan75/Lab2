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

  def test_convert_imperial(self):
    castle = Castle([0,0])         
    self.assertEqual( 3.28084 * 2, castle.convert(2, "imperial")) 

  def test_convert_parsec(self):
    castle = Castle([0,0])         
    self.assertEqual( 0.032408 * 2, castle.convert(2, "parsec")) 

  def test_convert_nautical(self):        
    castle = Castle([0,0])         
    self.assertEqual( 0.00053996 * 2, castle.convert(2, "nautical")) 
    
  def test_convert_metric(self):
    castle = Castle([0,0])         
    self.assertEqual( 2, castle.convert(2, "metric"))         


if __name__ == '__main__':
    unittest.main()
