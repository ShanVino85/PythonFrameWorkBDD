from behave import *

use_step_matcher("re")


@given('User is logged on to Dietician website for menu bar')
def step_impl(context):
    print('STEP: Given User is logged on to Dietician website for menu bar')


@when('User lands on Diet Plans page for menu bar')
def step_impl(context):
    print('STEP: When User lands on Diet Plans page for menu bar')


@then('User should see that Diet Plans tab on the menu bar is selected')
def step_impl(context):
   print('STEP: Then User should see that Diet Plans tab on the menu bar is selected')