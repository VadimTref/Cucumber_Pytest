Feature: Main Page

  #Scenario: Open Login page
    Given Main page is opened
    When User opens Login page
    Then Login page is opened

  #Scenario: Registration
    Given Main page is opened
    When User opens Registration page
    When User enters credentials
    When User clicks Submit button
    Then Registration is completed


  Scenario: Open Product Page
    Given Main page is opened
    When User clicks All Products
    Then Products page is opened