from finder import find_steps_modules, find_text_specs
from runner import StoryRunner
import sys
import os

def pycukes_console(specs_dir, steps_dir, output, colored=False):
    modules = find_steps_modules(steps_dir)
    for spec in find_text_specs(specs_dir):
        StoryRunner(spec, output, colored=colored, modules=modules).run()

def main():
    if len(sys.argv) > 1:
        for index, arg in enumerate(sys.argv[1:]):
            StoryRunner(open(arg).read(),
                        sys.stdout,
                        colored=True,
                        modules=find_steps_modules(os.path.dirname(arg)+'/../steps')).run()
            if index < len(sys.argv[1:]):
                sys.stdout.write('\n\n')
    else:
        for index, filename in enumerate(os.listdir('specs')):
            if filename.endswith('.story'):
                StoryRunner(open('specs/'+filename).read(),
                    sys.stdout,
                    colored=True,
                    modules=find_steps_modules('steps')).run()
            if index < os.listdir('specs'):
                sys.stdout.write('\n\n')

