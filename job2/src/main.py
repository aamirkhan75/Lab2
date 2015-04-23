import math

from city import *
from harddrive import *
from calculator import *


help = """
usage: <command> <...params>

       command: | print   => print cities, location, and connetion speed from the file
                | compare => compare driving and route for a city or route for some filesize (GB)
                | set     => sets which sized (GB) hard drive is being used
                | create  => creates a new city with a location (x and y) and a speed (mbps)
                | drive   => set the current car (Porsche, Bus, CementTruck, LadenSwallow)
                | route   => creates a route of cities
                | ?       => display this message
                | X       => quit the game
"""

cities = []
routes = []
location = [0, 0]

car = 'Bus'

cars = {
  'Porsche': 200,
  'Bus': 110,
  'Cement Truck': 100,
  'LadenSwallow': 60
}

with open('./job2/src/data.txt') as f:
  for line in f.readlines():
    data = line.strip().split(',')
    cities.append(City(data[0], int(data[1]), [int(data[2]), int(data[3])]))

hard_drive = Harddrive(500, 100) # 500GB

def print_game():
  print '------------------------------------------'
  print 'current drive: %d GB' % (hard_drive.size)
  print 'current car:   ' + car
  print '------------------------------------------'
  print '\nCities:'
  for city in cities:
    print 'city name: ' + city.name
    print 'speed:     %d mbps' % city.speed
    print 'location:  [%d, %d]' % (city.location[0], city.location[1])
    print 'distance:  %d km\n' % distance(city.location, location)
  print '\nRoutes:'
  for index, route in enumerate(routes):
    print '%d:' % index
    for city in route:
      print '  | ' + city.name
    print '\n'

def city_or_route_by_name(name):
  try:
    id = int(name)
    return routes[id]

  except ValueError:
    for city in cities:
      if name == city.name:
        return city

def write_city_file(city):
  f = open('./' + city.name + '.city','w')
  f.write(city.name + ', %d, %d, %d' % (city.speed, city.location[0], city.location[1]))
  f.close()

def parse_input(input):
  return input.split()

location = city_or_route_by_name('GrantsPass').location

print """
  Welcome to the network research tool

  Available cities are:

                | GrantsPass (Default)
                | SanFrancisco
                | Portland
                | NewYork
                | LosAngeles
                | Detroit
                | SanAntonio
                | Memphis
                | Chicago
                | Philadelphia
"""
commands = parse_input(raw_input("Please enter you city: "))

if len(commands) == 0:
  commands = ["empty"]

input_city = city_or_route_by_name(commands[0])
if input_city:
  location = input_city.location
else:
  print "We could not find that city, defaulting to GrantsPass"

while commands[0] != "X":
  command = commands[0]
  arguments = commands[1:len(commands)]

  if command == "print":
    print_game()
  elif command == "?":
    print help
  elif command == "compare":
    results = compare(city_or_route_by_name(arguments[0]), hard_drive, arguments[1], location, cars[car])
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
  elif command == "create":
    new_city = City(arguments[0], int(arguments[1]), int(arguments[2]))
    write_city_file(new_city)
    cities.append(new_city)
  elif command == "drive":
    car_in = arguments[0]
    if car_in in cars:
      car = car_in
    else:
      print 'Car not found.'
  elif command == "route":
    route = []
    for city in arguments:
      for city_obj in cities:
        if city == city_obj.name:
          route.append(city_obj)
    if len(route) > 0:
      routes.append(route)
    else:
      print "No valid cities detected."
  commands = parse_input(raw_input("Enter a command: "))
  if len(commands) == 0:
    commands = ["empty"]
