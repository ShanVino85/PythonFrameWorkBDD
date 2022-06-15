from behave import *

use_step_matcher("re")


@given('User is on Dietician website')
def step_impl(context):
   print('STEP: Given User is on Dietician website')


@when('User lands on Register page')
def step_impl(context):
    print('STEP: When User lands on Register page')


@then('User should see the title of page as Register')
def step_impl(context):
   print('STEP: Then User should see the title of page as Register')