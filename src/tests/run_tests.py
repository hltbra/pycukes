import doctest
import os

THIS_DIR = os.path.dirname(__file__)
MODULES = []
for file in os.listdir(THIS_DIR):
    if file.endswith('.py') and file != 'run_tests.py':
        MODULES.append(__import__(file[:-3]))

if __name__ == '__main__':
    print '-' * 80
    for module in MODULES:
        print 'Running %s doctest' % module.__name__
        doctest.testmod(module,
                        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)
