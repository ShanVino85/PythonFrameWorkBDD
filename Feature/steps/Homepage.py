from behave import *

use_step_matcher("re")


@given('User is on the browser')
def step_impl(context):
    print('STEP: Given User is on the browser')


@when('User opens the Dietician Website')
def step_impl(context):
   print('STEP: When User opens the Dietician Website')


@then('User should see the public page')
def step_impl(context):
   print('STEP: Then User should see the public page')


@given('User is on the public page')
def step_impl(context):
    print('STEP: Given User is on the public page')


@when('User navigates to this page from any browser')
def step_impl(context):
   print('STEP: When User navigates to this page from any browser')


@then('User should see a logo with the company name on the home page')
def step_impl(context):
    print('STEP: Then User should see a logo with the company name on the home page')


@given('User on Homepage')
def step_impl(context):
    print('STEP: Given User on Homepage')

@when('User navigates to the homepage')
def step_impl(context):
   print('STEP: When User navigates to the homepage')


@then('User should see a menu bar which contains few tabs along with a search icon, my account icon and a menu bar icon')
def step_impl(context):
    print('STEP: Then User should see a menu bar which contains few tabs along with a search icon, my account icon and a menu bar icon')

