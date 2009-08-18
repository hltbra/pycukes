'''
    >>> StoryRunner(story_text,
    ...             output=output,
    ...             with_colors=False,
    ...             modules=[]).run()
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
'''

from pycukes import StoryRunner
from cStringIO import StringIO
import os


output = StringIO()
story_text = """Story: Calculator
                As a math student
                I want to use a calculator
                So that my calculations can be easy to do
                
                Scenario 1: Sum of 1 and 2
                  Given I have a calculator
                  When I enter with 1 + 2 and press =
                  Then I see 3 in my LCD"""
