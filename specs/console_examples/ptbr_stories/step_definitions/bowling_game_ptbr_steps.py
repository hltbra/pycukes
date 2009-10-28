# coding: utf-8
from pycukes import *

class BowlingGame(object):
    score = 1
    def hit(self, balls):
        pass

@DadoQue('eu estou jogando boliche')
def start_game(contexto):
    contexto._bowling_game = BowlingGame()

@Quando('eu não acerto nenhuma bola')
def hit_no_balls(contexto):
    contexto._bowling_game.hit(0)

@Entao('eu tenho 0 pontos')
def i_have_zero_points(contexto):
    assert contexto._bowling_game.score == 0 
