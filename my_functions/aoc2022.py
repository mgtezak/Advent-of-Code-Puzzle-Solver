def aoc2022_day1_part1(puzzle_input):
    return sorted([sum(map(int, elf.split('\n'))) for elf in puzzle_input.split('\n\n')], reverse=True)[0]

def aoc2022_day1_part2(puzzle_input):
    return sum(sorted([sum(map(int, elf.split('\n'))) for elf in puzzle_input.split('\n\n')], reverse=True)[:3])

def aoc2022_day2_part1(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    points = 0
    for line in lines:
        if line in ['A Y', 'B Z', 'C X']:
            points += 6
        elif line in ['A X', 'B Y', 'C Z']:
            points += 3 
        points += ['X', 'Y', 'Z'].index(line[-1]) + 1
    return points

def aoc2022_day2_part2(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    wins_against = {'s': 'r', 'r': 'p', 'p': 's'}
    loses_against = {val: key for key, val in wins_against.items()}
    points = 0
    for line in lines:
        elf = ['r', 'p', 's'][['A', 'B', 'C'].index(line[0])]
        if line[-1] == 'Y':
            me = elf
            points += 3
        elif line[-1] == 'Z':
            me = wins_against[elf]
            points += 6
        else:
            me = loses_against[elf]
        points += ['r', 'p', 's'].index(me) + 1
    return points