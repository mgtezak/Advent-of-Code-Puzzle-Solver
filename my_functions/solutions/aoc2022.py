import string
import re
import numpy as np



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


def aoc2022_day3_part2(puzzle_input):
    lines = [line for line in puzzle_input.split()]
    letters = ' ' + string.ascii_letters
    result = 0
    for i in range(0, len(lines), 3):
        for l in lines[i]:
            if l in lines[i+1] and l in lines[i+2]:
                result += letters.index(l)
                break
    return result


####################################################################################################


def aoc2022_day4_part1(puzzle_input):
    lines = [list(map(int, re.split('[,-]', line))) for line in puzzle_input.split('\n')]
    return sum(a <= c <= d <= b or c <= a <= b <= d for a, b, c, d in lines)


def aoc2022_day4_part2(puzzle_input):
    lines = [list(map(int, re.split('[,-]', line))) for line in puzzle_input.split('\n')]
    return sum(a <= d and c <= b for a, b, c, d in lines)


####################################################################################################


def aoc2022_day5_part1(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    pos = [[] for _ in range(9)]
    start = lines[:9]
    for j in range(8, -1, -1):
        for i in range(1, len(start[j]), 4):
            if start[j][i].isupper():
                pos[int(i/4)].append(start[j][i])   

    instructions = [list(map(int, line.split()[1:6:2])) for line in lines[10:]]
    for q, f, t in instructions:                      # q: quantity, f: from, t: to
        crates = pos[f-1][-q:]                        # identify q crates at f
        pos[f-1] = pos[f-1][:-q]                      # remove them at f
        pos[t-1] += crates[::-1]                      # add them at t
    return ''.join(crate[-1] for crate in pos)        # return upper crate of each position


def aoc2022_day5_part2(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    pos = [[] for _ in range(9)]
    start = lines[:9]
    for j in range(8, -1, -1):
        for i in range(1, len(start[j]), 4):
            if start[j][i].isupper():
                pos[int(i/4)].append(start[j][i])   

    instructions = [list(map(int, line.split()[1:6:2])) for line in lines[10:]]
    for q, f, t in instructions:                      # q: quantity, f: from, t: to
        crates = pos[f-1][-q:]                        # identify q crates at f
        pos[f-1] = pos[f-1][:-q]                      # remove them at f
        pos[t-1] += crates                            # add them at t
    return ''.join(crate[-1] for crate in pos)        # return upper crate of each position


####################################################################################################


def aoc2022_day6_part1(puzzle_input):
    for i in range(4, len(puzzle_input) + 1):
        if len(set(puzzle_input[i-4:i])) == 4:
            return i


def aoc2022_day6_part2(puzzle_input):
    for i in range(14, len(puzzle_input) + 1):
        if len(set(puzzle_input[i-14:i])) == 14:
            return i


####################################################################################################


def aoc2022_day7_part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    dir_size = {'root': 0}
    for line in lines:
        if line[:2] == ['$', 'cd']:
            if line[2] == '/': 
                path = ['root']
            elif line[2] == '..': 
                path.pop()
            else:
                path.append(path[-1] + '/' + line[2])
                dir_size[path[-1]] = 0
        elif line[0].isnumeric():
            for p in path: 
                dir_size[p] += int(line[0]) 

    return sum([val for val in dir_size.values() if val <= 100_000])


def aoc2022_day7_part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    dir_size = {'root': 0}
    for line in lines:
        if line[:2] == ['$', 'cd']:
            if line[2] == '/': 
                path = ['root']
            elif line[2] == '..': 
                path.pop()
            else:
                path.append(path[-1] + '/' + line[2])
                dir_size[path[-1]] = 0
        elif line[0].isnumeric():
            for p in path: 
                dir_size[p] += int(line[0]) 

    return sorted([v for v in dir_size.values() if v >= dir_size['root'] - 40_000_000])[0]


####################################################################################################


def aoc2022_day8_part1(puzzle_input):
    grid = [[int(n) for n in line] for line in puzzle_input.split('\n')]
    visible = set()
    for row in range(len(grid)):
        tallest = -1
        for col in range(len(grid[0])):
            if grid[row][col] > tallest:
                visible.add((row, col))
                tallest = grid[row][col]
                
        tallest = -1
        for col in range(len(grid[0])-1, -1, -1):
            if grid[row][col] > tallest:
                visible.add((row, col))
                tallest = grid[row][col]
                
    for col in range(len(grid[0])):
        tallest = -1
        for row in range(len(grid)):
            if grid[row][col] > tallest:
                visible.add((row, col))
                tallest = grid[row][col]
                
        tallest = -1
        for row in range(len(grid)-1, -1, -1):
            if grid[row][col] > tallest:
                visible.add((row, col))
                tallest = grid[row][col]

    return len(visible)


def aoc2022_day8_part2(puzzle_input):
    grid = [[int(n) for n in line] for line in puzzle_input.split('\n')]
    scenic_score = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):

            down = up = right = left = 0
            treehouse = grid[y][x]
            
            # look right
            for col in range(x+1, len(grid[0])):
                right += 1
                if grid[y][col] >= treehouse:
                    break

            # look left
            for col in range(x-1, -1, -1):
                left += 1
                if grid[y][col] >= treehouse:
                    break

            # look down
            for row in range(y+1, len(grid)):
                down += 1
                if grid[row][x] >= treehouse:
                    break

            # look up
            for row in range(y-1, -1, -1):
                up += 1
                if grid[row][x] >= treehouse:
                    break
                        
            scenic_score[(x, y)] = down * up * right * left

    return max(scenic_score.values())


####################################################################################################


def aoc2022_day9_part1(puzzle_input):
    x = [0] * 2
    y = [0] * 2
    visited = {(0, 0)}
    moves = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    for line in puzzle_input.split('\n'):
        direction, steps = line.split()
        for _ in range(int(steps)):              
            x[0] += moves[direction][0]
            y[0] += moves[direction][1]
            if abs(x[0] - x[0+1]) > 1 or abs(y[0] - y[1]) > 1:
                x[1] += np.sign(x[0] - x[1])
                y[1] += np.sign(y[0] - y[1])
            visited.add((x[1], y[1])) 
    return len(visited)


def aoc2022_day9_part2(puzzle_input):
    x = [0] * 10
    y = [0] * 10
    visited = {(0, 0)}
    moves = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    for line in puzzle_input.split('\n'):
        direction, steps = line.split()
        for _ in range(int(steps)):              
            x[0] += moves[direction][0]
            y[0] += moves[direction][1]
            for i in range(9):             # move middle and tail
                if abs(x[i] - x[i+1]) > 1 or abs(y[i] - y[i+1]) > 1:
                    x[i+1] += np.sign(x[i] - x[i+1])
                    y[i+1] += np.sign(y[i] - y[i+1])
            visited.add((x[9], y[9]))  # track tail
    return len(visited)


####################################################################################################


def aoc2022_day10_part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    cycle = row = signal_sum = 0
    x = 1
    image = ['' for _ in range(6)]
    for line in lines:
        for _ in range(len(line)):
            cycle += 1
            if cycle == 41:
                cycle -= 40
                row += 1
            if cycle == 20:
                signal_sum += x * (cycle + 40 * row)
            image[row] += '#' if x in range(cycle-2, cycle+1) else ' '
        if line[0] == 'addx':
            x += int(line[1])
    image = '\n' + '\n'.join(image)
    return signal_sum


def aoc2022_day10_part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    cycle = row = signal_sum = 0
    x = 1
    image = ['' for _ in range(6)]
    for line in lines:
        for _ in range(len(line)):
            cycle += 1
            if cycle == 41:
                cycle -= 40
                row += 1
            if cycle == 20:
                signal_sum += x * (cycle + 40 * row)
            image[row] += '#' if x in range(cycle-2, cycle+1) else ' '
        if line[0] == 'addx':
            x += int(line[1])
    return '\n'.join(image)


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

