import math

latency = 20 #ms

def distance(loc1, loc2):
  x = abs(loc1[0] - loc2[0])
  y = abs(loc1[1] - loc2[1])

  return math.sqrt((x ** 2) + ((y ** 2)))

def compare(city, hard_drive, size, location, car):
  if type(city).__name__ == 'list': # its a route
    return route_compare(city, hard_drive, size, location, car)

  size_nbr = int(size)
  trips = ((size_nbr // hard_drive.size) * 2) + 1

  city_time = (size_nbr * 8000) / city.speed
  drive_time = ((trips * distance(city.location, location)) / car) * 60 * 60

  return {
    'city_time': city_time,
    'drive_time': drive_time + (size_nbr / (1.0 * hard_drive.speed / 8000))
  }

def route_compare(route, hard_drive, size, location, car):
  total_distance = 0
  average_speed = 0.0
  size_nbr = int(size)

  for index, city in enumerate(route):
    if index + 1 == len(route):
      continue
    begin = city
    end = route[index + 1]
    total_distance += distance(begin.location, end.location)

  for index, city in enumerate(route):
    if index + 1 == len(route):
      continue
    begin = city
    end = route[index + 1]
    dist = distance(begin.location, end.location)
    average_speed += ((abs(begin.speed - end.speed) / 2) * (dist / total_distance))

  trips = ((size_nbr // hard_drive.size) * 2) + 1

  city_time = ((1.0 * size_nbr) / (average_speed / 8000)) * ((1.0 * latency) / 1000)
  drive_time = ((trips * total_distance) / car) * 60 * 60

  return {
    'city_time': city_time,
    'drive_time': drive_time + (size_nbr / (1.0 * hard_drive.speed / 8000))
  }
