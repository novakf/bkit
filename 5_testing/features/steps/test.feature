Feature: Testing the Equation
  Scenario: Test calculate 4 roots
    Given equation with coef A 1 B -10 C 9
    When we calculate roots
    Then we should see root1 -3.0 root2 -1.0 root3 1.0 root4 3.0

  Scenario: Test calculate 2 roots
    Given equation with coef A 1 B -2 C 1
    When we calculate roots
    Then we should see root1 -1.0 root2 1.0 root3 empty root4 empty

  Scenario: Test calculate 0 roots
    Given equation with coef A 1 B 2 C 3 
    When we calculate roots
    Then we should see root1 empty root2 empty root3 empty root4 empty