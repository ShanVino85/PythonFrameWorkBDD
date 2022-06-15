from behave import *

use_step_matcher("re")


@given('User is logged on to Dietition website to validate heading')
def step_impl(context):
    print('STEP: Given User is logged on to Dietition website to validate heading')


@when('User lands on Create Plan page to validate heading')
def step_impl(context):
    print('STEP: When User lands on Create Plan page to validate heading')


@then('User sees the heading Confirm Health Conditions and Generate a new Diet Plan on the page')
def step_impl(context):
    print('STEP: Then User sees the heading Confirm Health Conditions and Generate a new Diet Plan on the page')


@given('User is logged on to Dietician website to browse button viibility')
def step_impl(context):
   print('STEP: Given User is logged on to Dietician website to browse button viibility')


@when('User lands on Create Plan page to test browse button')
def step_impl(context):
    print('STEP: When User lands on Create Plan page to test browse button')


@then('User should see a button with name Browse on the page')
def step_impl(context):
    print('STEP: Then User should see a button with name Browse on the page')


@given('User is logged on to Dietician website to browse button tool tip option')
def step_impl(context):
   print('STEP: Given User is logged on to Dietician website to browse button tool tip option')


@when('User lands on Create Plan page to test browse button tool tip option')
def step_impl(context):
    print('STEP: When User lands on Create Plan page to test browse button tool tip option')


@then('User should see a tool tip PDF files only for the Browse button')
def step_impl(context):
    print('STEP: Then User should see a tool tip PDF files only for the Browse button')


@given('User is logged on to Create plan page to test browse button operation')
def step_impl(context):
    print('STEP: Given User is logged on to Create plan page to test browse button operation')


@when('User clicks the Browse button and selects a document')
def step_impl(context):
    print('STEP: When User clicks the Browse button and selects a document')


@then('User should see the selected document in the field next to the Browse button on the page')
def step_impl(context):
    print('STEP: Then User should see the selected document in the field next to the Browse button on the page')

