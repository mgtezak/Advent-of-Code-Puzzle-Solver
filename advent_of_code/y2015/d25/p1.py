def part1(puzzle_input):

    instruction = puzzle_input.split()
    x, y = [int(instruction[i].strip(',.')) for i in (-1, -3)]
    row = col = i = 1
    while (row, col) != (x, y):
        if col > 1:
            row += 1
            col -= 1
        else:
            col = row + 1
            row = 1
        i += 1
    
    code = 20151125
    for _ in range(i-1):
        code = code * 252533 % 33554393

    return code