import string

def part2(puzzle_input):
    lines = [line for line in puzzle_input.split()]
    letters = ' ' + string.ascii_letters
    result = 0
    for i in range(0, len(lines), 3):
        for l in lines[i]:
            if l in lines[i+1] and l in lines[i+2]:
                result += letters.index(l)
                break
    return result