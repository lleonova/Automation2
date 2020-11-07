# Created by username at 10/25/20
Feature: Dress selection functionality
  # Enter feature description here

  Scenario: User can select Dress colors
    Given Open Amazon product B07PVB53RX page
    When Confirm number of Dress color choices
    Then Verify User can select trough Dress colors
