def aoc2022_day1_part1(puzzle_input):
    return sorted([sum(map(int, elf.split('\n'))) for elf in puzzle_input.split('\n\n')], reverse=True)[0]


def aoc2022_day1_part2(puzzle_input):
    return sum(sorted([sum(map(int, elf.split('\n'))) for elf in puzzle_input.split('\n\n')], reverse=True)[:3])


####################################################################################################


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


####################################################################################################


def aoc2022_day3_part1(puzzle_input):
    pass


def aoc2022_day3_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day4_part1(puzzle_input):
    pass


def aoc2022_day4_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day5_part1(puzzle_input):
    pass


def aoc2022_day5_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day6_part1(puzzle_input):
    pass


def aoc2022_day6_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day7_part1(puzzle_input):
    pass


def aoc2022_day7_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day8_part1(puzzle_input):
    pass


def aoc2022_day8_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day9_part1(puzzle_input):
    pass


def aoc2022_day9_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day10_part1(puzzle_input):
    pass


def aoc2022_day10_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day11_part1(puzzle_input):
    pass


def aoc2022_day11_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day12_part1(puzzle_input):
    pass


def aoc2022_day12_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day13_part1(puzzle_input):
    pass


def aoc2022_day13_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day14_part1(puzzle_input):
    pass


def aoc2022_day14_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day15_part1(puzzle_input):
    pass


def aoc2022_day15_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day16_part1(puzzle_input):
    pass


def aoc2022_day16_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day17_part1(puzzle_input):
    pass


def aoc2022_day17_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day18_part1(puzzle_input):
    pass


def aoc2022_day18_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day19_part1(puzzle_input):
    pass


def aoc2022_day19_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day20_part1(puzzle_input):
    pass


def aoc2022_day20_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day21_part1(puzzle_input):
    pass


def aoc2022_day21_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day22_part1(puzzle_input):
    pass


def aoc2022_day22_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day23_part1(puzzle_input):
    pass


def aoc2022_day23_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day24_part1(puzzle_input):
    pass


def aoc2022_day24_part2(puzzle_input):
    pass


####################################################################################################


def aoc2022_day25_part1(puzzle_input):
    pass


def aoc2022_day25_part2(puzzle_input):
    pass

