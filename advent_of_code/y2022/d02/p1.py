def part1(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    points = 0
    for line in lines:
        if line in ['A Y', 'B Z', 'C X']:
            points += 6
        elif line in ['A X', 'B Y', 'C Z']:
            points += 3 
        points += ['X', 'Y', 'Z'].index(line[-1]) + 1
    return points