'''
Aidan Alexander
This program creates a basic copy of minesweeper.
'''

def read_file(file_name):
    '''
    This function reads a file (minesweeper_parameters.txt)
    and then creates a list representing a grid for minsweeper.
    A "X" represents a mine and a 0 represents a safe spot.
    Args:
        file_name: string; name of file to open
    Returns:
        grid: list; 2D list containing the mapping
                    of mines and safe spots
    '''
    file = open(file_name, "r")
    grid = []
    width = int(file.readline())
    height = int(file.readline())
    # Iterate over remaining lines in file
    for line in file:
        grid.append(line.split(","))
    # Iterate over each item in grid and strip
    # all extra spaces or newline characters
    for i in grid:
        for j in range(len(i)):
            i[j] = i[j].strip()
            if i[j] == '1':
                i[j] = 'X'
    return grid

def make_empty_grid(grid):
    '''
    This function creates an empty list that
    mirrors the size of the initial list (grid)
    Args:
        grid: list; 2D list containing the mapping
                    of mines and safe spots
    Returns:
        player_grid: list; 2D list mirroring the size
                           of grid containg only empty
                           squares
    '''
    player_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[i])):
            new_row.append(' ')
        player_grid.append(new_row)
    return player_grid

def update_grid(grid):
    '''
    This function takes a 2D list (grid), and replaces
    every 0 with the number of adjacent mines.
    Args:
        grid: list; 2D list containing the mapping
                    of mines and safe spots
    Returns:
        grid: list; mutated 2D list containing the mapping
                    of mines, and the number of mines adjacent
                    to each square
    '''
    # Create list of coords to check around each square
    surround_coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), \
                (0, 1), (1, -1), (1, 0), (1, 1)]
    # Iterate over each square in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            mines = 0
            # Not checking surrounding if the square is a bomb
            if grid[i][j] == "X":
                grid[i][j] = "X"
            else:
                # Iterate through each coord in surround_coords
                for x, y in surround_coords:
                    # Create the coord to check around grid[i][j]
                    row = i + x
                    col = j + y
                    # Check if that coord is in the limits of the grid
                    if 0 <= row < len(grid) and 0 <= col < len(grid[i]):
                        # If the surrounding coord is a mine
                        if grid[row][col] == "X":
                            # Add a count to mines
                            mines += 1
                            # Replace grid[i][j] with surrounding mines count
                            grid[i][j] = str(mines)
    return grid

def dig(grid, coord, player_grid):
    '''
    This function implements player movement.
    Args:
        grid: list; 2D list containing the mapping of mines
                    and the number of mines adjacent to each sqaure
        coord: string; coordinate the player wishes to dig at
        player_grid: list; the grid that the player sees once
                           their move is made
    Returns:
        None
    '''
    # Column the user wishes to dig in
    col = ord(coord[0]) - 97
    # Row the user wishes to dig in
    row = len(grid) - 1 - int(coord[1:])
    # Checking to see if the player's move is within bounds
    if 0 <= col < len(grid) and 0 <= row < len(grid[0]):
        # Swapping values from the grid to the user's grid
        # at the move index
        player_grid[row][col] = grid[row][col]
        # Checking if the player's move is not a mine
        if player_grid[row][col] != "X":
            for i in range(len(grid)):
                # Checking all coords surrounding the player's move
                if i == (row-1) or i == row or i == (row+1):
                    for j in range(len(grid[i])):
                        if j == (col-1) or j == col or j == (col+1):
                            # Revealing adjacent squares
                            if grid[i][j] != "X":
                                player_grid[i][j] = grid[i][j]
    print_grid(player_grid)

def count_total_moves(grid, player_grid):
    '''
    This function counts how many more moves the player can make.
    Args:
        grid: list; 2D list containing the mapping of mines
                    and the number of mines adjacent to each sqaure
        player_grid: list; represents the grid that the player sees
    Returns:
        not_revealed - mines: integer; number of moves the player has left
    '''
    # Number of mines
    mines = 0
    # Number of squares not revealed by player
    not_revealed = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Checking if the square contains a mine
            if grid[i][j] == "X":
                mines += 1
    for i in range(len(player_grid)):
        for j in range(len(player_grid[i])):
            # Checking if the square has been revealed by the player
            if player_grid[i][j] == " ":
                not_revealed += 1
    # Returning the number of squares not revealed minus the number of mines
    return not_revealed - mines

def print_grid(player_grid):
    '''
    This function prints out the grid for the player to see
    Args:
        player_grid: list; represents the grid that the player sees
    Returns:
        None
    '''
    # Alphabet string for bottom of grid spaces
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(player_grid)):
        # Printing number representing row
        print('{:>2}'.format(len(player_grid)-1 - i), end = "")
        for j in range(len(player_grid[i])):
            # Printing each square
            print("[" + player_grid[i][j] + "]", end = "")
            if j == len(player_grid)-1:
                print("")
    print("   ", end = "")
    for j in range(len(player_grid[0])):
        # Printing letters at bottom of grid to represent column
        print(alphabet[j] + "  ", end = "")
    print("")

def determine_game_status(grid, player_grid):
    '''
    This function determines if the game is over or ongoing.
    Args:
        grid: list; 2D list containing the mapping of mines
                    and the number of mines adjacent to each sqaure
        player_grid: list; represents the grid that the player sees
    Returns:
        False: boolian; if the player has lost the game
        True: boolian; if the game is ongoing
    '''
    for i in range(len(player_grid)):
        for j in range(len(player_grid[i])):
            # Check if the player_grid contains an "X"
            if player_grid[i][j] == "X":
                # If True, then the player has lost
                return False
    # Check if there are any moves left that the player can make
    if count_total_moves(grid, player_grid) == 0:
        return False
    # If none of these conditions are True, gamestate is ongoing
    else:
        return True

if __name__ == '__main__':
    grid = read_file("minesweeper_parameters.txt")
    user_view = make_empty_grid(grid)
    update_grid(grid)
    # moves = ["a2", "b1", "d0", "d1", "e3", "c3", "c4"]
    index = 0
    moves = []
    while determine_game_status(grid, user_view):
        moves.append(input("Where would you like to dig?\n"))
        dig(grid, moves[index], user_view)
        index += 1