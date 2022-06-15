from behave import *

use_step_matcher("re")


@given('User is on Register page to signup with facebook')
def step_impl(context):
    print('STEP: Given User is on Register page to signup with facebook')


@when('User clicks Facebook button in the Sign Up with your Email form')
def step_impl(context):
    print('STEP: When User clicks Facebook button in the Sign Up with your Email form')


@then('User successfully login with Facebook account')
def step_impl(context):
   print('STEP: Then User successfully login with Facebook account')