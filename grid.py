def create_grid(rows=5,columns=10):
    '''returns nesetd array with first dimension
    number of rows, and second dimension number of
    columns   '''
    grid = []
    for row in range(rows):
        grid.append([])
        for column in range(columns):
            grid[row].append(0)
    return grid

grid = create_grid()
for i in grid:
    print(i)
