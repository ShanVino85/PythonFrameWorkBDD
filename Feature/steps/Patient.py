from behave import *

use_step_matcher("re")


@when('User clicks on "My Patients" tab')
def step_impl(context):
    print('STEP: When User clicks on "My Patients" tab')


@then('It shows elements as Dietician Software MyPatients')
def step_impl(context):
    print('STEP: Then It shows elements as Dietician Software MyPatients')