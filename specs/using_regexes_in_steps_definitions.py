'''
    >>> StoryRunner(story_text,
    ...             colored=False,
    ...             output=output,
    ...             modules=[calculator_with_regexes]).run()
    True
    >>> print output.getvalue()
    Story: Using Regexes in Step Definitions
      In order to use regexes in step definitions
      As a smart regex jedi
      I want to write step definitions using regexes
    <BLANKLINE>
      Scenario 1: Sum of 1 and 1
        When I sum 1 and 1   ... OK
        Then I have 2 as result   ... PENDING
    <BLANKLINE>
      Scenario 2: Sum of 22 and 33
        When I sum 22 and 33   ... OK
        Then I have 55 as result   ... PENDING
    <BLANKLINE>
      Ran 2 scenarios with 0 failures, 0 errors and 2 pending steps
    <BLANKLINE>
    '''

from pycukes import *
from pycukes.specs.steps import calculator_with_regexes
from cStringIO import StringIO

output = StringIO()

story_text = """Story: Using Regexes in Step Definitions
In order to use regexes in step definitions
As a smart regex jedi
I want to write step definitions using regexes

Scenario 1: Sum of 1 and 1
When I sum 1 and 1
Then I have 2 as result

Scenario 2: Sum of 22 and 33
When I sum 22 and 33
Then I have 55 as result"""
