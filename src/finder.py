import os
import sys


def find_steps_modules(dirname):
    sys.path.insert(0, dirname)
    modules = [__import__(filename[:-3]) for filename in os.listdir(dirname)
                                           if filename.endswith('steps.py')]
    del sys.path[0]
    return modules

def find_text_specs(dirname):
    return [open('%s/%s' % (dirname,filename)).read() for filename in os.listdir(dirname)
                                                        if filename.endswith('.story')]

def find_before_all(dirname):
    if not os.path.exists(dirname):
        return []
    sys.path.insert(0, dirname)
    modules = [__import__(filename[:-3]) for filename in os.listdir(dirname)
                                           if filename.endswith('.py')]
    del sys.path[0]
    before_all_meths = []
    for module in modules:
        steps = getattr(module, '_before_alls', [])
        before_all_meths.extend([step[1] for step in steps])
    return before_all_meths

