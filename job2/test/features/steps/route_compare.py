from behave import given, when, then

import sys
sys.path.append('job2/src')

from calculator import *

from city import *

from harddrive import *



city      = [City("portland", 100, [0, 0]), City("seattle", 200, [0, 25])]
harddrive = Harddrive(10, 100)
car       = 10

@given('I have size "{a}", location ["{b}", "{c}"] for route')
def step_impl(context, a, b, c):
    context.size = int(a)
    context.location = [int(b), int(c)]

@when('I compare driving speed and downloading speed for route')
def step_impl(context):
    context.comparison = compare(city, harddrive, context.size, context.location, car )

@then('It should give us "{city_result}" and "{drive_result}" for route')
def step_impl(context, city_result, drive_result):
    assert context.comparison["city_time"] == float(city_result)
    assert context.comparison["drive_time"] == float(drive_result)