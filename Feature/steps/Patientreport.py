from behave import *

use_step_matcher("re")


@given('Dietician is on the My patients page')
def step_impl(context):
    print('STEP: Given Dietician is on the My patients page')


@when('Enters the patient name in filter and clicks search')
def step_impl(context):
    print('STEP: When Enters the patient name in filter and clicks search')


@then('A record of the given patient is displays here')
def step_impl(context):
    print('STEP: Then A record of the given patient is displays here')


@when('Clicks View Previous Test Reports button')
def step_impl(context):
    print('STEP: When Clicks View Previous Test Reports button')


@then('Dietician navigates to View Patient Test Reports page')
def step_impl(context):
    print('STEP: Then Dietician navigates to View Patient Test Reports page')


@given('Dietician is on View Patients Test report page')
def step_impl(context):
    print('STEP: Given Dietician is on View Patients Test report page')


@when('Dietician checks the File/Report uploaded in the Confirm health condition and create diet plan page is available in the table')
def step_impl(context):
    print('STEP: When Dietician checks the File/Report uploaded in the Confirm health condition and create diet plan page is available in the table')


@then('File/Report displays in the table located in the View Patient Test Reports page')
def step_impl(context):
    print('STEP: Then File/Report displays in the table located in the View Patient Test Reports page')


@when('Clicks on the view PDF button of particular patients')
def step_impl(context):
    print('STEP: When Clicks on the view PDF button of particular patients')


@then('PDF file opens in separate window')
def step_impl(context):
    print('STEP: Then PDF file opens in separate window')


def step_impl(context):
    print('STEP: When Dietician checks the Patient Details and Doctor Details and health conditionsa and 7 Days Menu warnings and comments are available in the PDF file')


@then('Patient Details and doctor Details and health conditions and 7 Days Menu and warnings and comments are available in the PDF file')
def step_impl(context):
    print('STEP: Then Patient Details and doctor Details and health conditions and 7 Days Menu and warnings and comments are available in the PDF file')


@given('Dietician is on PDF file')
def step_impl(context):
    print('STEP: Given Dietician is on PDF file')


@when('Dietician clicks on View PDF button available in the Diet Plan column')
def step_impl(context):
    print('STEP: When Dietician clicks on View PDF button available in the Diet Plan column')


@when('Dietician checks the Patient Details and Doctor Details and health conditionsa and 7 Days Menu warnings and comments are available in the PDF file')
def step_impl(context):
    print('STEP: When Dietician checks the Patient Details and Doctor Details and health conditionsa and 7 Days Menu warnings and comments are available in the PDF file')