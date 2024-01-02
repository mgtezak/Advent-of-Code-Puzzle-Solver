from itertools import groupby

def part1(puzzle_input):
    for _ in range(40):
        puzzle_input = ''.join(str(len(list(g))) + str(n) for n, g in groupby(puzzle_input))
    return len(puzzle_input)