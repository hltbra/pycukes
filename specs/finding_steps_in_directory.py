'''
    >>> StoryRunner(story_text,
    ...             output=output,
    ...             modules=find_steps_modules(DIR),
    ...             colored=False).run()
    False
    >>> print output.getvalue()
    Story: Bowling Game
      As a bowling player
      I want to have a bowling software
      So that I and my friends can play online
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

      
from pycukes import StoryRunner, find_steps_modules
from cStringIO import StringIO
import os

story_text = """Story: Bowling Game
                As a bowling player
                I want to have a bowling software
                So that I and my friends can play online

                Scenario 1: Gutter Game
                  Given I am playing a bowling game
                  When I hit no balls
                  Then I have 0 points"""
output = StringIO()

DIR = os.path.dirname(__file__)+'/steps'
