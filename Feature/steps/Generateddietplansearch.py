from behave import *

use_step_matcher("re")


@given('The Dietitian is on the Generated Diet Plans page')
def step_impl(context):
    print('STEP: Given The Dietitian is on the Generated Diet Plans page')


@when('the Dietitian fills the search fields such as patients name or email address or phone number')
def step_impl(context):
    print( 'STEP: When the Dietitian fills the search fields such as patients name or email address or phone number')


@when('The Dietitian hits the search button')
def step_impl(context):
    print('STEP: When The Dietitian hits the search button')


@then('the Dietitian will be re directed to the search result page with similar inputs')
def step_impl(context):
    print( 'STEP: Then the Dietitian will be re directed to the search result page with similar inputs')