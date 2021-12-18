import random

from boards import *
import numpy as np

class Player():
    def __init__ (self, team):
        self.team = team
        if team != 'X' and team != 'O':
            print("Choose a valid team (X or O)")
    
    def play(self, game, tab_num, row, col, team):
        assert(team == "X" or team == "O"), "You have chosen invalid teams! The game will be interrupted."
        x = (tab_num - 1) * 9 + (row - 1) * 3 + col - 1
        game.positions = game.positions[~np.isin(game.positions, x)]
        return game.tab.play(tab_num, row, col, team)

class Human(Player):
    def __init__(self, team):
        Player.__init__(self, team)
    
    def play(self, game):
        print(f"Player {self.team} : What is your play? Ex: 2 1 3 -> mini-board 2, row 1 and column 3")
        play = [int(i) for i in input().split()]
        if len(play) != 3:
            print("Please, make an valid play")
            return -1
        tab_num, row, col = play
        return Player.play(self, game, tab_num, row,col, self.team)  

        
class Clumsy(Player):
    def __init__(self, team):
        Player.__init__(self, team)
    
    def play(self, game):
        chosen = random.choice(game.positions)
        col = chosen % 3 + 1
        chosen //= 3
        row = chosen % 3 + 1
        chosen //= 3
        tab_num = chosen + 1
        return Player.play(self, game, tab_num, row, col, self.team)

class Noob(Player):
    def __init__(self, team):
        Player.__init__(self, team)

    def play(self, game):
        chosen = game.positions[0]
        col = chosen % 3 + 1
        chosen //= 3
        row = chosen % 3 + 1
        chosen //= 3
        tab_num = chosen + 1
        return Player.play(self, game, tab_num, row, col, self.team)