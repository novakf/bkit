from behave import Given, When, Then
from lab1 import get_roots


@Given("equation with coef A {A} B {B} C {C}")
def given_increment(context, A: str, B: str, C: str):
    context.A = int(A)
    context.B = int(B)
    context.C = int(C)


@When("we calculate roots")
def given_increment(context):
    context.results = get_roots(context.A, context.B, context.C)


@Then("we should see root1 {root1} root2 {root2} root3 {root3} root4 {root4}")
def then_results(context, root1: str, root2: str, root3: str, root4: str):
    if root1 == "empty":
        assert context.results == []
    elif root2 == "empty":
        assert context.results == [float(root1)]
    elif root3 == "empty":
        assert context.results == [float(root1), float(root2)]
    elif root4 == "empty":
        assert context.results == [float(root1), float(root2), float(root3)]
    else:
        assert context.results == [float(root1), float(root2), float(root3), float(root4)]