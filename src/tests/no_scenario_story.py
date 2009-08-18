'''
    >>> StoryRunner(story_text,
    ...             output=output,
    ...             with_colors=False,).run()
    >>> print output.getvalue()
    Story: Calculator
    As a math student
    I want to use a calculator
    So that my calculations can be easy to do
    <BLANKLINE>
'''

from pycukes import StoryRunner
from cStringIO import StringIO

story_text = """Story: Calculator
                As a math student
                I want to use a calculator
                So that my calculations can be easy to do"""

output = StringIO()
