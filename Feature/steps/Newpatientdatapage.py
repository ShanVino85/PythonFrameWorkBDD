from behave import *

use_step_matcher("re")


@given('The Dietitian lands on the New Patient page')
def step_impl(context):
    print('STEP: Given The Dietitian lands on the New Patient page')

@when('the Dietitian clicks on the New Patient clickable header option in Home Page')
def step_impl(context):
    print('STEP: When the Dietitian clicks on the New Patient clickable header option in Home Page')


@then('The Dietitian will be re directed to New Patient page from Dietitian home page')
def step_impl(context):
    print('STEP: Then The Dietitian will be re directed to New Patient page from Dietitian home page')


@given('Dietitian is on New PATIENT page')
def step_impl(context):
    print('STEP: Given Dietitian is on New PATIENT page')


@when('The Dietitian fills the patient\'s FULL NAME')
def step_impl(context):
    print('STEP: When The Dietitian fills the patient\'s FULL NAME')


@when('the Dietitian fills the patient\'s Address Line 1')
def step_impl(context):
   print('STEP: When the Dietitian fills the patient\'s Address Line 1')


@when('The Dietitian fills the patient\'s Address line 2')
def step_impl(context):
   print('STEP: When The Dietitian fills the patient\'s Address line 2')


@when('the Dietitian clicks the country dropdown and selects the respective patient\'s country')
def step_impl(context):
    print('STEP: When the Dietitian clicks the country dropdown and selects the respective patient\'s country')


@when('the Dietitian fills the patient\'s City Name')
def step_impl(context):
   print('STEP: When the Dietitian fills the patient\'s City Name')


@when('the Dietitian fills the patient\'s State name')
def step_impl(context):
    print('STEP: When the Dietitian fills the patient\'s State name')


@when('the Dietitian fills the patient\'s Postal Code')
def step_impl(context):
   print('STEP: When the Dietitian fills the patient\'s Postal Code')


@when('the Dietitian fills the patient\'s Email Id')
def step_impl(context):
   print('STEP: When the Dietitian fills the patient\'s Email Id')


@when('the Dietitian fills the patient\'s 10 digit phone number')
def step_impl(context):
    print('STEP: When the Dietitian fills the patient\'s 10 digit phone number')


@when('The Dietitian clicks the update button')
def step_impl(context):
    print('STEP: When The Dietitian clicks the update button')


@then('the Dietitian will get an alert on screen saying new patient details updated')
def step_impl(context):
    print('STEP: Then the Dietitian will get an alert on screen saying new patient details updated')


@when('the Dietitian clicks on the update health conditions button')
def step_impl(context):
   print('STEP: When the Dietitian clicks on the update health conditions button')


@then('the Dietitian will be re directed to the update health conditions page')
def step_impl(context):
    print('STEP: Then the Dietitian will be re directed to the update health conditions page')


@given('the system doesnt accept the new patient data')
def step_impl(context):
    print('STEP: Given the system doesnt accept the new patient data')


@when('the Dietitian fills the new patient\'s first name and last name which are already in records')
def step_impl(context):
    print('STEP: When the Dietitian fills the new patient\'s first name and last name which are already in records')


@then('the Dietitian will get an alert on screen saying same first name and last name exists')
def step_impl(context):
    print('STEP: Then the Dietitian will get an alert on screen saying same first name and last name exists')


@when('the Dietitian doesnt fill 10 digits in the mobile number tab')
def step_impl(context):
    print('STEP: When the Dietitian doesnt fill 10 digits in the mobile number tab')


@then('the Dietitian will get an alert on screen saying enter valid mobile number')
def step_impl(context):
    print('STEP: Then the Dietitian will get an alert on screen saying enter valid mobile number')


@when('the Dietitian doesnt fill all the tabs in the form')
def step_impl(context):
    print('STEP: When the Dietitian doesnt fill all the tabs in the form')


@then('the Dietitian will get an alert on screen saying fill all the tabs in the form')
def step_impl(context):
    print('STEP: Then the Dietitian will get an alert on screen saying fill all the tabs in the form')


@when('the Dietitian doesnt fill valid 5 digit postal code')
def step_impl(context):
    print('STEP: When the Dietitian doesnt fill valid 5 digit postal code')


@then('the Dietitian will get an alert on screen saying enter valid 5 digit postal code')
def step_impl(context):
    print('STEP: Then the Dietitian will get an alert on screen saying enter valid 5 digit postal code')


@when('the Dietitian doesnt fill valid email address')
def step_impl(context):
    print('STEP: When the Dietitian doesnt fill valid email address')


@then('the Dietitian will get an alert on scree saying enter valid email address')
def step_impl(context):
    print('STEP: Then the Dietitian will get an alert on scree saying enter valid email address')


@when('the Dietitian fills the first name and last name as alphanumeric')
def step_impl(context):
    print('STEP: When the Dietitian fills the first name and last name as alphanumeric')


@then('the Dietitian will get an alert on screen saying invalid first name and last name should contain alphabets only')
def step_impl(context):
   print('STEP: Then the Dietitian will get an alert on screen saying invalid first name and last name should contain alphabets only')

