from pycukes import *

@Given('I have a calculator')
def i_have_a_calculator(self):
    pass

@When('I enter with 1 + 2 and press =')
def i_enter_with_one_and_two(self):
    assert False

@Then('I see 3 in my LCD')
def i_see_three_in_my_lcd(self):
    raise Exception()
