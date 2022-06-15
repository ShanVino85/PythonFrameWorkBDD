from behave import *

use_step_matcher("re")


@given('Sign up with First Name credential')
def step_impl(context):
    print('STEP: Given  Sign up with First Name credential')

@when('User fill the valid First Name')
def step_impl(context):
    print('STEP: When User fill the valid First Name')


@given('Sign up with Last Name credential')
def step_impl(context):
    print('STEP: Given Sign up with Last Name credential')


@when('User fill the Last Name')
def step_impl(context):
    print('STEP: When User fill the Last Name')


@given('Sign up with mobile no')
def step_impl(context):
    print('STEP: Given Sign up with mobile no')


@when('User fill the valid mobile no')
def step_impl(context):
    print('STEP: When User fill the valid mobile no')


@given('Sign up with any other field as Username')
def step_impl(context):
    print('STEP: Given Sign up with any other field as Username')


@when('User creates Username')
def step_impl(context):
    print('STEP: When User creates Username')


@given('Signup with email')
def step_impl(context):
    print('STEP: Given Signup with email')


@when('User enter the valid email')
def step_impl(context):
    print('STEP: When User enter the valid email')


@given('Sign up with password')
def step_impl(context):
    print('STEP: Given Sign up with password')


@when('User create password')
def step_impl(context):
    print('STEP: When User create password')


@given('Sign up with all valid credentials')
def step_impl(context):
    print('STEP: Given Sign up with all valid credentials')


@when('User clicks sign up button')
def step_impl(context):
    print('STEP: When User clicks sign up button')


@then('Users should be able to sign up successfully')
def step_impl(context):
    print('STEP: Then Users should be able to sign up successfully')


@given('Sign up formalities with one or more invalid values')
def step_impl(context):
    print('STEP: Given Sign up formalities with one or more invalid values')


@when('User try to write a numeric value in Firstname field')
def step_impl(context):
    print('STEP: When User try to write a numeric value in Firstname field')


@then('It should display an error Please enter a valid name')
def step_impl(context):
    print('STEP: Then It should display an error Please enter a valid name')


@given('Sign up with empty field')
def step_impl(context):
    print('STEP: Given Sign up with empty field')


@when('User leaves email field empty')
def step_impl(context):
    print('STEP: When User leaves email field empty')


@then('It should display an alert to fill up all the mandatory fields')
def step_impl(context):
    print('STEP: Then It should display an alert to fill up all the mandatory fields')


@given('Sign up with invalid ph no')
def step_impl(context):
    print('STEP: Given Sign up with invalid ph no')


@when('User puts 7 digit ph no')
def step_impl(context):
    print('STEP: When User puts 7 digit ph no')


@then('It should give an alert to user for using a valid ph no for the field')
def step_impl(context):
    print('STEP: Then It should give an alert to user for using a valid ph no for the field')


@given('Sign up with invalid password')
def step_impl(context):
    print('STEP: Given Sign up with invalid password')


@when('User creates shorter password than required')
def step_impl(context):
    print('STEP: When User creates shorter password than required')



@then('User should get an error message asking to fill all the boxes')
def step_impl(context):
    print('STEP: Then User should get an error message asking to fill all the boxes')


@then('User should get an error message password criteria did not match')
def step_impl(context):
    print('STEP: Then User should get an error message password criteria did not match')


@given('User on sign up form page')
def step_impl(context):
    print('STEP: Given User on sign up form page')


@when('User leaves any other field empty')
def step_impl(context):
    print('STEP: When User leaves any other field empty')