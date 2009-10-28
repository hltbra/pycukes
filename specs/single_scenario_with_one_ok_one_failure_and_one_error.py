'''
    >>> StoryRunner(story_text,
    ...             output=output,
    ...             colored=False,
    ...             modules=[sum_of_one_and_two_with_one_ok_one_fail_and_one_error]).run()
    False
    >>> print output.getvalue()
    Story: Calculator
      As a math student
      I want to use a calculator
      So that my calculations can be easy to do
    <BLANKLINE>
      Scenario 1: Sum of 1 and 2
        Given I have a calculator   ... OK
        When I enter with 1 + 2 and press =   ... FAIL
        Then I see 3 in my LCD   ... ERROR
    <BLANKLINE>
      Failures:
        File ".../sum_of_one_and_two_with_one_ok_one_fail_and_one_error.py", line ..., in i_enter_with_one_and_two
          assert False
        AssertionError
    <BLANKLINE>
    <BLANKLINE>
      Errors:
        File ".../sum_of_one_and_two_with_one_ok_one_fail_and_one_error.py", line ..., in i_see_three_in_my_lcd
          raise Exception()
        Exception
    <BLANKLINE>
    <BLANKLINE>
      Ran 1 scenario with 1 failure, 1 error and 0 pending steps
    <BLANKLINE>
'''

from pycukes import StoryRunner
from pycukes.specs.steps import sum_of_one_and_two_with_one_ok_one_fail_and_one_error
from cStringIO import StringIO


output = StringIO()
story_text = """Story: Calculator
                As a math student
                I want to use a calculator
                So that my calculations can be easy to do
                
                Scenario 1: Sum of 1 and 2
                  Given I have a calculator
                  When I enter with 1 + 2 and press =
                  Then I see 3 in my LCD"""

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
