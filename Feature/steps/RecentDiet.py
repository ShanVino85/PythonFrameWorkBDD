from behave import *

use_step_matcher("re")


@given('User is logged on to Dietician website to validate')
def step_impl(context):
    print('STEP: Given User is logged on to Dietician website to validate')

@then('User should see 5 records per page')
def step_impl(context):
    print('STEP: Then User should see 5 records per page')


@given('User is on view recent diets page to validate')
def step_impl(context):
    print('STEP: Given User is on view recent diets page to validate')


@when('More than one page of records are displayed and User is on first page')
def step_impl(context):
    print('STEP: When More than one page of records are displayed and User is on first page')


@then('Next Page button  is enabled')
def step_impl(context):
    print('STEP: Then Next Page button  is enabled')


@given('User is on View Recent Diets Page and more than one page of records are displayed and User is on first page')
def step_impl(context):
    print('STEP: Given User is on View Recent Diets Page and more than one page of records are displayed and User is on first page')


@when('User clicks on next button')
def step_impl(context):
    print('STEP: When User clicks on next button')


@then('User should see the second page')
def step_impl(context):
    print('STEP: Then User should see the second page')


@given('User is on last page of view recent diets')
def step_impl(context):
    print('STEP: Given User is on last page of view recent diets')


@when('User see more than one page of records')
def step_impl(context):
    print('STEP: When User see more than one page of records')


@then('Previous Page button is enabled')
def step_impl(context):
    print('STEP: Then Previous Page button is enabled')


@given('User is on last page of view recent diets to validate previou page')
def step_impl(context):
    print('STEP: Given User is on last page of view recent diets to validate previou page')


@when('User clicks on previous page button')
def step_impl(context):
    print('STEP: When User clicks on previous page button')


@then('User should be traversed to previous page')
def step_impl(context):
    print('STEP: Then User should be traversed to previous page')


@given('User is on first page')
def step_impl(context):
    print('STEP: Given User is on first page')


@then('Previous page button is disabled')
def step_impl(context):
    print('STEP: Then Previous page button is disabled')
