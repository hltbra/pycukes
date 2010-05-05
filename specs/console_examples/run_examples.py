from cStringIO import StringIO
from should_dsl import should_be
import subprocess
import os
import sys


bowling_game_output = open('bowling_game_output').read()
bowling_game_pending_output = open('bowling_game_pending_output').read()
bowling_game_without_colors_output = open('bowling_game_without_colors_output').read()
bowling_game_using_feature_injection_output = open('bowling_game_using_feature_injection_output').read()
calculator_output = open('calculator_output').read()
bowling_game_ptbr_output = open('bowling_game_ptbr_output').read()
bowling_and_calculator_output = '\n'.join([bowling_game_output,
                                             calculator_output])
all_outputs = '\n'.join([bowling_game_output,
                           bowling_game_using_feature_injection_output,
                           calculator_output,])
hooks_output = open('hooks_output').read()

INPUTS_AND_OUTPUTS = [('pycukes stories/bowling_game.story',
                            bowling_game_output, 1),
                      ('pycukes stories/bowling_game.story stories/calculator.story',
                            bowling_and_calculator_output, 1),
                      ('pycukes',
                            all_outputs, 1),
                      ('pycukes --stories-dir=features',
                            '\n', 0),
                      ('pycukes --stories-dir=stories_dir1',
                            bowling_game_output.replace('stories', 'stories_dir1'), 1),
                      ('pycukes --stories-dir=stories_dir1 --steps-dir=stories',
                            bowling_game_pending_output, 0),
                      ('pycukes stories/bowling_game.story --no-colors',
                            bowling_game_without_colors_output, 1),
                      ('pycukes stories/bowling_game.story --colored',
                            bowling_game_output, 1),
                      ('pycukes stories/bowling_game.story --colored --no-colors',
                            bowling_game_output, 1),
                      ('pycukes stories/bowling_game_using_feature_injection.story',
                            bowling_game_using_feature_injection_output, 1),
                      ('pycukes ptbr_stories/bowling_game_ptbr.story --language pt-br',
                            bowling_game_ptbr_output, 1),
                      ('cd stories && pycukes bowling_game.story',
                            bowling_game_output.replace('stories', '.'), 1),
                      ('pycukes stories_with_hooks/messages.story -n',
                            hooks_output, 0)
                      ]

def remove_all_pycs(dirname):
    for filename in os.listdir(dirname):
        filename = os.path.join(dirname, filename)
        if filename.endswith('.pyc'):
            os.remove(filename)
        elif os.path.isdir(filename):
            remove_all_pycs(filename)

def run_examples():
    exceptions = []
    failures = 0
    for input_command, expected_output, exit_code in INPUTS_AND_OUTPUTS:
        print '\t', input_command,
        remove_all_pycs(os.path.abspath(os.path.dirname(__file__)))
        try:
            process = subprocess.Popen(input_command,
                                   stdout=subprocess.PIPE,
                                   shell=True)
            out = process.communicate()[0]+'\n'
            out |should_be.equal_to| expected_output
            process.wait() |should_be.equal_to| exit_code
            print '- OK'
        except AssertionError, e:
            print '- FAIL'
            print e
            failures += 1
    return failures


if __name__ == '__main__':
    print '-'*80
    print 'Running console examples'
    sys.exit(run_examples())
