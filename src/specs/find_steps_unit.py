'''
    >>> steps_modules = find_steps_modules(STEPS_DIR)
    >>> len(steps_modules)
    1
    >>> steps_modules == [bowling_game_steps]
    True
'''
from pycukes import find_steps_modules
from pycukes.tests.scenarios import bowling_game_steps
import os
import sys


STEPS_DIR = os.path.dirname(__file__)+'/scenarios'
#
#sys.path.append(STEPS_DIR)
#scenarios_modules = [__import__(filename[:-3]) for filename in os.listdir(STEPS_DIR)
#                        if filename.endswith('.py') and filename not in ['__init__.py']]
#sys.path = sys.path[:-1]
