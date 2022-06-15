from behave import *

use_step_matcher("re")


@given('User is on Register page to click on Log In here link')
def step_impl(context):
    print(u'STEP: Given User is on Register page to click on Log In here link')


@when('User clicks Log in here link')
def step_impl(context):
    print(u'STEP: When User clicks Log in here link')


@then('User is re-directed to Sign In Page')
def step_impl(context):
    print(u'STEP: Then User is re-directed to Sign In Page')