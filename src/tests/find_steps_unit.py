'''
    >>> find_steps_modules(STEPS_DIR) == scenarios_modules
    True
'''
from pycukes import find_steps_modules
import os
import sys


STEPS_DIR = os.path.dirname(__file__)+'/scenarios'

sys.path.append(STEPS_DIR)
scenarios_modules = [__import__(filename[:-3]) for filename in os.listdir(STEPS_DIR)
                        if filename.endswith('.py') and filename not in ['__init__.py']]
sys.path = sys.path[:-1]
