'''
    >>> sys.stderr = StringIO()
    >>> StoryRunner(text,
    ...             output,
    ...             colored=False,
    ...             before_all=[show_foo, show_foobar]).run()
    True
    >>> sys.stderr.getvalue()
    'FOO\\nFOOBAR\\n'
    >>> sys.stderr = StringIO()
    >>> StoryRunner(text,
    ...             output,
    ...             colored=False,
    ...             before_each=[show_foo, show_foobar]).run()
    True
    >>> sys.stderr.getvalue()
    'FOO\\nFOOBAR\\nFOO\\nFOOBAR\\n'
'''
from StringIO import StringIO
from pycukes.runner import StoryRunner
import sys


text = """
Story: Using before_all
  As a dev
  I want to execute some function before all scenarios
  So that I can manage my stories better

  Scenario 1: Nothing
    Then I should see "FOO" and "BAR" on my stderr
 
  Scenario 2: Repetition
    Then I should not see "FOO" and "BAR" again
"""

output = StringIO()


def show_foo(context):
    context.last_call = "FOO"
    print >>sys.stderr, "FOO"

def show_foobar(context):
    print >>sys.stderr, context.last_call + "BAR"
