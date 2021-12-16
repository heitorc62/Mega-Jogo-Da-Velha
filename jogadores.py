import random
import sys

from numpy.core.fromnumeric import choose
from megajogodavelha import *
import numpy as np

class Game():
    def __init__(self, player1, player2):
        self.positions = np.arange(0, 81)
        self.tab = Mega()
        self.players = [player1, player2]
    
    def reset(self):
        self.positions = np.arange(0, 81)
        self.tab = Mega()

        
    def playing(self):
        step = 0
        valid = 1  
        while self.tab.winner == -1: 
            if valid: self.tab.show()
            turn = step % 2
            if self.players[turn].play(self) == 0:
                step += 1
                valid = 1
            else: valid = 0
            self.tab.check_winner()
            print()
        self.show_winner()
        
    def show_winner(self):
        self.tab.show()
        if self.tab.winner == '-':
            print("Draw!!")
        else:
            print(self.tab.winner)
        

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

def main():
    player1 = Clumsy("X")
    player2 = Clumsy("O")
    game = Game(player1, player2)
    game.playing()

if __name__ == "__main__":
    main()