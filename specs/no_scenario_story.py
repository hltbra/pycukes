'''
    >>> StoryRunner(story_text,
    ...             output=output,
    ...             colored=False,).run()
    True
    >>> print output.getvalue()
    Story: Calculator
      As a math student
      I want to use a calculator
      So that my calculations can be easy to do
    <BLANKLINE>
      Ran 0 scenarios with 0 failures, 0 errors and 0 pending steps
    <BLANKLINE>
'''

from pycukes import StoryRunner
from cStringIO import StringIO

story_text = """Story: Calculator
                As a math student
                I want to use a calculator
                So that my calculations can be easy to do"""

output = StringIO()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
