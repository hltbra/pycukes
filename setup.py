from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pycukes',
      version=version,
      description="A text-style BDD framework built on top of Pyhistorian",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='bdd behaviour behavior pyhistorian story',
      author='Hugo Lopes Tavares',
      author_email='hltbra@gmail.com',
      url='http://github.com/hugobr/pycukes',
      license='MIT',
      packages=['pycukes', 'pycukes.tests', 'pycukes.tests.scenarios',],
      package_dir={'pycukes': 'src',  'pycukes.tests': 'src/tests', 'pycukes.tests.scenarios': 'src/tests/scenarios'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'story_parser',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
