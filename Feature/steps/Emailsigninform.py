from behave import *

use_step_matcher("re")


@given('User is on Dietition page to test log in with your email form')
def step_impl(context):
   print('STEP: Given User is on Dietition page to test log in with your email form')

@when('User is on Sign In page to test log in with your email form')
def step_impl(context):
    print('STEP: When User is on Sign In page to test log in with your email form')


@then('User should see a form with heading Log in with  your email form to sign In using email')
def step_impl(context):
    print('STEP: Then User should see a form with heading Log in with  your email form to sign In using email')


@given('User is on Dietition page to test Login button')
def step_impl(context):
    print('STEP: Given User is on Dietition page to test Login button')


@when('User is on Sign In page to test log in  button with your email form')
def step_impl(context):
    print('STEP: When User is on Sign In page to test log in  button with your email form')


@then('User should see a button with text Log in in the Sign In form')
def step_impl(context):
    print('STEP: Then User should see a button with text Log in in the Sign In form')


@given('User is on sign In page to test Email and password empty')
def step_impl(context):
    print('STEP: Given User is on sign In page to test Email and password empty')


@when('User clicks Log In button with all fields empty')
def step_impl(context):
    print('STEP: When User clicks Log In button with all fields empty')


@then('User gets  error message Please fill out fields in textbox')
def step_impl(context):
    print('STEP: Then User gets  error message Please fill out fields in textbox')


@given('User is on sign In page to test invalid Email and valid password')
def step_impl(context):
    print('STEP: Given User is on sign In page to test invalid Email and valid password')


@when('User clicks Log In button with invalid email and valid password')
def step_impl(context):
    print('STEP: When User clicks Log In button with invalid email and valid password')


@then('User should see message Please fill with valid email id')
def step_impl(context):
    print('STEP: Then User should see message Please fill with valid email id')


@given('User is on sign In page to test valid Email and invalid password')
def step_impl(context):
    print('STEP: Given User is on sign In page to test valid Email and invalid password')


@when('User clicks Log In button with valid email and invalid password')
def step_impl(context):
    print('STEP: When User clicks Log In button with valid email and invalid password')


@then('User gets a message Invalid Password Pleasetry again')
def step_impl(context):
    print('STEP: Then User gets a message Invalid Password Pleasetry again')


@given('User is on sign In page to test valid Email and empty password field')
def step_impl(context):
    print('STEP: Given User is on sign In page to test valid Email and empty password field')


@when('User clicks Log In button with valid email and empty password')
def step_impl(context):
    print('STEP: When User clicks Log In button with valid email and empty password')


@then('User gets a message Please fill the password')
def step_impl(context):
    print('STEP: Then User gets a message Please fill the password')


@given('User is on sign In page to test invalid Email and password')
def step_impl(context):
    print('STEP: Given User is on sign In page to test invalid Email and password')


@when('User clicks Log In with both invalid email and password')
def step_impl(context):
    print('STEP: When User clicks Log In with both invalid email and password')


@then('User gets error message message Invalid Login credentials')
def step_impl(context):
    print('STEP: Then User gets error message message Invalid Login credentials')


@given('User is on sign In page to test valid Email and password')
def step_impl(context):
    print('STEP: Given User is on sign In page to test valid Email and password')


@when('User clicks Log In with both valid email and password')
def step_impl(context):
    print('STEP: When User clicks Log In with both valid email and password')


@then('User gets a message logged in successfully and sees signout button')
def step_impl(context):
    print('STEP: Then User gets a message logged in successfully and sees signout button')


@given('User is on sign In page to forgot password')
def step_impl(context):
    print('STEP: Given User is on sign In page to forgot password')


@when('User clicks on forgot password button')
def step_impl(context):
    print('STEP: When User clicks on forgot password button')


@then('User is redirected to reset password link')
def step_impl(context):
    print('STEP: Then User is redirected to reset password link')


@given('User is on sign In page to test facebook button')
def step_impl(context):
    print('STEP: Given User is on sign In page to test facebook button')


@when('User clicks Facebook button to log in')
def step_impl(context):
    print('STEP: When User clicks Facebook button to log in')


@then('User is redirected to Facebook  login Page')
def step_impl(context):
    print('STEP: Then User is redirected to Facebook  login Page')

