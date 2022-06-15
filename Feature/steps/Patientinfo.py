from behave import *
use_step_matcher("re")

@given('User is on my patients page')
def step_impl(context):
    print('STEP: Given User is on my patients page')


@when('User types in anything other than 0 to 9 in phone number field')
def step_impl(context):
   print('STEP: When User types in anything other than 0 to 9 in phone number field')


@then('It must throw error message and discontinue search action')
def step_impl(context):
   print('STEP: Then It must throw error message and discontinue search action')


@when('User types in anything other valid character in email address field')
def step_impl(context):
  print('STEP: When User types in anything other valid character in email address field')


@when('User types in anything other alphabets in name field')
def step_impl(context):
   print('STEP: When User types in anything other alphabets in name field')


@given('User is on my patients')
def step_impl(context):
  print('STEP: Given User is on my patients')


@when('User clicks on search button with all fields empty')
def step_impl(context):
   print('STEP: When User clicks on search button with all fields empty')


@then('Displays all patients for that dietician only')
def step_impl(context):
   print('STEP: Then Displays all patients for that dietician only')


@given('User is on my patients list')
def step_impl(context):

  print('STEP: Given User is on my patients list')


@when('User clicks on search button with or without all fields empty')
def step_impl(context):
   print('STEP: When User clicks on search button with or without all fields empty')


@then('It shows columns name like Record Number CustID and Name and Details and Last Visit and Actions and View Previous Test Report and View Previous Diet Plans and Create New Report or Plan')
def step_impl(context):
    print('STEP: Then It shows columns name like Record Number CustID and Name and Details and Last Visit and Actions and View Previous Test Report and View Previous Diet Plans and Create New Report or Plan')


@given('Patients record are displayed')
def step_impl(context):
   print('STEP: Given Patients record are displayed')


@when('Records are more than 10')
def step_impl(context):
    print('STEP: When Records are more than 10')


@then('It must show pagination links')
def step_impl(context):
   print('STEP: Then It must show pagination links')


@when('User clicks on next pagination link')
def step_impl(context):
    print('STEP: When User clicks on next pagination link')


@then('It goes to next page and shows different patients on that page"')
def step_impl(context):
   print('STEP: Then It goes to next page and shows different patients on that page"')


@when('User clicks on previous pagination link')
def step_impl(context):
    print('STEP: When User clicks on previous pagination link')


@then('It goes to previous page')
def step_impl(context):
    print('STEP: Then It goes to previous page')


@given('User has searched patients')
def step_impl(context):
    print('STEP: Given User has searched patients')


@when('Patients records Cust ID are displayed')
def step_impl(context):
   print('STEP: When Patients records Cust ID are displayed')


@then('Customer Id is shown in column Cust ID column')
def step_impl(context):
    print('STEP: Then Customer Id is shown in column Cust ID column')


@when('Patients records  Name are displayed')
def step_impl(context):
   print('STEP: When Patients records  Name are displayed')


@then('Patients name is displayed in Name column')
def step_impl(context):
    print('STEP: Then Patients name is displayed in Name column')


@when('Patients records are displayed')
def step_impl(context):
    print('STEP: When Patients records are displayed')


@then('Details column shows patients email or phone number or address')
def step_impl(context):
   print('STEP: Then Details column shows patients email or phone number or address')


@when('Patients records are valid date displayed')
def step_impl(context):
    print('STEP: When Patients records are valid date displayed')


@then('Last visit date is shown in valid date format')
def step_impl(context):
   print('STEP: Then Last visit date is shown in valid date format')


@when('Patients records valid format are displayed')
def step_impl(context):
   print('STEP: When Patients records valid format are displayed')


@then('Verify that email address is in valid format in details cloumn')
def step_impl(context):
   print('STEP: Then Verify that email address is in valid format in details cloumn')


@given('Patients records are displayed')
def step_impl(context):
   print('STEP: Given Patients records are displayed')


@when('User clicks on button View Previous Diet Plans')
def step_impl(context):
    print('STEP: When User clicks on button View Previous Diet Plans')


@then('It redirects user to Generated Diet Plans page')
def step_impl(context):
   print('STEP: Then It redirects user to Generated Diet Plans page')


@when('User clicks on button Create New Report/Plan')
def step_impl(context):
    print('STEP: When User clicks on button Create New Report/Plan')


@then('It redirects user to Confirm Health Conditions and Generate a New Diet plan page')
def step_impl(context):
    print(u'STEP: Then It redirects user to Confirm Health Conditions and Generate a New Diet plan page')


@when('User clicks on button View Previous Test Reports')
def step_impl(context):
    print('STEP: When User clicks on button View Previous Test Reports')


@then('It redirects user to View Patient Test Reports page')
def step_impl(context):
    print('STEP: Then It redirects user to View Patient Test Reports page')


@then('Verify that email address is in valid format in details column')
def step_impl(context):
   print('STEP: Then Verify that email address is in valid format in details column')


@then('Displays all patients for that dietitian only')
def step_impl(context):
   print('STEP: Then Displays all patients for that dietitian only')