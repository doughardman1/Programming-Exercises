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

print(valid(puzzle, 5, (2,0)))
