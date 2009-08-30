from finder import find_steps_modules, find_text_specs
from runner import StoryRunner
from optparse import OptionParser
import sys
import os

def pycukes_console(stories_dir, steps_dir, output, colored=False):
    modules = find_steps_modules(steps_dir)
    for spec in find_text_specs(stories_dir):
        StoryRunner(spec, output, colored=colored, modules=modules).run()


def main():
    steps_modules = []
    files = []
    stories_dirname = 'stories'
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            break
        files.append(arg)
        stories_dirname = os.path.dirname(arg) or '.'

    parser = OptionParser()
    parser.add_option('-s', '--stories-dir', default=None, dest='stories_dir')
    parser.add_option('-t', '--steps-dir', default=None, dest='steps_dir')
    parser.add_option('-n', '--no-colors', default=None, action='store_true', dest='no_colors')
    parser.add_option('-c', '--colored', default=None, action='store_true', dest='colored')
    parser.add_option('-l', '--language', default='en-us', dest='language')
    values, args = parser.parse_args()

    try:
        if values.stories_dir:
            files.extend([values.stories_dir+'/'+filename for filename in os.listdir(values.stories_dir)
                            if filename.endswith('.story')])
            stories_dirname = values.stories_dir
        elif files == []:
            files.extend([stories_dirname+'/'+filename for filename in os.listdir(stories_dirname)
                                              if filename.endswith('.story')])

        steps_modules = find_steps_modules(values.steps_dir or stories_dirname+'/step_definitions')
    except OSError:
        pass

    colored = True
    if values.no_colors and not values.colored:
        colored = False

    for index, story in enumerate(files):
        StoryRunner(open(story).read(),
                    sys.stdout,
                    colored=colored,
                    modules=steps_modules,
                    language=values.language).run()
        if index < len(files)-1:
            sys.stdout.write('\n\n')
