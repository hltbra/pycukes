from pycukes import *


class BowlingGame(object):
    score = 1
    def hit(self, balls):
        pass


@BeforeAll
def start_game(context):
    context._bowling_game = BowlingGame()
    context._bowling_game.score = 0
