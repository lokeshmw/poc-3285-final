Feature:get cart items

  @cart_items
  Scenario: get cart item names
    Given I logged my account and got navigated to the the Homepage
    When I clicked on cart option
    And printed the items present in cart