from behave import *

use_step_matcher("re")


@given('User is on register page to Signup')
def step_impl(context):
   print('STEP: Given User is on register page to Signup')

@when('User enters the user first name last name valid mobile number and password')
def step_impl(context):
    print('STEP: When User enters the user first name last name valid mobile number and password')


@then('User clicks on Signup')
def step_impl(context):
    print ('STEP: Then User clicks on Signup')


@when('User navigates to Next page')
def step_impl(context):
    print('STEP: When User navigates to Next page')


@then('User is able to signup successfully')
def step_impl(context):
    print('STEP: Then User is able to signup successfully')


@given('User On SignUp form with an Email Option')
def step_impl(context):
    print('STEP: Given User On SignUp form with an Email Option')


@when('User enters all the valid values in the respective options')
def step_impl(context):
    print('STEP: When User enters all the valid values in the respective options')


@then('User is successfully redirected to Signin page')
def step_impl(context):
    print('STEP: Then User is successfully redirected to Signin page')


@given('User is on register page')
def step_impl(context):
    print('STEP: Given User is on register page')


@when('User clicks on signup button with all fields empty')
def step_impl(context):
   print('STEP: When User clicks on signup button with all fields empty')


@then('User should see the message that Mandatory fields cannot be empty')
def step_impl(context):
   print('STEP: Then User should see the message that Mandatory fields cannot be empty')


@given('User is on register page to signup with invalid name')
def step_impl(context):
    print('STEP: Given User is on register page to signup with invalid name')


@when('User clicks SIGN UP button in the Sign Up form  by entering numeric text for First Name valid values for the remaining fields')
def step_impl(context):
    print('STEP: When User clicks SIGN UP button in the Sign Up form  by entering numeric text for First Name valid values for the remaining fields')


@then('User should see a message Invalid data entered for First Name')
def step_impl(context):
    print('STEP: Then User should see a message Invalid data entered for First Name')


@given('User is on register page to signup with invalid last name')
def step_impl(context):
   print('STEP: Given User is on register page to signup with invalid last name')


@when('User clicks SIGN UP button in the Sign Up form  by entering numeric text for last Name valid values for the remaining fields')
def step_impl(context):
    print('STEP: When User clicks SIGN UP button in the Sign Up form  by entering numeric text for last Name valid values for the remaining fields')


@then('User should see a message Invalid data entered for last name')
def step_impl(context):
    print('STEP: Then User should see a message Invalid data entered for last name')


@given('User is on register page to signup with invalid mobile number')
def step_impl(context):
    print('STEP: Given User is on register page to signup with invalid mobile number')


@when('User clicks SIGN UP button in the Sign Up form  by entering alphanumeric text for mobile number field and valid values for the remaining fields')
def step_impl(context):
    print('STEP: When User clicks SIGN UP button in the Sign Up form  by entering alphanumeric text for mobile number field and valid values for the remaining fields')


@then('User should see a message Invalid data entered for mobile number')
def step_impl(context):
    print('STEP: Then User should see a message Invalid data entered for mobile number')


@given('User is on register page to signup with invalid anyother field')
def step_impl(context):
    print('STEP: Given User is on register page to signup with invalid anyother field')


@when('User clicks SIGN UP button in the Sign Up form  by entering numeric values for anyother field and valid values for the remaining fields')
def step_impl(context):
    print('STEP: When User clicks SIGN UP button in the Sign Up form  by entering numeric values for anyother field and valid values for the remaining fields')


@then('User should see a message Invalid data entered for anyother field')
def step_impl(context):
   print('STEP: Then User should see a message Invalid data entered for anyother field')


@given('User is on register page to signup with invalid email id  field')
def step_impl(context):
   print('STEP: Given User is on register page to signup with invalid email id  field')


@when('User clicks SIGN UP button in the Sign Up form  by entering invalid email id  and valid values for the remaining fields')
def step_impl(context):
    print('STEP: When User clicks SIGN UP button in the Sign Up form  by entering invalid email id  and valid values for the remaining fields')


@then('User should see a message Invalid data entered for email id  field')
def step_impl(context):
    print('STEP: Then User should see a message Invalid data entered for email id  field')


@given('User is on register page to signup with invalid password  field')
def step_impl(context):
    print('STEP: Given User is on register page to signup with invalid password  field')


