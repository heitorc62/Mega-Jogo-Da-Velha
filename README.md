# Ultimate Tic-Tac-Toe
That's a [Ultimate Tic-Tac-Toe](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe) game implementation in Python with some rule changes.

## Summary Table
* [Contributors](#contributors)
* [Requirements](#requirements)
* [Game Rules changes](#game-rules-changes)
* [Boards and Game Classes](#boards-and-game-classes)
* [Players Classes](#players-classes)
* [If you want to use our classes](#if-you-want-to-use-our-classes)
* [Play the game](#play-the-game)

## Contributors

Participants |nUSP
-- | --
João Guilherme Alves Santos | 11819560
Heitor Barroso Cavalcante | 12566101
Nathan Luiz Bezerra Martins | 11805061

## Requirements
Some player classes are using [NumPy](https://numpy.org/install/)'s arrays, you need to install it.\
Moreover, if you want to run our tests you have to install [Pytest](https://docs.pytest.org/en/6.2.x/getting-started.html). If you want to have more details about the test, install [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html#installation).

## Game Rules changes
The difference between the original Ultimate Tic Tac Toe's game and this one is that every turn the player can choose any local board to play.
In this game, you can't play in a local board that already has a winner.

## Boards and Game Classes
This repository has three boards classes and a Game class:
#### Board
Generic board class, used as a base class of the other two.
* Methods:
``` py 
def check_winner(self)
```
The **check_winner** method checks if the board has a winner or has no more valid moves.

#### Mini
This class represents the local board.
* Methods:
```py
def play(self,row,col,player)
```
The **play** method makes plays in the board. The arguments **row** is the row that you want to make your play *(1 <= row <= 3)*, **col** is the column you want to play *(1<= col <= 3)* and **player** is your team's mark ("X" or "O"). 


#### Mega
This class represents the global board. The Mega board has a attribute called **grid_mega** that is a 3x3 list of local boards where the plays will happen.
* Methods:
```py
def play(self,wich,row,col,player)
```
Almost the same as Mini's play, but this one has a argument called **wich** that represents the local board that you want to play *( 1 <= wich <= 9)*.
```py
def show()
```
The **show** method prints the global board with all the local boards inside.


Example:

![image](https://user-images.githubusercontent.com/85133393/146601927-466582e2-f75b-458f-be4a-603e7f56571d.png)\
When a local board has a X shape, the X player has won that local board. Same to local board with O shape.

#### Game
This class represents an Ultimate Tic-Tac-Toe game.
* Initialize:
To initialize a Game class you have to pass two [players](#players-classes) as arguments. For example:
```py
game = Game(player1, player2)
```
* Methods:
```py
def reset(self)
```
The **reset** method cleans the entire game and keeps the players that were playing.
```py
def playing(self)
```
The **playing** method runs the entire game and stops when someone won the game or all cell's are filled.
```py
def show_winner(self)
```
The **show_winner** method prints the winner of the game or when the game tied.

## Players Classes
This repository has three player types:
* Clumsy\
Makes random plays.

* Noob\
Always play in the first empty position in a valid board.

* Human\
Reads plays in the standard input.
 
### Initialize a player
To initialize a player class you have to pass "X" or "O" as argument to choose your team mark. For example:
```py
player1 = Noob("X")
```

## If you want to use our classes 

#### To use our classes in python's interative mode:
Firstly, being in the same directory of the files in this repository, you will have to type "python3" in your console.\
Then, you'll have entered in python's interative mode.
Now, the user has to import "boards" and "players", trailing the following steps:
```sh
>>> from boards import *
>>> from players import *
```
Then, you should define the players, for example, in a Human x Clumsy mode:
```sh
>>> player1 = Human("X")
>>> player2 = Clumsy("O")
```
Now, the only thing left is to play!
```sh
>>> game = Game(player1, player2)
>>> game.playing
```
#### Yet, if you want to use python's scripting mode to use our classes, that is possible too.
All you'll have to do is, create a .py file and type the following lines (in this example, the Noob x Human mode is shown):

```py
from boards import *
from players import *

player1 = Noob("X")
player2 = Human("O")
game = Game(player1, player2)
game.playing()
```
## Play the game
The game is in **Uttt.py**. You just need run the file and the game starts.\
At first, it will ask the type of the players that will play. *You have to type 1 for Human, 2 for Noob, or another number for Clumsy.*\
After that, the game will start.
***Enjoy!***
