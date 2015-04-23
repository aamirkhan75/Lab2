from city import *
from harddrive import *


help = """
usage: <command> <...params>

       command: | print   => print cities, distance, and connetion speed from the file
                | compare => compare download and hard drive speed for file of some size (GB)
                | set     => sets which sized (GB) hard drive is being used
                | create  => creates a new city with a distance (km) and a speed (mbps)
                | drive   => set the current car (Porsche, Bus, CementTruck, LadenSwallow)
                | ?       => display this message
                | X       => quit the game
"""

cities = []

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
    cities.append(City(data[0], int(data[1]), int(data[2])))

hard_drive = Harddrive(50, 1000)

def print_game():
  print '------------------------------------------'
  print 'current drive: %d GB' % (hard_drive.size)
  print 'current car:   ' + car
  print '------------------------------------------'
  for city in cities:
    print 'city name: ' + city.name
    print 'speed:     %d mbps' % city.speed
    print 'distance:  %d km\n' % city.distance

def city_by_name(name):
  for city in cities:
    if name == city.name:
      return city

def compare(city, size):
  city_obj = city_by_name(city)
  size_nbr = int(size)
  trips = ((size_nbr // hard_drive.size) * 2) + 1

  city_time = (size_nbr * 8000) / city_obj.speed
  drive_time = ((trips * city_obj.distance) / cars[car]) * 60 * 60

  return {
    'city_time': city_time,
    'drive_time': drive_time
  }

def write_city_file(city):
  f = open('./' + city.name + '.city','w')
  f.write(city.name + ', %d, %d' % (city.speed, city.distance))
  f.close()

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
    results = compare(arguments[0], arguments[1])
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
  commands = parse_input(raw_input("Enter a command: "))
