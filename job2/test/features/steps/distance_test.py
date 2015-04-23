from behave import given, when, then

import sys
sys.path.append('job2/src')

from calculator import *

@given('I have points ["{a}", "{b}"] and ["{c}", "{d}"]')
def step_impl(context, a, b, c, d):
    context.x = [int(a), int(b)]
    context.y = [int(c), int(d)]

@when('I calculate the distance between them')
def step_impl(context):
    context.distance = distance(context.x, context.y)

@then('It should equal "{hypotenuse}"')
def step_impl(context, hypotenuse):
    assert context.distance == int(hypotenuse)
