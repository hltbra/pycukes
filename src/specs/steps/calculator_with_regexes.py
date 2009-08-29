from pycukes import *

@When('I sum $left and $right')
def sum_two_numbers(context, left, right):
    context._sum = int(left) + int(right)
#Then I have 2 as result

