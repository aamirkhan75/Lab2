from behave import *

@given ("average network speed = 15 mg")
def step_impl(context):
  context.average_network_speed = 15

@when ("network is greater than 30 mg")
def step_impl(context):
  context.network_speed =20

@then ("network is faster")  
def step_impl(context):
   if (context.network_speed > context.average_network_speed)
     assert

@given ("average hard drive speed is 7200 rpm")
def step_impl(context):
  context.average_harddrive_speed = 7200

@when ("hard drive speed is 8000")
def step_impl(context):
  context.harddrive_speed = 8000  

@then ("The hard drive is faster")
def step_impl(context):
  assert context.harddrive_speed > context.average_harddrive_speed  
