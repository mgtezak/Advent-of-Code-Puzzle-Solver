from itertools import groupby

def part2(puzzle_input):
    for _ in range(50):
        puzzle_input = ''.join(str(len(list(g))) + str(n) for n, g in groupby(puzzle_input))
    return len(puzzle_input)