'''
    >>> import sys
    >>> StoryRunner(story_text,
    ...             output=output,
    ...             modules=[sys],
    ...             colored=False).run()
    True
    >>> print output.getvalue()
    Story: Bowling Game
      As a bowling player
      I want to have a bowling software
      So that I and my friends can play online
    <BLANKLINE>
      Scenario 1: Gutter Game
        Given I am playing a bowling game   ... PENDING
        When I hit no balls   ... PENDING
        Then I have 0 points   ... PENDING
    <BLANKLINE>
      Ran 1 scenario with 0 failures, 0 errors and 3 pending steps
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
