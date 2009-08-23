from finder import find_steps_modules, find_text_specs
from runner import StoryRunner
from optparse import OptionParser
import sys
import os

def pycukes_console(specs_dir, steps_dir, output, colored=False):
    modules = find_steps_modules(steps_dir)
    for spec in find_text_specs(specs_dir):
        StoryRunner(spec, output, colored=colored, modules=modules).run()


def main():
    steps_modules = []
    files = []
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            break
        files.append(arg)

    parser = OptionParser()
    parser.add_option('-s', '--specs-dir', default=None, dest='specs_dir')
    parser.add_option('-t', '--steps-dir', default=None, dest='steps_dir')
    parser.add_option('-n', '--no-colors', default=False, action='store_true', dest='no_colors')
    values, args = parser.parse_args()

    try:
        if values.specs_dir:
            files.extend([values.specs_dir+'/'+filename for filename in os.listdir(values.specs_dir)
                            if filename.endswith('.story')])
        elif files == []:
            files.extend(['specs/'+filename for filename in os.listdir('specs')
                                              if filename.endswith('.story')])

        steps_modules = find_steps_modules(values.steps_dir or 'steps')
    except OSError:
        pass

    for index, story in enumerate(files):
        StoryRunner(open(story).read(),
                    sys.stdout,
                    colored=not values.no_colors,
                    modules=steps_modules).run()
        if index < len(files)-1:
            sys.stdout.write('\n\n')
