'''
    >>> find_text_specs(SPECS_DIR) == ["""Story: Bowling Game
    ... As a bowling player
    ... I want to play bowling online
    ... So that I can play with everyone in the world
    ...
    ...   Scenario 1: Gutter Game
    ...     Given I am playing a bowling game
    ...     When I hit no balls
    ...     Then I have 0 points
    ... """]
    True
'''

from pycukes import find_text_specs
import os

SPECS_DIR = os.path.dirname(__file__)+'/text_specs'
