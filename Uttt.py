from boards import *
from players import *

def main():
    players = []
    print("Choosing the players type:")
    for i in range(2):
        type = int(input("Type 1 for Human,2 for Noob or another number for Clumsy:"))
        mark = "X" if i%2 == 0 else "O"
        players.append( Human(mark) if type == 1 else(Noob(mark) if type==2 else (Clumsy(mark))) )
    game = Game(*players)
    game.playing()

if __name__ == "__main__":
    main()