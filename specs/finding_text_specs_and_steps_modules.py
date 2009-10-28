'''
    >>> pycukes_console(stories_dir=SPECS_DIR,
    ...                 steps_dir=STEPS_DIR,
    ...                 output=output)

    >>> print output.getvalue()
    Story: Bowling Game
      As a bowling player
      I want to play bowling online
      So that I can play with everyone in the world
    <BLANKLINE>
      Scenario 1: Gutter Game
        Given I am playing a bowling game   ... OK
        When I hit no balls   ... OK
        Then I have 0 points   ... FAIL
    <BLANKLINE>
      Failures:
        File ".../bowling_game_steps.py", line ..., in ...
          assert context._bowling_game.score == 0
        AssertionError
    <BLANKLINE>
    <BLANKLINE>
      Ran 1 scenario with 1 failure, 0 errors and 0 pending steps
    <BLANKLINE>
'''

from cStringIO import StringIO
from pycukes import pycukes_console
import os

SPECS_DIR = os.path.dirname(__file__)+'/text_specs'
STEPS_DIR = os.path.dirname(__file__)+'/steps'
output = StringIO()
