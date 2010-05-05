'''
    >>> sys.stderr = StringIO()
    >>> StoryRunner(text,
    ...             output,
    ...             colored=False,
    ...             before_all=[show_foo],
    ...             after_all=[show_bar]).run()
    True
    >>> sys.stderr.getvalue()
    'FOO\\nBAR\\n'


    >>> sys.stderr = StringIO()
    >>> StoryRunner(text,
    ...             output,
    ...             colored=False,
    ...             before_each=[show_foo],
    ...             after_each=[show_bar],
    ...             after_all=[show_foobar]).run()
    True
    >>> sys.stderr.getvalue()
    'FOO\\nBAR\\nFOO\\nBAR\\nFOOBAR\\n'
'''
from StringIO import StringIO
from pycukes.runner import StoryRunner
import sys


text = """
Story: Using after_all
  As a dev
  I want to execute some function after all scenarios
  So that I can manage my stories better

  Scenario 1: Nothing
    Then I should see "FOO" then I should see "BAR"
 
  Scenario 2: Repetition
    Then I should not see "BAR" after "FOO"
"""

output = StringIO()


def show_foo(context):
    print >>sys.stderr, "FOO"

def show_bar(context):
    print >>sys.stderr, "BAR"

def show_foobar(context):
    print >>sys.stderr, "FOOBAR"
