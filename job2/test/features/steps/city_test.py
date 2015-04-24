from behave import given, when, then

import sys
sys.path.append('job2/src')

from calculator import *

from city import *

from harddrive import *

city      = City("portland", 500, [0, 0])
harddrive = Harddrive(10, 100)
car       = 1

@given('The size "{x}", location ["{y}", "{z}"]')
def step_impl(context, x, y, z):
    context.size = int(x)
    context.location = [int(y), int(z)]

@when('comparing the driving speed and downloading speed')
def step_impl(context):
    context.comparison = compare(city, harddrive, context.size, context.location, car )

    

@then('It should give "{city_result}" and "{drive_result}"')
def step_impl(context, city_result, drive_result):
    assert context.comparison["city_time"] == int(city_result)
    assert context.comparison["drive_time"] == float(drive_result)
   




# from behave import given, when, then

# @given('we have behave installed')
# def step_impl(context):
#     pass

# @when('we implement a test')
# def step_impl(context):
#     assert True is not False

# @then('behave will test it for us!')
# def step_impl(context):
#     assert context.failed is False
