from pycukes import *

@Given('I have a calculator')
def i_have_a_calc(context):
    pass

@When('I enter with 1 + -2 and press =')
def one_plus_minus_two(context):
    pass

@Then('I see -1 in my LCD')
def fail(context):
    assert None
