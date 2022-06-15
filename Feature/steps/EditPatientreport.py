from behave import *

use_step_matcher("re")


@given('Dietician naviagates to My Patients screen')
def step_impl(context):
    print('STEP: Given Dietician naviagates to My Patients screen')

@when('Dietician enters patient name and clicks search button')
def step_impl(context):
    print('STEP: When Dietician enters patient name and clicks search button')


@then('Patient details for the given name is displays in the My Patients screen')
def step_impl(context):
    print('STEP: Then Patient details for the given name is displays in the My Patients screen')


@when('Dietician checks  VIEW PREVIOUS TEST REPORTand PLANS and CREATE NEW REPORT and PLAN and EDIT PREVIOUS REPORT and PLAN buttons')
def step_impl(context):
    print('STEP: When Dietician checks  VIEW PREVIOUS TEST REPORTand PLANS and CREATE NEW REPORT and PLAN and EDIT PREVIOUS REPORT and PLAN buttons')


@then('VIEW PREVIOUS TEST REPORT and PLAN and CREATE NEW REPORT and PLAN buttons  EDIT PREVIOUS REPORT and PLAN buttons displays in the My Patients screen')
def step_impl(context):
    print('STEP: Then VIEW PREVIOUS TEST REPORT and PLAN and CREATE NEW REPORT and PLAN buttons  EDIT PREVIOUS REPORT and PLAN buttons displays in the My Patients screen')


@given('Dietician is on My Patients screen')
def step_impl(context):
    print('STEP: Given Dietician is on My Patients screen')


@when('Dietician clicks EDIT PREVIOUS REPORT/PLAN button')
def step_impl(context):
    print('STEP: When Dietician clicks EDIT PREVIOUS REPORT/PLAN button')


@then('Dietician navigates to Confirm Health conditions and Generate a new Diet plan')
def step_impl(context):
    print('STEP: Then Dietician navigates to Confirm Health conditions and Generate a new Diet plan')


@given('Dietician is on Confirm Health Conditions and Generate a new Diet Plan page')
def step_impl(context):
    print('STEP: Given Dietician is on Confirm Health Conditions and Generate a new Diet Plan page')


@when('Dietician gets the page with pre selections of health conditionsa andCo-Morbidities and Preference')
def step_impl(context):
    print('STEP: When Dietician gets the page with pre selections of health conditionsa andCo-Morbidities and Preference')


@then('health conditions and Co-Morbidities and Preference are preselected based on the report and Menu created')
def step_impl(context):
    print('STEP: Then health conditions and Co-Morbidities and Preference are preselected based on the report and Menu created')


@when('Dietician changes the condition and Co Morbidities and preference')
def step_impl(context):
    print('STEP: When Dietician changes the condition and Co Morbidities and preference')


@then('changed condition and Co Morbidities and preferences appears on the screen along with the previous selection')
def step_impl(context):
    print('STEP: Then changed condition and Co Morbidities and preferences appears on the screen along with the previous selection')


@when('Clicks both of the confirm buttons')
def step_impl(context):
    print('STEP: When Clicks both of the confirm buttons')


@then('Confirm button turns into Confirmed and authenticiated with the message Health conditions and Co Morbidities and preferences are confirmed')
def step_impl(context):
    print('STEP: Then Confirm button turns into Confirmed and authenticiated with the message Health conditions and Co Morbidities and preferences are confirmed')


@when('Clicks GENERATE MENU button     Diet plan')
def step_impl(context):
    print('STEP: When Clicks GENERATE MENU button  Diet plan')


@then('updated and authendicated with the message Report and Diet Plan is updated successfully')
def step_impl(context):
    print('STEP: Then updated and authendicated with the message Report and Diet Plan is updated successfully')


@given('Dietician navigates to My Patients screen')
def step_impl(context):
    print('STEP: Given Dietician navigates to My Patients screen')


@when('Enters patient name and hit the search button')
def step_impl(context):
    print('STEP: When Enters patient name and hit the search button')


@when('Dietician gets VIEW PREVIOUS TEST REPORT and  VIEW PREVIOUS DIET PLANS and CREATE NEW REPORT or  PLAN buttons')
def step_impl(context):
    print('STEP: When Dietician gets VIEW PREVIOUS TEST REPORT and  VIEW PREVIOUS DIET PLANS and CREATE NEW REPORT or  PLAN buttons')


@then('EDIT PREVIOUS REPORT/PLAN button is not displays on the screen')
def step_impl(context):
    print('STEP: Then EDIT PREVIOUS REPORT/PLAN button is not displays on the screen')


@when('Clicks GENERATE MENU button	Diet plan')
def step_impl(context):
   print(u'STEP: When Clicks GENERATE MENU button	Diet plan')