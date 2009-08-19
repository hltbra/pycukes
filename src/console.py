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
        files = sys.argv[1:]
    else:
        files = ['specs/'+filename for filename in os.listdir('specs')
                              if filename.endswith('.story')]
    for index, story in enumerate(files):
        StoryRunner(open(story).read(),
                    sys.stdout,
                    colored=True,
                    modules=find_steps_modules('steps')).run()
        if index < len(files):
            sys.stdout.write('\n\n')
