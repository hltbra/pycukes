PyCukes
=======

PyCukes is a Cucumber-like BDD tool built on top of Pyhistorian.
PyCukes was created to fill the gap pyhistorian left, so with it is possible to talk to your stakeholders first with text files, instead of simple understendable python files like Pyhistorian.


Usage
=====

First, make sure you have installed story_runner, pyhistorian and pycukes.
By default, if you just call ``pycukes`` from your command line into some dir, it will look for a ``stories`` dir (expecting your stories files are there) and then look for a ``step_definitions`` dir (expecting your step definitions are there).
Each story file by convention ends with .story, like ``calculator.story`` and each step definition should end with steps.py, like ``calculator_steps.py``.

So, lets say you have the directory tree::

 |-- calculator
    `-- stories
        |-- calculator.story
        `-- step_definitions
            `-- calculator_steps.py


To run your stories, you can simple call::

    $ pycukes

Or if you can specify exactly what stories run::
    
    $ pycukes stories/calculator.story


Parameters
==========
::

    -s or --stories-dir  --  specify your stories directory
    -t or --steps-dir  --  specify your step definitions directory
    -n or --no-colors  --  tells pycukes not to show colored output
    -c or --colored (default) -- tells pycukes to show colored output
    -l or --language (en-us by default) -- specify your story language [en-us and pt-br are supported]


Real Example
============

Directory tree::

    hugo@hugo-laptop:~/app$ tree
    .
    `-- stories
        |-- bowling_game.story
        `-- step_definitions
            `-- bowling_game_steps.py


Content of bowling_game.story file::

    hugo@hugo-laptop:~/app$ cat stories/bowling_game.story 
    Story: Bowling Game
      As a bowling player
      I want to play bowling online
      So that I can play with everyone in the world
      
        Scenario 1: Gutter Game
          Given I am playing a bowling game
          When I hit no balls
          Then I have 0 points

Content of bowling_game_steps.py::

    hugo@hugo-laptop:~/app$ cat stories/step_definitions/bowling_game_steps.py
    from pycukes import *

    class BowlingGame(object):
        score = 1
        def hit(self, balls):
            pass


    @Given('I am playing a bowling game')
    def start_game(context):
        context._bowling_game = BowlingGame()

    @When('I hit no balls')
    def hit_no_balls(context):
        context._bowling_game.hit(0)

    @Then('I have 0 points')
    def i_have_zero_points(context):
        assert context._bowling_game.score == 0 

Running::

    hugo@hugo-laptop:~/app$ pycukes stories/bowling_game.story 
    Story: Bowling Game
      As a bowling player
      I want to play bowling online
      So that I can play with everyone in the world

      Scenario 1: Gutter Game
        Given I am playing a bowling game   ... OK
        When I hit no balls   ... OK
        Then I have 0 points   ... FAIL

      Failures:
        File "stories/step_definitions/bowling_game_steps.py", line 19, in i_have_zero_points
          assert context._bowling_game.score == 0
        AssertionError


      Ran 1 scenario with 1 failure, 0 errors and 0 pending steps
