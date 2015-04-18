import logging

from utility import *
from castle import *
from orc import *

help = """
usage: <command> <...params>

       command: | print                 => print status of the game
                | priority <id> <level> => set orc priority (low|medium|high)
                | ?                     => display this message
                | X                     => quit the game
"""

orc_types = ['Strongman',
             'Hunter',
             'Farmer',
             'Warrior',
             'Archer',
             'Healer',
             'Horseback Rider',
             'Knight']

unit = 'imperial' # metric | imperial | parsec | nautical

unit_map = {
  'metric':   ' meters',
  'imperial': ' feet',
  'parsec':   '*10^-15 parsecs',
  'nautical': ' nautical miles'
}

castle = Castle ([0,0]) #creating a castle
orcs = []

utility = Utility('main', logging.DEBUG)

def generate_orc():
  x = random.randint(50, 100)
  y = random.randint(50, 100)
  type = orc_types[random.randint(0, 7)]

  return Orc([x, y], type)

def print_board():
  for orc in orcs:
    utility.info('orc ID:       %d' % orc.id())
    utility.info('orc priority: ' + orc.priority)
    utility.info('distance:     %f' % castle.orc_distance(orc, unit) + unit_map[unit])
    utility.info('speed:        %d\n' % orc.speed)

def parse_input(input):
  return input.split()

def unit_Conversation(current_unit,target_unit,current_unit_value):
  if current_unit == "meter" and target_unit == "feet":
    return current_unit_value * 3

orcs.append(generate_orc())
orcs.append(generate_orc())
# orcs.append(generate_orc())
# orcs.append(generate_orc())
# orcs.append(generate_orc())

commands = parse_input(raw_input("Enter a command: "))

while commands[0] != "X":
  command = commands[0]
  arguments = commands[1:len(commands)]

  if command == "print":
    print_board()
  elif command == "?":
    print help
  elif command == "priority" and len(arguments) > 1:
    for orc in orcs:
      if orc.id() == int(arguments[0]):
        orc.priority = arguments[1]
        print "set priority of " + arguments[0] + " to " + arguments[1]
  commands = parse_input(raw_input("Enter another command: "))




#need to follow the example of random inside the orc class. 



#  this method is going to print status of the board. it will print out all the location of orcs and castle.