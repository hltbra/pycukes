'''
    >>> StoryRunner(story_text,
    ...             output=output,
    ...             modules=find_steps_modules(DIR),
    ...             before_all=find_before_all(DIR2),
    ...             after_all=find_after_all(DIR2),
    ...             before_each=find_before_each(DIR2),
    ...             after_each=find_after_each(DIR2),
    ...             colored=False).run()
    HELLO WORLD
    True
'''

      
from pycukes import (StoryRunner,
                     find_steps_modules,
                     find_before_all,
                     find_after_all,
                     find_before_each,
                     find_after_each)
from cStringIO import StringIO
import os
import doctest

checker = doctest.OutputChecker()

story_text = """Story: Bowling Game
                As a bowling player
                I want to have a bowling software
                So that I and my friends can play online

                Scenario 1: Gutter Game
                  Then I have 2 points
                  And I have not printed HELLO WORLD
                
                Scenario 2: Gutter Game (again)
                  Then I have 4 points
                  And I have not printed HELLO WORLD
                """
output = StringIO()

DIR = os.path.dirname(__file__)+'/steps'
DIR2 = os.path.dirname(__file__)+'/hooks'