@when('User clicks SIGN UP button in the Sign Up form  by entering invalid password  and valid values for the remaining fields')
def step_impl(context):
    print('STEP: When User clicks SIGN UP button in the Sign Up form  by entering invalid password  and valid values for the remaining fields')


@then('User should see a message Invalid data entered forpassword field')
def step_impl(context):
   print('STEP: Then User should see a message Invalid data entered forpassword field')


@given('User is on register page to signup with all fields empty on email sign up form')
def step_impl(context):
   print('STEP: Given User is on register page to signup with all fields empty on email sign up form')


@when('User clicks SIGN UP button in the Sign Up form  by leaving all fields empty on email signup form')
def step_impl(context):
   print('STEP: When User clicks SIGN UP button in the Sign Up form  by leaving all fields empty on email signup form')


@then('User should see a message cannot be empty')
def step_impl(context):
    print('STEP: Then User should see a message cannot be empty')


@given('User is on register page to signup with invalid name  on email sign up form')
def step_impl(context):
    print('STEP: Given User is on register page to signup with invalid name  on email sign up form')


@when('User clicks SIGN UP button in the Sign Up form by entering invalid name  on email signup form')
def step_impl(context):
    print('STEP: When User clicks SIGN UP button in the Sign Up form by entering invalid name  on email signup form')


@then('User should see a message invalid data entered for name')
def step_impl(context):
    print('STEP: Then User should see a message invalid data entered for name')


@given('User is on register page to signup with invalid last name  on email sign up form')
def step_impl(context):
    print('STEP: Given User is on register page to signup with invalid last name  on email sign up form')


@when('User clicks SIGN UP button in the Sign Up form by entering invalid last name  on email signup form')
def step_impl(context):
   print('STEP: When User clicks SIGN UP button in the Sign Up form by entering invalid last name  on email signup form')


@then('User should see a message invalid data entered for last name on email sign up form')
def step_impl(context):
   print('STEP: Then User should see a message invalid data entered for last name on email sign up form')


@given('User is on register page to signup with invalid UserName  on email sign up form')
def step_impl(context):
    print('STEP: Given User is on register page to signup with invalid UserName  on email sign up form')


@when('User clicks SIGN UP button in the Sign Up form by entering invalid UserName  on email signup form')
def step_impl(context):
   print('STEP: When User clicks SIGN UP button in the Sign Up form by entering invalid UserName  on email signup form')


@then('User should see a message invalid data entered for UserName on email sign up form')
def step_impl(context):
    print('STEP: Then User should see a message invalid data entered for UserName on email sign up form')


@given('User is on register page to signup with invalid Email Address  on email sign up form')
def step_impl(context):
   print('STEP: Given User is on register page to signup with invalid Email Address  on email sign up form')


@when('User clicks SIGN UP button in the Sign Up form by entering invalid Email Address on email signup form')
def step_impl(context):
   print('STEP: When User clicks SIGN UP button in the Sign Up form by entering invalid Email Address on email signup form')


@then('User should see a message invalid data entered for Email Address on email sign up form')
def step_impl(context):
    print('STEP: Then User should see a message invalid data entered for Email Address on email sign up form')


@given('User is on register page to signup with invalid Password  on email sign up form')
def step_impl(context):
    print('STEP: Given User is on register page to signup with invalid Password  on email sign up form')


@when('User clicks SIGN UP button in the Sign Up form by entering invalid Password  on email signup form')
def step_impl(context):
   print('STEP: When User clicks SIGN UP button in the Sign Up form by entering invalid Password  on email signup form')


@then('User should see a message invalid data entered for Password on email sign up form')
def step_impl(context):
    print('STEP: Then User should see a message invalid data entered for Password on email sign up form')


@given('User is on register page to signup with invalid confirm Password  on email sign up form')
def step_impl(context):
    print('STEP: Given User is on register page to signup with invalid confirm Password  on email sign up form')


@when('User clicks SIGN UP button in the Sign Up form by entering invalid confirm Password on email signup form')
def step_impl(context):
   print('STEP: When User clicks SIGN UP button in the Sign Up form by entering invalid confirm Password on email signup form')


@then('User should see a message invalid data entered for confirm Password on email sign up form')
def step_impl(context):
   print('STEP: Then User should see a message invalid data entered for confirm Password on email sign up form')
