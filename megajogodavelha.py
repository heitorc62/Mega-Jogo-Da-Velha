class tabuleiro():
    # 0 -> nao marcado
    # 1 -> player 1
    # 2 -> jogador 2
    def __init__(self):
        self.grid = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        self.winner = -1
        self.filled = 0

    def check_winner(self):
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != 0 and self.grid[0][0] != "draw":
            self.winner = self.grid[0][0]
            return
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != 0 and self.grid[0][2] != "draw":
            self.winner = self.grid[0][0]
            return
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != 0 and self.grid[i][0] != "draw":
                self.winner = self.grid[i][0]
                return
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != 0 and self.grid[0][i] != "draw":
                self.winner = self.grid[0][i]
                return
        
        if self.filled == 9:   # VELHA
            self.winner = "draw"
        
    def __str__(self):
        return (f" {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} \n {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} \n {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}")

class mega(tabuleiro):
    def __init__(self):
        tabuleiro.__init__(self)
        self.grid_mega = [[mini(), mini(), mini()],[mini(), mini(), mini()],[mini(), mini(), mini()]]

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

    # def show(self):
    #     for linha in self.grid_mega:
    #         for tab in linha:
    #             print(tab)
    #             print()
    #         print()

    def show(self):
        for i in range(3):
            if i != 0: print()
            for j in range(3):
                print(f"{self.grid_mega[i][0].grid[j]}  |  {self.grid_mega[i][1].grid[j]}  |  {self.grid_mega[i][2].grid[j]}")
            if(i!= 2): print("_____________________________________")
             
    
class mini(tabuleiro):
    def __init__(self):
        tabuleiro.__init__(self)
    
    def play(self,row,col,player):
        row -= 1
        col -= 1
        if self.grid[row][col] == 0 and 0 <= row <= 2 and 0 <= col <= 2:         
            self.grid[row][col] = player
            self.filled += 1
            return 0
        else:
            print("Please, choose an empty and valid cell.")
            return -1

        
    # def __str__(self):
    #     return (f" {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} \n {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} \n {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}")
    # def __str__(self):
    #     return tabuleiro.__str__(self)

def main():
    tab = mega()
    jogador = 0
    while tab.winner == -1:
        tab.show()
        atual = 2 if jogador % 2 == 0 else 1 
        print(f"Jogador {atual} : Qual sua jogada? Ex: 2 1 3 , para tabuleiro 2 linha 1 e coluna 3")
        grid, row, col =  [int(i) for i in input().split()]
        if(tab.play(grid,row,col,atual) == 0):
            jogador += 1
            tab.check_winner()
    tab.show()
    if tab.winner == "draw":
        print("Deu Velha!!")
    else:
        print(f"O vencedor é: {tab.winne}")

if __name__ == "__main__":
    main()
