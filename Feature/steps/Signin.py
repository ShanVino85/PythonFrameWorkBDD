from behave import *

use_step_matcher("re")


@given('user is on dietition website to validate sign in page')
def step_impl(context):
    print('STEP: Given user is on dietition website to validate sign in page')


@when('user click on icon symbol on sign in page')
def step_impl(context):
   print('STEP: When user click on icon symbol on sign in page')


@then('user should see the title of the page signIn')
def step_impl(context):
   print('STEP: Then user should see the title of the page signIn')


@given('user is on dietition website to test mandatory fields on sign in page')
def step_impl(context):
    print('STEP: Given user is on dietition website to test mandatory fields on sign in page')


@when('user is  on sign in page to test mandatory fields')
def step_impl(context):
   print('STEP: When user is  on sign in page to test mandatory fields')


@then('User should see all mandatory fields with star symbol on top of those fields in sign in page')
def step_impl(context):
    print('STEP: Then User should see all mandatory fields with star symbol on top of those fields in sign in page')