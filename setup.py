from setuptools import setup, find_packages
import sys, os

version = '0.2'
README = open('README.rst').read()

setup(name='pycukes',
      version=version,
      description="A Cucumber-like BDD framework built on top of Pyhistorian",
      long_description=README,
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
                   'pycukes.specs': 'specs',
                   'pycukes.specs.steps': 'specs/steps',
                   'pycukes.specs.text_specs': 'specs/text_specs',
                   'pycukes.specs.console_examples': 'specs/console_examples',},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'story_parser>=0.1.2',
          'should_dsl',
          'pyhistorian>=0.6.8',
          # -*- Extra requirements: -*-
      ],
      entry_points= {
            'console_scripts': ['pycukes = pycukes.console:main']},
      )
