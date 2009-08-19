import os
import sys


def find_steps_modules(dirname):
    sys.path.append(dirname)
    modules = [__import__(filename[:-3]) for filename in os.listdir(dirname)
                                           if filename.endswith('steps.py')]
    sys.path = sys.path[:-1]
    return modules

def find_text_specs(dirname):
    return [open('%s/%s' % (dirname,filename)).read() for filename in os.listdir(dirname)
                                                        if filename.endswith('.story')]
