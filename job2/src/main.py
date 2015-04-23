from city import *
from harddrive import *


help = """
usage: <command> <...params>

       command: | print   => print cities, distance, and connetion speed from the file
                | compare => compare download and hard drive speed for file of some size (GB)
                | set     => sets which sized (GB) hard drive is being used
                | ?       => display this message
                | X       => quit the game
"""

cities = []

with open('./job2/src/data.txt') as f:
  for line in f.readlines():
    data = line.strip().split(',')
    cities.append(City(data[0], int(data[1]), int(data[2])))

hard_drive = Harddrive(50, 1000)

def print_game():
  print '------------------------------------------'
  print 'current drive: %d GB, %d mbps' % (hard_drive.size, hard_drive.speed)
  print '------------------------------------------'
  for city in cities:
    print 'city name: ' + city.name
    print 'speed:     %d mbps' % city.speed
    print 'distance:  %d km\n' % city.distance

def city_by_name(name):
  for city in cities:
    if name == city.name:
      return city

def compare(city, size, distance):
  city_obj = city_by_name(city)
  size_nbr = int(size)
  dist_nbr = int(distance)

  city_time = (size_nbr * 8000) / city_obj.speed
  drive_time = (size_nbr * 8000) / hard_drive.speed

  return {
    'city_time': city_time,
    'drive_time': drive_time
  }

def parse_input(input):
  return input.split()

commands = parse_input(raw_input("Enter a command: "))

while commands[0] != "X":
  command = commands[0]
  arguments = commands[1:len(commands)]

  if command == "print":
    print_game()
  elif command == "?":
    print help
  elif command == "compare":
    results = compare(arguments[0], arguments[1], arguments[2])
    print "Network Time:    %d s" % results['city_time']
    print "Hard Drive Time: %d s" % results['drive_time']
    if results['city_time'] < results['drive_time']:
      print 'Network is better by %d s\n' % (int(results['drive_time']) - int(results['city_time']))
    elif results['city_time'] > results['drive_time']:
      print 'Hard Drive is better by %d s\n' % (int(results['city_time']) - int(results['drive_time']))
    else:
      print 'Tie.\n'
  elif command == "set":
    hard_drive = Harddrive(int(arguments[0]), int(arguments[1]))
  commands = parse_input(raw_input("Enter a command: "))
