from behave import *

use_step_matcher("re")


@given('User is on home page after login')
def step_impl(context):
   print('STEP: Given User is on home page after login')

@when('Clicks My account icon on the menu bar')
def step_impl(context):
    print('STEP: When Clicks My account icon on the menu bar')


@then('Account displays few clickable options which will be redirected to their respective pages')
def step_impl(context):
    print('STEP: Then Account displays few clickable options which will be redirected to their respective pages')


@when('user clicks on Test Reports option')
def step_impl(context):
    print('STEP: When user clicks on Test Reports option')


@then('user can see the Test reports')
def step_impl(context):
    print('STEP: Then user can see the Test reports')


@when('user clicks on Diet Plans option')
def step_impl(context):
    print('STEP: When user clicks on Diet Plans option')


@then('user can see all the Diet Plans')
def step_impl(context):
    print('STEP: Then user can see all the Diet Plans')


@when('user clicks on Previous Visits')
def step_impl(context):
    print('STEP: When user clicks on Previous Visits')


@then('user can see all their Previous visits')
def step_impl(context):
    print('STEP: Then user can see all their Previous visits')


@when('user clicks on Upcoming visits')
def step_impl(context):
    print('STEP: When user clicks on Upcoming visits')


@then('user can see all the Upcoming visits')
def step_impl(context):
    print('STEP: Then user can see all the Upcoming visits')


@when('user clicks on BOOK AN APPOINTMENT')
def step_impl(context):
    print('STEP: When user clicks on BOOK AN APPOINTMENT')


@then('user will be redireted to Book an Appointment page')
def step_impl(context):
    print('STEP: Then user will be redireted to Book an Appointment page')


@when('user clicks on Services')
def step_impl(context):
    print('STEP: When user clicks on Services')


@then('user can see all the services provided')
def step_impl(context):
    print('STEP: Then user can see all the services provided')


@when('user clicks on Recipes')
def step_impl(context):
    print('STEP: When user clicks on Recipes')


@then('user can see all the recipes available')
def step_impl(context):
    print('STEP: Then user can see all the recipes available')

