from behave import *
import requests
import pytest
import pytest_bdd

use_step_matcher("re")

def test_1():
    name ="Jenkins"
    title="Jenkins is CI server"
    assert name == "Jenkins"

@given('User is on the browser')
def open_a_browser(context):
    print('Given User is on the browser')


@when('User opens the Dietician Website')
def open_page_title(context):
   print('STEP: When User opens the Dietician Website')


@then('User should see the public page')
def verify_public_page(context):
   print('Then User should see the public page')

