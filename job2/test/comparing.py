from behave import *

@given ("estimated speed such as 100 mb per sec")

def step_impl(context):
  context.estimated_speeds = 110


@when ("network is faster than 100 mb per sec")

def step_imp(context):
  context.network_speed = 150
  

@then ("network is faster")

def step_imp(context):
  assert context.network_speed > context.estimated_speeds

@given ("estimated speed such as 100 miles per hour")  

def step_imp(context):
  context.estimated_speeds = 110

@when ("driving is faster than 100 miles per hour")

def step_imp(context):

  context.driving_speed = 160

@then ("driving is faster")

def step_imp(context):
  assert context.driving_speed > context.estimated_speeds

@given ("previous hard drive was 500 gb")

def step_impl(context):

  context.harddrive_size = 500

@when ("previous hard drive exceed 400 gb")

def step_impl(context):  
  context.hard_drive_usage = 400

@then ("increase hard drive size to 1000 gb")

def step_impl(context):
  if (context.hard_drive_usage >= 400):
     context.harddrive_size = 2 * context.harddrive_size
  assert context.harddrive_size == 1000    