import doctest
import subprocess
import os


if __name__ == '__main__':
    THIS_DIR = os.path.dirname(__file__) or '.'
    print '-' * 80
    for file in os.listdir(THIS_DIR):
        if file.endswith('.py') and file not in ['__init__.py', 'run_tests.py']:
            print 'Running %s doctest' % file
            doctest.testmod(__import__(file[:-3]),
                        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)

    print '-'*80
    print 'Running console examples'
    subprocess.call('cd %s/console_examples; sh run_examples.sh' % THIS_DIR, shell=True)
