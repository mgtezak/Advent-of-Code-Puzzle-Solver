def part1(puzzle_input):
    lines = [list(map(int, line.split('x'))) for line in puzzle_input.split('\n')]
    total_paper = 0
    for line in lines:
        sides = [line[0]*line[1], line[1]*line[2], line[0]*line[2]]
        total_paper += sum(sides) * 2 + min(sides)
    return total_paper