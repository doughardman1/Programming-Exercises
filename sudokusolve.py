board = [
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
    # Check row
    for i in range(len(puzzle[0])):
        if puzzle[cell[0]][i] == number:
            return False
        
    # Check row
    for i in range(len(puzzle[1])):
        if puzzle[i][cell[1]] == number:
            return False

print(valid(board, 5, (0,2)))
