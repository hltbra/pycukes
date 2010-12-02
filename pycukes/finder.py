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


def _find_hook_steps(name, dirname):
    sys.path.insert(0, dirname)
    modules = [__import__(filename[:-3]) for filename in os.listdir(dirname)
                                           if filename.endswith('.py')]
    del sys.path[0]
    before_all_meths = []
    for module in modules:
        steps = getattr(module, name, [])
        before_all_meths.extend([step[1] for step in steps])
    return before_all_meths


def find_before_all(dirname):
    return _find_hook_steps('_before_alls', dirname)


def find_after_all(dirname):
    return _find_hook_steps('_after_alls', dirname)


def find_before_each(dirname):
    return _find_hook_steps('_before_eachs', dirname)

def find_after_each(dirname):
    return _find_hook_steps('_after_eachs', dirname)
