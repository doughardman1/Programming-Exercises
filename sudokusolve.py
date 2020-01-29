def valid(puzzle, number, cell):
    '''
    Takes a sudoku puzzle as a list containing 9 lists which hold numbers along the
    rows of the puzzle. Checks to see if a given number can be validly placed in a
    cell by checking the row, column and 3x3 box that the cell is in in the puzzle.
    Returns False if number placement is invalid and True if it is valid.
    '''

    # Check row
    for i in range(len(puzzle[0])):
        if puzzle[cell[0]][i] == number:
            return False
        
    # Check row
    for i in range(len(puzzle[1])):
        if puzzle[i][cell[1]] == number:
            return False

    # Check 3x3 box
    x_start = cell[0] - cell[0] % 3
    y_start = cell[1] - cell[1] % 3

    for i in range(3):
        for j in range(3):
            if puzzle[x_start + i][y_start + j] == number:
                return False
            
    return True


def find_empty_cell(puzzle, position):
    '''
    Takes a puzzle and returns True if an empty/unassigned cell (where value == 0)
    is found. If no empty cells are present then False is returned. a position list
    variable is kept which gets updated with the position of the empty cell from the
    solve function.

    '''
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                position[0] = i
                position[1] = j
                return True
    return False


def solve(puzzle):
    '''
    Solves a sudoku puzzle recursively using a Backtracking approach.
    Returns True if a solution is found, otherwise returns False and the function is called
    recursively until the end of the puzzle is reached.
    '''
    position = [0,0] #init position list with the starting coordinates (0,0)

    # if no empty cell is found then the puzzle is finished
    if (find_empty_cell(puzzle, position) == False):
        return True

    # set row and col to be the respective positions found from the find_empty_cell function
    row = position[0]
    col = position[1]

    # iterate through numbers 1 to 9
    for number in range(1,10):
        if (valid(puzzle, number, (row, col)) == True):
            puzzle[row][col] = number # assign cell number
            if (solve(puzzle) == True): 
                return True # return True if successful 
            puzzle[row][col] = 0 # otherwise reset cell to be empty again
    return False # forces Backtracking / recursive function

if __name__=="__main__":
    
    puzzle = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

    if (solve(puzzle) == True):
        print('solved!')
        # print finished puzzle
        for i in range(9):
            print(puzzle[i])
            
    else:
        print('Couldn\'t solve')
