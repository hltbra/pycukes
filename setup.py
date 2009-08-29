from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pycukes',
      version=version,
      description="A Cucumber-like BDD framework built on top of Pyhistorian",
      long_description=open('README.rst').read(),
      classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Documentation',
          'Topic :: Software Development :: Testing',],
      keywords='bdd behaviour behavior pyhistorian story',
      author='Hugo Lopes Tavares',
      author_email='hltbra@gmail.com',
      url='http://github.com/hugobr/pycukes',
      license='MIT License',
      packages=['pycukes', 'pycukes.specs', 'pycukes.specs.steps',],
      package_dir={'pycukes': 'src',
                   'pycukes.specs': 'src/specs',
                   'pycukes.specs.steps': 'src/specs/steps',
                   'pycukes.specs.text_specs': 'src/specs/text_specs',
                   'pycukes.specs.console_examples': 'src/specs/console_examples',},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'story_parser',
          'pyhistorian',
          # -*- Extra requirements: -*-
      ],
      entry_points= {
            'console_scripts': ['pycukes = pycukes.console:main']},
      )
