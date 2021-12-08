class tabuleiro():
    # 0 -> nao marcado
    # 1 -> player 1
    # 2 -> jogador 2
    def __init__(self):
        self.grid = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        self.winner = -1
        self.filled = 0

    def play(self,row,col,player):
        if self.grid[row][col] == 0:         
            self.grid[row][col] = player
            self.filled += 1
            return 0
        else:
            print("Please, choose an empty cell.")
            return -1

    def check_winner(self):
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != 0:
            self.winner = self.grid[0][0]
            return
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != 0:
            self.winner = self.grid[0][0]
            return
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != 0:
                self.winner = self.grid[i][0]
                return
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != 0:
                self.winner = self.grid[0][i]
                return
        
        if self.filled == 9:   # VELHA
            self.winner = 0    
        
    def __str__(self):
        return (f" {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} \n {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} \n {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}")

def main():
    tab = tabuleiro()
    jogador = 0
    while tab.winner == -1:
        print(tab)
        atual= 2 if jogador % 2 == 0 else 1 
        print("Qual sua jogada? Ex: 0 2 , para linha 0 e coluna 2")
        row, col =  [int(i) for i in input().split()]
        if(tab.play(row,col,atual) == 0):
            jogador += 1
            tab.check_winner()

if __name__ == "__main__":
    main()
