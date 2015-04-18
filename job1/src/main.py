import logging

from utility import *
from castle import *
from orc import *

command = raw_input ("Enter a command: ")
castle = Castle ([0,0]) #creating a castle
orcs = []        # setting up the types of orcs for job1.
orcs.append(Orc ([100,100]))
orcs.append(Orc ([100,100]))

utility = Utility('main', logging.DEBUG)

def print_board():
  for orc in orcs:
    utility.info(castle.orc_distance(orc))
    utility.info(orc.speed)

def unit_Conversation(current_unit,target_unit,current_unit_value):
  if current_unit == "meter" and target_unit == "feet":
    return current_unit_value * 3

while command != "X":
  if command == "print":
    print_board()
  command = raw_input("Enter another command: ")




#need to follow the example of random inside the orc class. 



#  this method is going to print status of the board. it will print out all the location of orcs and castle.