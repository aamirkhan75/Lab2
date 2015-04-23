from behave import given, when, then

import sys
sys.path.append('job2/src')

from calculator import *

from city import *

from harddrive import *



city      = City("portland", 500, [0, 0])
harddrive = Harddrive(10, 100)
car       = 10

@given('I have size "{a}", location ["{b}", "{c}"]')
def step_impl(context, a, b, c):
    context.size = int(a)
    context.location = [int(b), int(c)]

@when('I compare driving speed and downloading speed')
def step_impl(context):
    context.comparison = compare(city, harddrive, context.size, context.location, car )

@then('It should give us "{city_result}" and "{drive_result}"')
def step_impl(context, city_result, drive_result):
    assert context.comparison["city_time"] == int(city_result)
    assert context.comparison["drive_time"] == float(drive_result)
