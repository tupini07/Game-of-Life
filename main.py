#! /usr/lib/python
from Game import Game
'''
The universe of the Game of Life (invented by British mathematician John Horton Conway in 1970) 
is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two
possible states, alive or dead.
Every cell interacts with its eight neighbors, which are the cells that are horizontally, 
vertically, or diagonally adjacent. At each step in time, the following transitions occur:

    1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by overcrowding.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The above are the original rules defined by Conway when he first thought of the game, however there
are a lot of variations, even games that use other forms for their cells that are not squared.

This version of the 'Game' of life is a simple implementation in the python language, mainly for 
learning purposes. However if you'll like to change something or add something then you're welcome'd to
do so.

This 'project' features a Board class that is the representation of the actual board, the LifeNode
which is what we know as cell, the Injector, that randomly toggles cells on and off, the Game class
that contains all the logic necessary for the game to work, and the GameRules which specify different
parameters for the game (like under-population, over-population, etc.).

I've done my best to keep it simple as possible (and making things much longer then necessary for 
the purpose of making it comprehensible to people who don't know how the game works) and to document
everything that needs documenting. However if you find something that you can explain better or that
needs to be explained and it is not then you are invited to do it :) .

If you want to know more visit: http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
'''

if __name__ == '__main__':
    game = Game()   
    ''' this is a R-pentomino, if you want to see it just uncomment this, and remember to turn
        injector off, your grid needs to be mode than 5 in size
    game.toggle_cel(3, 1)
    game.toggle_cel(2, 2)
    game.toggle_cel(4, 1)
    game.toggle_cel(3, 2)
    game.toggle_cel(3, 3)
    '''
    game.start()