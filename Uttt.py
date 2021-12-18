from boards import *
from players import *

def main():
    player1 = Noob("X")
    player2 = Human("O")
    game = Game(player1, player2)
    game.playing()

if __name__ == "__main__":
    main()