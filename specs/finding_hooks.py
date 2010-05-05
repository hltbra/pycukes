'''
    >>> StoryRunner(story_text,
    ...             output=output,
    ...             modules=find_steps_modules(DIR),
    ...             before_all=find_before_all(DIR2),
    ...             colored=False).run()
    True
'''

      
from pycukes import StoryRunner, find_steps_modules, find_before_all
from cStringIO import StringIO
import os

story_text = """Story: Bowling Game
                As a bowling player
                I want to have a bowling software
                So that I and my friends can play online

                Scenario 1: Gutter Game
                  Then I have 0 points
                
                Scenario 2: Gutter Game (again)
                  Then I have 0 points
                """
output = StringIO()

DIR = os.path.dirname(__file__)+'/steps'
DIR2 = os.path.dirname(__file__)+'/hooks'
