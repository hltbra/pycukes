import os
import sys


def find_steps_modules(dirname):
    sys.path.append(dirname)
    modules = [__import__(filename[:-3]) for filename in os.listdir(dirname)
                                           if filename.endswith('.py') and filename not in ['__init__.py']]
    sys.path = sys.path[:-1]
    return modules
