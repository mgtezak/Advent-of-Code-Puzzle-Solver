import string

def part1(puzzle_input):
    lines = [line for line in puzzle_input.split()]
    letters = ' ' + string.ascii_letters
    result = 0
    for line in lines:
        half = int(len(line)/2)
        first = line[:half]
        second = line[half:]
        for l in first:
            if l in second:
                result += letters.index(l)
                break
    return result