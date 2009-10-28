'''
    >>> StoryRunner(story_text,
    ...             output=output,
    ...             colored=False,
    ...             modules=[]).run()
    True
    >>> print output.getvalue()
    Story: Calculator
      As a math student
      I want to use a calculator
      So that my calculations can be easy to do
    <BLANKLINE>
      Scenario 1: Sum of 1 and 2
        Given I have a calculator   ... PENDING
        When I enter with 1 + 2 and press =   ... PENDING
        Then I see 3 in my LCD   ... PENDING
    <BLANKLINE>
      Ran 1 scenario with 0 failures, 0 errors and 3 pending steps
    <BLANKLINE>
'''

from pycukes import StoryRunner
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
    doctest.testmod()
