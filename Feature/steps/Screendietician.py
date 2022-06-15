from behave import *

use_step_matcher("re")


@given('User is on dietician page')
def step_impl(context):
    print('STEP: Given User is on dietician page')

@when('User clicks dietician link')
def step_impl(context):
    print('STEP: When User clicks dietician link')


@then('User should see dietician page')
def step_impl(context):
    print('STEP: Then User should see dietician page')


@given('User is on view recent diets page')
def step_impl(context):
    print('STEP: Given User is on view recent diets page')


@when('User clicks the view recent diets')
def step_impl(context):
    print('STEP: When User clicks the view recent diets')


@then('User should see  recent diets')
def step_impl(context):
    print('STEP: Then User should see  recent diets')


@given('User is on view recent test reports page')
def step_impl(context):
    print('STEP: Given User is on view recent test reports page')


@when('User clicks view recent test reports')
def step_impl(context):
    print('STEP: When User clicks view recent test reports')


@then('User should see view recent test reports')
def step_impl(context):
    print('STEP: Then User should see view recent test reports')


@given('User on new patient page')
def step_impl(context):
    print('STEP: Given User on new patient page')


@when('User clicks new patient button')
def step_impl(context):
    print('STEP: When User clicks new patient button')


@then('it should display new patient details')
def step_impl(context):
    print('STEP: Then it should display new patient details')


@when('User clicks dietician home')
def step_impl(context):
    print('STEP: When User clicks dietician home')


@then('User should go to dietician home page')
def step_impl(context):
    print('STEP: Then User should go to dietician home page')


@when('User clicks my patient')
def step_impl(context):
    print('STEP: When User clicks my patient')


@then('It should display my patient')
def step_impl(context):
    print('STEP: Then It should display my patient')


@when('User clicks Confirm conditions and create diet plan')
def step_impl(context):
    print('STEP: When User clicks Confirm conditions and create diet plan')


@then('User should see Confirm conditions and create diet plan page')
def step_impl(context):
    print('STEP: Then User should see Confirm conditions and create diet plan page')

