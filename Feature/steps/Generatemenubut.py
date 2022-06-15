from behave import *

use_step_matcher("re")


@given('User is logged on to Dietician website')
def step_impl(context):
    print('STEP: Given User is logged on to Dietician website')


@when('User lands on Confirm conditions and Create Plan page')
def step_impl(context):
    print('STEP: When User lands on Confirm conditions and Create Plan page')


@then('User should see a button with text GENERATE MENU  at the bottom of the page')
def step_impl(context):
    print('STEP: Then User should see a button with text GENERATE MENU  at the bottom of the page')


@given('User is on create plan page to click on menu button')
def step_impl(context):
    print('STEP: Given User is on create plan page to click on menu button')


@when('User clicks the GENERATE MENU button')
def step_impl(context):
    print('STEP: When User clicks the GENERATE MENU button')


@then('New Diet plan should be generated with the latest confirmed Health conditions')
def step_impl(context):
    print('STEP: Then New Diet plan should be generated with the latest confirmed Health conditions')


@given('User is on create plan page to click on menu button to land on view recent diets page')
def step_impl(context):
    print('STEP: Given User is on create plan page to click on menu button to land on view recent diets page')


@when('User clicks the GENERATE MENU button to land on view recent diets page')
def step_impl(context):
    print('STEP: When User clicks the GENERATE MENU button to land on view recent diets page')


@then('User should land on View Recent Diets page')
def step_impl(context):
   print('STEP: Then User should land on View Recent Diets page')
