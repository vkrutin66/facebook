
Feature: Facebook

Scenario: Facebook random actions

  Given website "https://www.facebook.com/"
  Then login as "makar.nenashev@gmail.com" password "78qa22!#"
  Then make random actions
  Then exit