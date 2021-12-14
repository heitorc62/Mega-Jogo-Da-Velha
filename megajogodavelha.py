class Tabuleiro():
    # ' ' -> nao marcado
    # 'X' -> player 1
    # 'O' -> jogador 2
    # '-' -> velha
    def __init__(self):
        self.grid = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        self.winner = -1
        self.filled = 0

    def check_winner(self):
        if self.winner != -1: return
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != " ": self.winner = self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != " ": self.winner = self.grid[0][2]
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != " ": self.winner = self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != " ": self.winner = self.grid[0][i]

        if(self.winner == "X"): self.grid = [["X", " ", "X"],[" ", "X", " "],["X", " ", "X"]]
        elif(self.winner == "O"): self.grid = [["O", "O", "O"],["O", " ", "O"],["O", "O", "O"]]
        elif self.filled == 9:
            self.winner = "-"
            self.grid = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

class Mega(Tabuleiro):
    def __init__(self):
        Tabuleiro.__init__(self)
        self.grid_mega = [[Mini(), Mini(), Mini()],[Mini(), Mini(), Mini()],[Mini(), Mini(), Mini()]]

    def play(self,wich,row,col,player):
        wich -= 1
        if not(0 <= wich <= 8) or self.grid_mega[wich // 3][wich % 3].winner != -1:
            print("Please, choose an empty and valid mini-board.")
            return -1
        row_mega = wich // 3
        col_mega = wich % 3
        if (self.grid_mega[row_mega][col_mega].play(row, col, player) == -1): return -1
        self.grid_mega[row_mega][col_mega].check_winner()
        if self.grid_mega[row_mega][col_mega].winner != -1:
            self.grid[row_mega][col_mega] = self.grid_mega[row_mega][col_mega].winner
            self.filled += 1
        self.check_winner()
        return 0

    def show(self):
        for i in range(3):
            print("         |         |         ")
            for j in range(3):
                for k in range(3):
                    if k < 2 : end =  "  |"
                    else: end =""
                    print(f"  {self.grid_mega[i][k].grid[j][0]}|{self.grid_mega[i][k].grid[j][1]}|{self.grid_mega[i][k].grid[j][2]}",end=end)
                print()
            if(i!= 2): print("_________|_________|_________")
            else:
                print("         |         |         ")
             
    
class Mini(Tabuleiro):
    def __init__(self):
        Tabuleiro.__init__(self)
    
    def play(self,row,col,player):
        row -= 1
        col -= 1
        if self.grid[row][col] == " " and 0 <= row <= 2 and 0 <= col <= 2:         
            self.grid[row][col] = player
            self.filled += 1
            return 0
        else:
            print("Please, choose an empty and valid cell.")
            return -1

        
    def __str__(self):
        return (f" {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} \n {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} \n {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}")

def main():
    tab = Mega()
    jogador = 0
    while tab.winner == -1:
        tab.show()
        atual = "X" if jogador % 2 == 0 else "O" 
        print(f"Jogador {atual} : Qual sua jogada? Ex: 2 1 3 , para tabuleiro 2 linha 1 e coluna 3")
        grid, row, col =  [int(i) for i in input().split()]
        if(tab.play(grid,row,col,atual) == 0):
            jogador += 1
            tab.check_winner()
    tab.show()
    if tab.winner == "-":
        print("Deu Velha!!")
    else:
        print(f"O vencedor é: {tab.winner}")

if __name__ == "__main__":
    main()
