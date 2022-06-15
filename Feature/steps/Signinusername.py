from behave import *

use_step_matcher("re")


@given('user is on dietition website to test sign In form heading')
def step_impl(context):

    print('STEP: Given user is on dietition website to test sign In form heading')

@when('user is on sign in page to test sign In form heading')
def step_impl(context):
    print('STEP: When user is on sign in page to test sign In form heading')


@then('User should see a form with heading Sign In form to sign In using Username')
def step_impl(context):
    print('STEP: Then User should see a form with heading Sign In form to sign In using Username')


@given('user is on dietition website to test sign In button')
def step_impl(context):
   print('STEP: Given user is on dietition website to test sign In button')


@when('user is on sign in page to test sign In button')
def step_impl(context):
   print('STEP: When user is on sign in page to test sign In button')


@then('User should see a button with text SIGN IN in the Sign In form')
def step_impl(context):
    print('STEP: Then User should see a button with text SIGN IN in the Sign In form')


@given('user is on sign in page to test with all fields empty')
def step_impl(context):
    print('STEP: Given user is on sign in page to test with all fields empty')


@when('User clicks Sign In Button in the Sign In form with all fields empty')
def step_impl(context):
    print('STEP: When User clicks Sign In Button in the Sign In form with all fields empty')


@then('User should get error message Please fill out the fields')
def step_impl(context):
    print('STEP: Then User should get error message Please fill out the fields')


@given('user is on sign In page to test invalid FirstName')
def step_impl(context):
    print('STEP: Given user is on sign In page to test invalid FirstName')


@when('User clicks Sign In button entering numeric values for Username and valid values for password')
def step_impl(context):
    print('STEP: When User clicks Sign In button entering numeric values for Username and valid values for password')


@then('User should get a message Invalid entry for first field')
def step_impl(context):
    print('STEP: Then User should get a message Invalid entry for first field')


@given('user is on sign in page to test with invalid password')
def step_impl(context):
    print('STEP: Given user is on sign in page to test with invalid password')


@when('User clicks Sign In button entering extra length of password')
def step_impl(context):
    print('STEP: When User clicks Sign In button entering extra length of password')


@then('User should get a message Invalid entry for password field')
def step_impl(context):
    print('STEP: Then User should get a message Invalid entry for password field')


@given('user is on sign in page to test with username and password')
def step_impl(context):
   print('STEP: Given user is on sign in page to test with username and password')


@when('User clicks Sign In button entering invalid values for both fields')
def step_impl(context):
    print('STEP: When User clicks Sign In button entering invalid values for both fields')


@then('User should get error message Invalid login credentials')
def step_impl(context):
   print('STEP: Then User should get error message Invalid login credentials')


@given('user is on sign In page to test forgot password button')
def step_impl(context):
    print('STEP: Given user is on sign In page to test forgot password button')


@when('User clicks on Forgot Password button')
def step_impl(context):
    print('STEP: When User clicks on Forgot Password button')


@then('User should be directed to  Reset password link')
def step_impl(context):
   print('STEP: Then User should be directed to  Reset password link')


@given('user is on sign In page to Not member Yet button')
def step_impl(context):
    print('STEP: Given user is on sign In page to Not member Yet button')


@when('User clicks on not member yet button')
def step_impl(context):
    print('STEP: When User clicks on not member yet button')


@then('User will land on Register Page on dietition website')
def step_impl(context):
    print('STEP: Then User will land on Register Page on dietition website')


@given('User is on sign In page to test all fields valid entry')
def step_impl(context):
   print('STEP: Given User is on sign In page to test all fields valid entry')


@when('Validating Sign In with all fields valid entry')
def step_impl(context):
    print('STEP: When Validating Sign In with all fields valid entry')


@then('User logged into sign in page successfully')
def step_impl(context):
   print('STEP: Then User logged into sign in page successfully')

