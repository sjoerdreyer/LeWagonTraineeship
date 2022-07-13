# pylint: disable=missing-docstring


def sudoku_validator(grid):
    '''
    returns True if a sudoku grid is valid, and false otherwise
    '''
    row = True
    column = True
    box_9 = True

    inverted_grid = [list(x) for x in zip(grid[0], grid[1], grid[2],
                                          grid[3], grid[4], grid[5],
                                          grid[6], grid[7], grid[8])]
    t_by_t = []

    for cel_row in range(0, 9, 3):
        for cel_col in range(0, 9, 3):
            grid_three = grid[cel_row][cel_col: cel_col+3]
            grid_three.extend(grid[cel_row+1] [cel_col: cel_col+3])
            grid_three.extend(grid[cel_row+2] [cel_col: cel_col+3])
            t_by_t.append(grid_three)

    for row_ in range(9):
        if len(set(grid[row_])) != 9:
            row = False

    for col in range(9):
        if len(set(inverted_grid[col])) != 9:
            column = False

    for grid_ in range(9):
        if len(set(t_by_t[grid_])) != 9:
            box_9 = False

    if row is True and column is True and box_9 is True:
        return True
    return False
