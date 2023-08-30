Feature: change language

  @change_language
  Scenario: change language to requested one
    Given I logged to my account and got navigated to Homepage
    When I clicked on language option
    And changed the language to what is requested
    Then verify the changed language