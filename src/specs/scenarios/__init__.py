import os
import sys
sys.path.append(os.path.dirname(__file__))

for filename in os.listdir(os.path.dirname(__file__)):
    if filename.endswith('.py') and filename != '__init__.py':
        globals()[filename[:-3]] = __import__(filename[:-3])
