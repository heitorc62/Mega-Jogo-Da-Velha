from megajogodavelha import *
from jogadores import *
import pytest
import sys
from teste_velha import velha
from tud_test_base import set_keyboard_input, get_display_output

class Test_Board():
    def test_check_winner(self):
        tab = Board()
        tab.grid = [["X", "X", "X"],["O", "O", "X"],["O", "X", "O"]]
        tab.check_winner()
        assert(tab.winner == "X"), "Error: win in the first row"

        tab = Board() 
        tab.grid = [["O", " ", " "],[" ", "O", " "],[" ", " ", "O"]]
        tab.check_winner()
        assert(tab.winner == "O"), "Error: win in num1 diagonal"

        tab = Board()
        tab.grid = [["", " ", "X"],[" ", "X", " "],["X", " ", " "]]
        tab.check_winner()
        assert(tab.winner == "X"), "Error: win in num2 diagonal"

        tab = Board()
        tab.grid = [["O", " ", " "],["O", " ", " "],["O", " ", " "]]
        tab.check_winner()
        assert(tab.winner == "O"), "Error: win in the first column"

        tab = Board()
        tab.grid = [[" ", " ", " "],["X", "X", "X"],[" ", " ", " "]]
        tab.check_winner()
        assert(tab.winner == "X"), "Error: win in the second row"

        tab = Board()
        tab.grid = [[" ", " ", " "],[" ", " ", " "],["O", "O", "O"]]
        tab.check_winner()
        assert(tab.winner == "O"), "Error: win in the third row"
        
        tab = Board()
        tab.grid = [[" ", "X", " "],[" ", "X", " "],[" ", "X", " "]]
        tab.check_winner()
        assert(tab.winner == "X"), "Error: win in the second column"

        tab = Board()
        tab.grid = [[" ", " ", "O"],[" ", " ", "O"],[" ", " ", "O"]]
        tab.check_winner()
        assert(tab.winner == "O"), "Error: win in the third column"

        tab = Board()
        tab.filled = 9
        tab.grid = [["X", "O", "X"],["O", "X", "O"],["O", "X", "O"]]
        tab.check_winner()
        assert(tab.winner == "-"), "Error: draw"
        
class Test_Mini():
    def test_play(self):
        tab = Mini()
        assert(tab.play(1,1,"X") == 0)
        assert(tab.grid[0][0] == "X")
        assert(tab.play(0,0,"X") == -1)
        assert(tab.play(5,4,"X") == -1) 

class Test_Mega():
    def test_play(self):
        tab = Mega()
        assert(tab.play(1,1,1,"X") == 0)
        assert(tab.grid_mega[0][0].grid[0][0] == "X")
        tab= Mega()
        assert(tab.play(0,0,0,"X") == -1)
        assert(tab.play(-1,5,4,"X") == -1)
    
# class Test_Game():
#     def test_Game(self):
#         p0 = Noob("O")
#         p1 = Clumsy("X")
#         game = Game(p0, p1)
#         game.playing()
#         assert(game.tab.winner == "O")

#         # set_keyboard_input(velha)
#         p0 = Human("O")
#         p1 = Human("X")
#         game1 = Game(p0, p1)       
#         for i in range(81):
#             set_keyboard_input(velha[i])
#             output = get_display_output()
#         game1.playing()
#         # output = get_display_output()

if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))


