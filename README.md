<h1>Game of Life</h1>

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

<h2> ToDo </h2>
This is a list of things that will be nice to do some day.
<ul>
<li>Some way to make it easier to input patterns like reading them from a file or enabling mouse clics</li>
<li>A way to pause/stop the game, currently it runs a definite number of generations before stopping</li>
<li>Give it come colors</li>
<li>Display the age of each cell, maybe using colors to indicate youngest/oldest</li>
<li>Make a real interface, for the moment it works just in the terminal and it'll be nice to have a GUI (maybe TkInter?)
</ul>

<h2>How To Run</h2>
It's very simple to run this program, the only thing you need to do is go to your console and navigate to the project's folder, then:

    python main.py
    
And that's it! Remember to edit the GameRules file if you want some special parameters and the main.py file to set any initial state you would like.
