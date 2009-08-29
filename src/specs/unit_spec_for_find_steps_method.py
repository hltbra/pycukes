'''
    >>> steps_modules = find_steps_modules(STEPS_DIR)
    >>> len(steps_modules)
    1
    >>> steps_modules == [bowling_game_steps]
    True
'''
from pycukes import find_steps_modules
from pycukes.specs.steps import bowling_game_steps
import os
import sys


STEPS_DIR = os.path.dirname(__file__)+'/steps'
