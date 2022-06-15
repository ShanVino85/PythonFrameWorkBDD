from behave import *

use_step_matcher("re")


@given('User is on any page after login')
def step_impl(context):
    print('STEP: Given User is on any page after login')


@when('User clicks on My Patients tab')
def step_impl(context):
   print('STEP: When User clicks on My Patients tab')


@then('Name email and phone number filter options and search button are displayed')
def step_impl(context):
   print('STEP: Then Name email and phone number filter options and search button are displayed')


@given('User is logged in')
def step_impl(context):
    print('STEP: Given User is logged in')


@when('User is on my patients')
def step_impl(context):
    print('STEP: When User is on my patients')


@then('Button used for search has text as Search')
def step_impl(context):
    print('STEP: Then Button used for search has text as Search')


@when('User starts typing inside name filter box')
def step_impl(context):
    print('STEP: When User starts typing inside name filter box')


@then('Text inside name filter box should disappear')
def step_impl(context):
    print('STEP: Then Text inside name filter box should disappear')


@when('User starts typing inside email address filter box')
def step_impl(context):
    print('STEP: When User starts typing inside email address filter box')


@then('Text inside email address filter box should disappear')
def step_impl(context):
    print('STEP: Then Text inside email address filter box should disappear')


@when('User starts typing inside phone number filter box')
def step_impl(context):
    print('STEP: When User starts typing inside phone number filter box')


@then('Text inside phone number filter box should disappear')
def step_impl(context):
    print('STEP: Then Text inside phone number filter box should disappear')


@when('User clicks on search with name phrase into name filter box')
def step_impl(context):
    print('STEP: When User clicks on search with name phrase into name filter box')


@then('Records for name phrase are shown')
def step_impl(context):
   print('STEP: Then Records for name phrase are shown')


@when('User clicks on search with email phrase into email address filter')
def step_impl(context):
    print('STEP: When User clicks on search with email phrase into email address filter')


@then(u'Records for email phrase are shown')
def step_impl(context):
    print(u'STEP: Then Records for email phrase are shown')


@when(u'User clicks on search with phone number into phone number filter')
def step_impl(context):
    print(u'STEP: When User clicks on search with phone number into phone number filter')


@then(u'Records for phone number are shown')
def step_impl(context):
    print(u'STEP: Then Records for phone number are shown')
