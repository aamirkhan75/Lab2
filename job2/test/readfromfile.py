from behave import *
import os.path 

@given("There is no such file")

def step_impl(context):

  result = os.path.isfile('not existing file')
  assert context.failed is False
  

@given ("There is file exists and we read cities, distance and connection")

def step_impl(context):
  f = open ('data.txt','r+')
  str1 = f.readline()
  assertEqual('Grants pass    400      100')





   


