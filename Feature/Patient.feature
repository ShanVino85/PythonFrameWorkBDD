@tag
Feature: My Patient elements

  @Test001
  Scenario: Verify my patient tab
    Given User is on any page after login
    When User clicks on "My Patients" tab
    Then It shows elements as Dietician Software MyPatients
