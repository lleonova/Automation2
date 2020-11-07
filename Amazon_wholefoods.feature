# Created by username at 11/6/20
Feature: Test Scenarios for the Amazon WholeFoods Deals Page functionality


  Scenario: Every product under the yellow line on the Amazon WholeFoods Deals page has a text ‘Regular’ and a product name
    Given Open Amazon WholeFoods Deals page
    Then Every product under the yellow line has has a text ‘Regular’ and a product name
