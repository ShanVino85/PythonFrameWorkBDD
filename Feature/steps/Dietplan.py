from behave import *

use_step_matcher("re")


@given('User is logged on to Dietician website for diets plan page')
def step_impl(context):
    print('STEP: Given User is logged on to Dietician website for diets plan page')


@when('User lands on Diet Plans page')
def step_impl(context):
    print('STEP: When User lands on Diet Plans page')


@then('User should see the heading Generated Diet Plans on the page')
def step_impl(context):
    print('STEP: Then User should see the heading Generated Diet Plans on the page')