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

@Then('I have not printed HELLO WORLD')
def not_printed_hello_world(context):
    assert context._printed_hello_world == False

@Then('I have $value points')
def i_have_zero_points(context, value):
    assert context._bowling_game.score == int(value), context._bowling_game.score


