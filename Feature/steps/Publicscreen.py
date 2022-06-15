from behave import *

use_step_matcher("re")


@given('User is on public page')
def step_impl(context):
    print('STEP: Given User is on public page')

@when('User opens the browser')
def step_impl(context):
    print('STEP: When User opens the browser')


@then('User navigates to the public page')
def step_impl(context):
   print('STEP: Then User navigates to the public page')


@given('User is on home page')
def step_impl(context):
   print('STEP: Given User is on home page')


@when('User clicks the user sign in button')
def step_impl(context):
    print('STEP: When User clicks the user sign in button')


@then('User should be directed to the sign in page')
def step_impl(context):
    print('STEP: Then User should be directed to the sign in page')


@when('User clicks Register link')
def step_impl(context):
    print('STEP: When User clicks Register link')


@then('User should be redirected to the registration page')
def step_impl(context):
    print('STEP: Then User should be redirected to the registration page')


@when('User clicks TEAM tab')
def step_impl(context):
    print('STEP: When User clicks TEAM tab')


@then('It should display the page with three doctors or dieticians name and details')
def step_impl(context):
    print('STEP: Then It should display the page with three doctors or dieticians name and details')


@when('User clicks clients button')
def step_impl(context):
   print('STEP: When User clicks clients button')


@then('User should take to the clients testimonial page')
def step_impl(context):
    print('STEP: Then User should take to the clients testimonial page')


@when('User clicks > button')
def step_impl(context):
    print('STEP: When User clicks > button')


@then('User should be on the second page of client testimonial')
def step_impl(context):
    print('STEP: Then User should be on the second page of client testimonial')


@when('User clicks the > button')
def step_impl(context):
    print('STEP: When User clicks the > button')


@then('User should be on the last page of client testimonial')
def step_impl(context):
    print('STEP: Then User should be on the last page of client testimonial')


@given('User is on sing in page')
def step_impl(context):
   print('STEP: Given User is on sing in page')


@when('User clicks Forgot Password button')
def step_impl(context):
    print('STEP: When User clicks Forgot Password button')


@then('User should be taken to the forgot password specific page')
def step_impl(context):
    print('STEP: Then User should be taken to the forgot password specific page')


@when('User clicks the Product feature button')
def step_impl(context):
    print('STEP: When User clicks the Product feature button')


@then('User should be navigated to the page where product feature page')
def step_impl(context):
    print('STEP: Then User should be navigated to the page where product feature page')


@when('User clicks Contact')
def step_impl(context):
    print('STEP: When User clicks Contact')


@then('It should display Contact page')
def step_impl(context):
    print('STEP: Then It should display Contact page')


@when('User clicks the Blogs link')
def step_impl(context):
   print('STEP: When User clicks the Blogs link')


@then('It should display Blogs page')
def step_impl(context):
   print('STEP: Then It should display Blogs page')


@when('User is on blogs page')
def step_impl(context):
    print('STEP: When User is on blogs page')


@then('User should see blogs written onthe page')
def step_impl(context):
    print('STEP: Then User should see blogs written onthe page')


@when('User clicks Fearured Content')
def step_impl(context):
    print('STEP: When User clicks Fearured Content')


@then('It should display featured content page')
def step_impl(context):
    print('STEP: Then It should display featured content page')

