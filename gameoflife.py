# Game of Life
import numpy as np

class Grid:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.grid = np.random.choice(a=[0, 1], size=(self.cols, self.rows))

    def print_grid(self):
        print(self.grid)

    def evolve(self):
        x = 0
        y = 0

        next = self.grid #replicate current grid for next step
        state = self.grid[x][y]

        for x in range(0, self.cols):
            for y in range(0, self.rows):

                # count neighbours of current cell
                sum = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if x+i == -1 or y+j == -1 or x+i == self.cols or y+j == self.rows:
                            pass
                        else:
                            sum += self.grid[x+i][y+j]
                sum = sum - self.grid[x][y]

                # check game of life rules for current cell
                state = self.grid[x][y]
                if state == 0 and sum == 3:
                    next[x][y] = 1
                elif state == 1 and sum < 2:
                    next[x][y] = 0
                elif state == 1 and sum > 3:
                    next[x][y] = 0
                else:
                    next[x][y] = state
                    
        return next


if __name__ == "__main__":
    grid = Grid(5,5)
    grid.print_grid()
    grid.evolve()
    grid.print_grid()
    grid.evolve()
    grid.print_grid()
    grid.evolve()
    grid.print_grid()
