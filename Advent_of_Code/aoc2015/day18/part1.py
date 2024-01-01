def part1(puzzle_input):
    '''Need to redo this with numpy!'''

    def get_neighbors(x, y):
        return [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2) if x+i in range(len(grid)) and y+j in range(len(grid)) and (i, j) != (0,0)]

    def get_num_lit_neighbors(x, y, grid):
        return sum([grid[j][i] == 1 for i, j in get_neighbors(x, y)])

    def switch(grid):
        new_grid = [[0] * 100 for _ in range(100)]
        for y in range(len(grid)):
            for x in range(len(grid)):
                if (get_num_lit_neighbors(x, y, grid) == 3) or (grid[y][x] == 1 and get_num_lit_neighbors(x, y, grid) == 2):
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
        return new_grid

    grid = [[0] * 100 for _ in range(100)]
    for y, line in enumerate(puzzle_input.split('\n')):
        for x, val in enumerate(line):
            if val == '#':
                grid[y][x] = 1

    for _ in range(100):
        grid = switch(grid)

    return sum(sum(row) for row in grid)