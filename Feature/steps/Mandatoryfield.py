from behave import *

use_step_matcher("re")


@given('User is on Dietician website page')
def step_impl(context):
   print('STEP: Given User is on Dietician website page')


@when('User lands on Register page on Dietician website')
def step_impl(context):
    print('STEP: When User lands on Register page on Dietician website')


@then('User should see all mandatory flields with star symbol on top of those fields')
def step_impl(context):
    print('STEP: Then User should see all mandatory flields with star symbol on top of those fields')