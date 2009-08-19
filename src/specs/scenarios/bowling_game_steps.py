from pycukes import *

class BowlingGame(object):
    score = 1
    def hit(self, balls):
        pass


@Given('I am playing a bowling game')
def start_game(self):
    self._bowling_game = BowlingGame()

@When('I hit no balls')
def hit_no_balls(self):
    self._bowling_game.hit(0)

@Then('I have 0 points')
def i_have_zero_points(self):
    assert self._bowling_game.score == 0 
