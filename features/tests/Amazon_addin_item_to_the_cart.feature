# Created by username at 10/14/20
Feature: Test Scenarios for Amazon Shopping Cart functionality
  # Enter feature description here

  Scenario: User can search for a product and successfully add it to the cart
    Given Open Amazon page
    When Input Amoretu Women Summer Tunic Dress into search field
    And Click on search icon
    Then Product results for Amoretu Women Summer Tunic Dress are shown
    And Click on first item in the search result
    And Choose Small size from drop-down menu
    And Select first color choice
    And Click Add To Cart Button
    And Amazon Shopping Cart Count has 1 items
    And User can see Added to Cart text
    And Click on Shopping Cart icon
    Then Verify that cart has 1 item