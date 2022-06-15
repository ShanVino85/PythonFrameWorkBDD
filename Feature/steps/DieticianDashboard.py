from behave import *

use_step_matcher("re")


@given("Dietitian logged in successfully to the Dietitian website")
def step_impl(context):
   print('STEP: Given Dietitian logged in successfully to the Dietitian website')

@when('Dietitian verifes Dashboard Left Side Bar')
def step_impl(context):
    print('STEP: When Dietitian verifes Dashboard Left Side Bar')


@then('User can see Upcoming Events section in left side bar')
def step_impl(context):
    print('STEP: Then User can see Upcoming Events section in left side bar')


@when('Dietitian Verifies Upcoming Event Items')
def step_impl(context):
    print('STEP: When Dietitian Verifies Upcoming Event Items')


@then('Dietitian can see the Items of  Upcoming Events section in left side bar')
def step_impl(context):
    print('STEP: Then Dietitian can see the Items of  Upcoming Events section in left side bar')


@when('Dietitian verifies Dashboard Top Right Side Bar')
def step_impl(context):
    print('STEP: When Dietitian verifies Dashboard Top Right Side Bar')


@then('User can see Banner or Announcements section in top right side bar')
def step_impl(context):
    print('STEP: Then User can see Banner or Announcements section in top right side bar')


@when('Dietitian verifies Dashboard Bottom Right Side Bar')
def step_impl(context):
    print('STEP: When Dietitian verifies Dashboard Bottom Right Side Bar')


@then('Dietitian can see the ratio graph of enrolled patients  in bottom right side bar Recovery rate')
def step_impl(context):
    print('STEP: Then Dietitian can see the ratio graph of enrolled patients  in bottom right side bar Recovery rate')


@when('Dietitian Verifies Total Patient')
def step_impl(context):
    print('STEP: When Dietitian Verifies Total Patient')


@then('Dietitian can see the Total Patient count')
def step_impl(context):
    print('STEP: Then Dietitian can see the Total Patient count')


@when('Dietitian verifies Verify New Patient')
def step_impl(context):
    print('STEP: When Dietitian verifies Verify New Patient')


@then('Dietitian can see the New Patient count')
def step_impl(context):
    print('STEP: Then Dietitian can see the New Patient count')


@when('Dietitian Verifies Recovered Patient')
def step_impl(context):
    print('STEP: When Dietitian Verifies Recovered Patient')


@then('Dietitian can see Recovered Patient count')


@when('Dietitian Verifies Incoming Patient History')
def step_impl(context):
    print('STEP: When Dietitian Verifies Incoming Patient History')


@then('Dietitian can see the comparison  graph in Incoming Patient History')
def step_impl(context):
    print('STEP: Then Dietitian can see the comparison  graph in Incoming Patient History')