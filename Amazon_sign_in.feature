# Created by username at 11/7/20
Feature: Test Scenarios for Amazon Sign In Page functionality

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Return and Orders link
    Then Verify Sign In page is opened
