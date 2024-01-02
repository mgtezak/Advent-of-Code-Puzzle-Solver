def part1(puzzle_input):
    for i in range(4, len(puzzle_input) + 1):
        if len(set(puzzle_input[i-4:i])) == 4:
            return i


def aoc2022_day6_part2(puzzle_input):
    for i in range(14, len(puzzle_input) + 1):
        if len(set(puzzle_input[i-14:i])) == 14:
            return i