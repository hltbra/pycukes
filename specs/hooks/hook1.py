from pycukes import *
from should_dsl import *


class BowlingGame(object):
    score = 1
    def hit(self, balls):
        pass


@BeforeAll
def start_game(context):
    context._bowling_game = BowlingGame()
    context._bowling_game.score = 0
    context._printed_hello_world = False


@BeforeEach
def score_2(context):
    context._bowling_game.score += 2


@AfterAll
def print_hello_world(context):
    print 'HELLO WORLD'
    context._printed_hello_world = True
