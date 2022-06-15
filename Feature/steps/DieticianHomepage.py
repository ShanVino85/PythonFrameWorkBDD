from behave import *

use_step_matcher("re")


@given('The Dietitian is on Dietitian HOME PAGE')
def step_impl(context):
   print('STEP: Given The Dietitian is on Dietitian HOME PAGE')

@when('The Dietitian fills valid username, password')
def step_impl(context):
    print('STEP: When The Dietitian fills valid username, password')


@when('clicks the logged in as Dietitian option')
def step_impl(context):
    print('STEP: When clicks the logged in as Dietitian option')


@when('clicks the Sign IN button')
def step_impl(context):
    print('STEP: When clicks the Sign IN button')


@then('The page will be re directed to the Dietitian homepage and the username will display as Logged in as Dietitian Name')
def step_impl(context):
   print('STEP: Then The page will be re directed to the Dietitian homepage and the username will display as Logged in as Dietitian Name')


@given('The Dietitian is on Dietitian HOME PAGE Top Panel Section')
def step_impl(context):
    print('STEP: Given The Dietitian is on Dietitian HOME PAGE Top Panel Section')


@when('The Dietitian Home Page contains company logo and an image')
def step_impl(context):
   print('STEP: When The Dietitian Home Page contains company logo and an image')


@then('The Dietitian will see logo and image')
def step_impl(context):
    print('STEP: Then The Dietitian will see logo and image')


@when('The Dietitian Home page contains few clickable header options such as HOME,NEW PATIENT,MY PATIENT,DIET PLAN')
def step_impl(context):
    print('STEP: When The Dietitian Home page contains few clickable header options such as HOME,NEW PATIENT,MY PATIENT,DIET PLAN')


@then('The Dietitian will be re directed to the respective pages upon a click')
def step_impl(context):
    print('STEP: Then The Dietitian will be re directed to the respective pages upon a click')


@given('Dietitian is on body of Dietitian HOME PAGE')
def step_impl(context):
    print('STEP: Given Dietitian is on body of Dietitian HOME PAGE')


@when('The Dietitian Home page contains Company banner and important Announcements')
def step_impl(context):
    print('STEP: When The Dietitian Home page contains Company banner and important Announcements')


@then('The Dietitian will see all the important announcements upon login')
def step_impl(context):
    print('STEP: Then The Dietitian will see all the important announcements upon login')


@given('Dietitian is Signing Out')
def step_impl(context):
   print('STEP: Given Dietitian is Signing Out')


@when('The Dietitian home page top panel contains a SIGN OUT clickable button')
def step_impl(context):
    print('STEP: When The Dietitian home page top panel contains a SIGN OUT clickable button')


@then('The Dietitian Signs out of the portal upon the click')
def step_impl(context):
    print('STEP: Then The Dietitian Signs out of the portal upon the click')

