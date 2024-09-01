# Minesweeper
This program is a basic replica of the classic game Minesweeper.

# minesweeper_setup.txt
Text file that read_file function reads in order to set up the
board size and mine locations.

  Note : board size is unchangeable, mine locations are changeable.
  
A 1 represents a mine, a 0 represents a safe dig spot.

Example of minesweeper_setup.txt file -

5 # Num Columns

5 # Num Rows

1, 0, 0, 0, 0

1, 0, 0, 0, 0

0, 1, 0, 0, 0

0, 0, 0, 0, 1

1, 0, 0 ,0, 1

# minesweeper.py
Program to run minesweeper game.

To play :
  run the program
  user will be prompted in terminal
  enter desired dig location (Ex. "a1")
  continue until mine is hit
