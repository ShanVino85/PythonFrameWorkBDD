from behave import *

use_step_matcher("re")


@given('User is logged on to Dietician website to validate PDF')
def step_impl(context):

    print('STEP: Given User is logged on to Dietician website to validate PDF')

@when('User is on View Recent Diets Page')
def step_impl(context):
   print('STEP: When User is on View Recent Diets Page')


@then('View PDF option is available for the generated diet plans')
def step_impl(context):
    print('STEP: Then View PDF option is available for the generated diet plans')


@given('User is on view recent diet page to validate PDF')
def step_impl(context):
   print('STEP: Given User is on view recent diet page to validate PDF')


@when('User selects the View PDF button for a generated diet plan')
def step_impl(context):
    print('STEP: When User selects the View PDF button for a generated diet plan')


@then('User should see the information in the PDF as Patient details,Doctor details,Patient health details,7-day menu,warnings,Comments')
def step_impl(context):
    print('STEP: Then User should see the information in the PDF as Patient details,Doctor details,Patient health details,7-day menu,warnings,Comments')


@given('User is logged on to Dietician website to validate PDF for a diet plan')
def step_impl(context):
    print('STEP: Given User is logged on to Dietician website to validate PDF for a diet plan')


@when('User selects the view PDF button')
def step_impl(context):
    print('STEP: When User selects the view PDF button')


@then('User should be able to see download option for the PDF and able to download the PDF')
def step_impl(context):
    print('STEP: Then User should be able to see download option for the PDF and able to download the PDF')
