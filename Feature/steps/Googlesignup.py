from behave import *

use_step_matcher("re")


@given('User is on Register page to signup with google')
def step_impl(context):
   print(u'STEP: Given User is on Register page to signup with google')


@when('User clicks Google button in the Sign Up with your Email form')
def step_impl(context):
    print(u'STEP: When  User clicks Google button in the Sign Up with your Email form')


@then('User successfully login with Google account')
def step_impl(context):
    print(u'STEP: Then User successfully login with Google account')