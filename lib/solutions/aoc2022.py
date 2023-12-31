# Third party imports
import numpy as np

# Native imports
import string
import re
import math
from ast import literal_eval
from functools import cmp_to_key
from itertools import cycle
from operator import add, sub, mul, truediv



def aoc2022_day1_part1(puzzle_input):
    elves = []
    for elf in puzzle_input.split('\n\n'):
        elves.append(sum(map(int, elf.split('\n'))))
    return max(elves)


def aoc2022_day1_part2(puzzle_input):
    elves = []
    for elf in puzzle_input.split('\n\n'):
        elves.append(sum(map(int, elf.split('\n'))))
    return sum(sorted(elves)[-3:])    


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

    monkeys = [[line.split() for line in monkey.split('\n')] for monkey in puzzle_input.split('\n\n')]
    m_items = dict()                                   # will track which monkey has which item
    m_inspect = {m: 0 for m, _  in enumerate(monkeys)} # will count how often each monkey will inspect an item
    m_attrs = dict()                                   # tuple of operation and test each monkey performs
    lcm = 1                                            # least common multiple of each monkeys divisor (in this case simply product, since they're all primes)

    for m in monkeys:
        num = int(m[0][1].strip(':'))

        items = [int(i.strip(',')) for i in m[1][2:]]
        m_items[num] = items

        op = tuple(m[2][-2:])                                   # (operator, operand) e. g.: ('*', 17))
        test = tuple(map(int, [m[3][-1], m[4][-1], m[5][-1]]))  # (divisible by, if true, if false)
        lcm *= int(m[3][-1])
        m_attrs[num] = (op, test)

    for _ in range(20):

        for monkey in range(len(monkeys)):

            m_inspect[monkey] += len(m_items[monkey])
            for item in m_items[monkey]:

                op, test = m_attrs[monkey]

                if op[1] == 'old':
                    item **= 2
                elif op[0] == '*':
                    item *= int(op[1])
                else:
                    item += int(op[1])

                item //= 3

                item %= lcm   # x is divisble by y iff x % (multiple of y) is divisble by y
                               
                if item % test[0] == 0:
                    m_items[test[1]].append(item)
                else:
                    m_items[test[2]].append(item)

            m_items[monkey] = []

    a, b = sorted(m_inspect.values())[-2:]

    return a * b


def aoc2022_day11_part2(puzzle_input):

    monkeys = [[line.split() for line in monkey.split('\n')] for monkey in puzzle_input.split('\n\n')]
    m_items = dict()                                   # will track which monkey has which item
    m_inspect = {m: 0 for m, _  in enumerate(monkeys)} # will count how often each monkey will inspect an item
    m_attrs = dict()                                   # tuple of operation and test each monkey performs
    lcm = 1                                            # least common multiple of each monkeys divisor (in this case simply product, since they're all primes)

    for m in monkeys:
        num = int(m[0][1].strip(':'))

        items = [int(i.strip(',')) for i in m[1][2:]]
        m_items[num] = items

        op = tuple(m[2][-2:])                                   # (operator, operand) e. g.: ('*', 17))
        test = tuple(map(int, [m[3][-1], m[4][-1], m[5][-1]]))  # (divisible by, if true, if false)
        lcm *= int(m[3][-1])
        m_attrs[num] = (op, test)

    for _ in range(10_000):

        for monkey in range(len(monkeys)):

            m_inspect[monkey] += len(m_items[monkey])
            for item in m_items[monkey]:

                op, test = m_attrs[monkey]

                if op[1] == 'old':
                    item **= 2
                elif op[0] == '*':
                    item *= int(op[1])
                else:
                    item += int(op[1])

                item %= lcm   # x is divisble by y iff x % (multiple of y) is divisble by y
                               
                if item % test[0] == 0:
                    m_items[test[1]].append(item)
                else:
                    m_items[test[2]].append(item)

            m_items[monkey] = []

    a, b = sorted(m_inspect.values())[-2:]

    return a * b


####################################################################################################


def aoc2022_day12_part1(puzzle_input):

    lines = puzzle_input.split('\n')
    grid = [[] for _ in lines]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':                        # elevation at S = a
                x_start, y_start, char = x, y, 'a'
            elif char == 'E':                      # elevation at E = z 
                x_end, y_end, char = x, y, 'z'
            grid[y].append(ord(char) - 97)         # turn letters (a-z) into numbers (0-25)

    x_range, y_range = range(len(grid[0])), range(len(grid))

    def validate_move(x: int, y: int, elevation: int) -> bool:
        '''returns True if the coordinates are inside the grid and the climb is not too steep'''
        return (x in x_range) and (y in y_range) and (grid[y][x] < elevation + 2)
    
    steps = elevation = 0
    visited = {(x_start, y_start): (steps, elevation)}
    queue = [(x_start, y_start)]

    while queue:
        x, y = queue.pop(0)
        steps, elevation = visited[(x, y)]
        
        if x == x_end and y == y_end:
            break

        moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        possible_moves = [(x, y) for x, y in moves if validate_move(x, y, elevation)]

        for x, y in possible_moves:
            if (x, y) not in visited:
                visited[(x, y)] = (steps + 1, grid[y][x])
                queue.append((x, y))
        
    return steps


def aoc2022_day12_part2(puzzle_input):

    lines = puzzle_input.split('\n')
    grid = [[] for _ in lines]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':                        # elevation at S = a
                char = 'a'
            elif char == 'E':                      # elevation at E = z 
                x_end, y_end, char = x, y, 'z'
            grid[y].append(ord(char) - 97)         # turn letters (a-z) into numbers (0-25)

    x_range, y_range = range(len(grid[0])), range(len(grid))

    def validate_move(x: int, y: int, elevation: int) -> bool:
        '''returns True if the coordinates are inside the grid and the climb is not too steep'''
        return (x in x_range) and (y in y_range) and (grid[y][x] < elevation + 2)

    def get_shortest_distance(x_start, y_start) -> int:
        '''Breadth-first-search algorithm that finds the shortest path and returns number of steps if path exists'''
        
        steps = elevation = 0
        visited = {(x_start, y_start): (steps, elevation)}
        queue = [(x_start, y_start)]

        while queue:
            x, y = queue.pop(0)
            steps, elevation = visited[(x, y)]
            
            if x == x_end and y == y_end:
                break

            moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            possible_moves = [(x, y) for x, y in moves if validate_move(x, y, elevation)]

            for x, y in possible_moves:
                if (x, y) not in visited:
                    visited[(x, y)] = (steps + 1, grid[y][x])
                    queue.append((x, y))
            
        return float('inf')

    possible_starts = [(x, y) for y, row in enumerate(grid) for x, elevation in enumerate(row) if elevation == 0]
    return min(get_shortest_distance(*coords) for coords in possible_starts)


####################################################################################################


def aoc2022_day13_part1(puzzle_input):

    def compare_item(left, right):
        if type(left) == type(right):

            if type(left) == list: ### both are lists

                for i, l in enumerate(left):

                    if i == len(right): ### right ran out of indices
                        return -1

                    if compare_item(l, right[i]) == 1:
                        return 1

                    elif compare_item(l, right[i]) == -1:
                        return -1

                if len(right) > len(left): ### left ran out of indices
                    return 1
                
            elif left != right: ### both are numbers and not equal
                    return 1 if left < right else -1

        else: ### if one is int the other is list: put the int in a list and compare lists
            return compare_item([left], right) if type(left) == int else compare_item(left, [right])
    
    def safe_eval(line):
        assert set(line).issubset(set('0123456789[],')), "This line contains invalid characters"
        return literal_eval(line)
    
    total = 0
    for i, lines in enumerate(puzzle_input.split('\n\n'), start=1):
        lines = [safe_eval(line) for line in lines.split('\n')]
        if compare_item(*lines) == 1:
            total += i

    return total


def aoc2022_day13_part2(puzzle_input):

    def compare_item(left, right):
        if type(left) == type(right):

            if isinstance(left, list): ### both are lists

                for i, _ in enumerate(left):

                    if i == len(right): ### right ran out of indices
                        return -1

                    if compare_item(left[i], right[i]) == 1:
                        return 1

                    elif compare_item(left[i], right[i]) == -1:
                        return -1

                if len(right) > len(left): ### left ran out of indices
                    return 1
                
            elif left != right: ### both are numbers and not equal
                    return 1 if left < right else -1

        else: ### if one is int the other is list: put the int in a list and compare lists
            return compare_item([left], right) if type(left) == int else compare_item(left, [right])
    
    def safe_eval(line):
        assert set(line).issubset(set('0123456789[],')), "This line contains invalid characters"
        return literal_eval(line)

    packets = [[safe_eval(line) for line in s.split('\n')] for s in puzzle_input.split('\n\n')]
    all_packets = [l for packet in packets for l in packet] + [[[2]], [[6]]]
    sorted_packets = ['index 0'] + sorted(all_packets, key=cmp_to_key(compare_item), reverse=True)
    return sorted_packets.index([[2]]) * sorted_packets.index([[6]])


####################################################################################################


def aoc2022_day14_part1(puzzle_input):

    regex = re.compile('(\d+),(\d+)')
    coords = []
    for line in puzzle_input.split('\n'):
        coords.append([list(map(int, xy)) for xy in regex.findall(line)])

    # figuring out the dimensionality
    x_max = max(x for line in coords for x, _ in line)
    y_max = max(y for line in coords for _, y in line)
    grid = [['.' for _ in range(x_max+150)] for _ in range(y_max+2)]

    # adding rock
    for line in coords:
        for i, (x, y) in enumerate(line):
            grid[y][x] = '#'
            if i > 0:
                for x_ in range(*sorted([x, line[i-1][0]])):
                    grid[y][x_] = '#'
                for y_ in range(*sorted([y, line[i-1][1]])):
                    grid[y_][x] = '#'

    def add_sand():
        x, y = (500, 0)
        while y < len(grid) - 1:
            if grid[y+1][x] == '.':
                x, y = x, y+1
            elif grid[y+1][x-1] == '.':
                x, y = x-1, y+1
            elif grid[y+1][x+1] == '.':
                x, y = x+1, y+1
            else:
                break
        grid[y][x] = 'o'
        return x, y

    sand = 0
    while True:
        x, y = add_sand()
        if  y == len(grid) - 1:
            break
        sand += 1

    return sand


def aoc2022_day14_part2(puzzle_input):

    regex = re.compile('(\d+),(\d+)')
    coords = []
    for line in puzzle_input.split('\n'):
        coords.append([list(map(int, xy)) for xy in regex.findall(line)])

    # figuring out the dimensionality
    x_max = max(x for line in coords for x, _ in line)
    y_max = max(y for line in coords for _, y in line)
    grid = [['.' for _ in range(x_max+150)] for _ in range(y_max+2)]

    # adding rock
    for line in coords:
        for i, (x, y) in enumerate(line):
            grid[y][x] = '#'
            if i > 0:
                for x_ in range(*sorted([x, line[i-1][0]])):
                    grid[y][x_] = '#'
                for y_ in range(*sorted([y, line[i-1][1]])):
                    grid[y_][x] = '#'

    def add_sand():
        x, y = (500, 0)
        while y < len(grid) - 1:
            if grid[y+1][x] == '.':
                x, y = x, y+1
            elif grid[y+1][x-1] == '.':
                x, y = x-1, y+1
            elif grid[y+1][x+1] == '.':
                x, y = x+1, y+1
            else:
                break
        grid[y][x] = 'o'
        return x, y

    sand = 0
    while True:
        x, y = add_sand()
        if x == 500 and y == 0:
            break
        sand += 1

    return sand + 1


####################################################################################################


def aoc2022_day15_part1(puzzle_input):

    sensors = {}
    for line in puzzle_input.split('\n'):
        x1, y1, x2, y2 = map(int, [line.split()[i].strip('xy=,:') for i in (2,3,8,9)])
        sensors[(x1, y1)] = abs(x1 - x2) + abs(y1 - y2)

    coverage = set()
    for x, y in sensors:
        distance_to_row = abs(2_000_000 - y)
        leftover = sensors[(x, y)] - distance_to_row
        for i in range(-leftover, leftover):
            coverage.add(x + i)

    return len(coverage)


def aoc2022_day15_part2(puzzle_input):

    sensors = {}
    for line in puzzle_input.split('\n'):
        x1, y1, x2, y2 = map(int, [line.split()[i].strip('xy=,:') for i in (2,3,8,9)])
        sensors[(x1, y1)] = abs(x1 - x2) + abs(y1 - y2)

    def merge_left(ranges):
        if ranges[1][0] <= ranges[0][1] + 1:
            if ranges[1][1] > ranges[0][1]:
                ranges[0][1] = ranges[1][1]
            ranges.pop(1)
            return True
        return False
        
    def get_ranges(row):
        ranges = list()
        for s in sensors:
            x, y = s
            distance_to_row = abs(row - y)
            leftover = max([0, sensors[s] - distance_to_row])
            if leftover:
                low = max(x-leftover, 0) # inclusive boundary
                high = min(x+leftover, 4_000_000) # not inclusive boundary
                ranges.append([low, high])

        ranges.sort()
        while len(ranges) > 1:
            if not merge_left(ranges):
                break

        return ranges

    for y in range(4_000_000):
        r = get_ranges(y)
        if len(r) > 1:
            x = r[0][1] + 1
            break
    
    return x * 4_000_000 + y


####################################################################################################


def aoc2022_day16_part1(puzzle_input):

    def calc_distance(start: str, end: str, connections: dict) -> int:
        queue = [(start, 0)]
        visited = [start]
        while len(queue) > 0:
            node, steps = queue.pop(0)
            steps += 1
            for n in connections[node]:
                if n not in visited:
                    visited.append(n)
                    queue.append((n, steps))
                if n == end:
                    return steps

    def calc_release(start: str, end: str, t: int, max_t: int, distances: dict, release_rates: dict) -> int:
        payoff_time = max(max_t - t - distances[start][end], 0)
        total_release = payoff_time * release_rates[end]
        return total_release

    def dfs(unvisited: list, curr_v: str='AA', total: int=0, time: int=0, max_time: int=30) -> None:
        
        for next_v in unvisited:
            if (distances[curr_v][next_v] > max_time - time):
                continue

            unvisited_ = [u for u in unvisited if u != next_v]
            time_      = time + distances[curr_v][next_v]
            total_     = total + calc_release(curr_v, next_v, time, max_time, distances, release_rates)
            dfs(unvisited_, next_v, total_,time_, max_time)
        
        total_release.add(total)

    regex = r'Valve ([\w]+) has flow rate=([\d]+); tunnels? leads? to valves? (([\w]+,\s)*[\w]+)'
    connections = {}
    release_rates = {}
    for line in puzzle_input.split('\n'):
        valve, rate, connected, _ = re.findall(regex, line)[0]
        connections[valve] = connected.split(', ')
        if rate != '0': 
            release_rates[valve] = int(rate)
            
    distances = dict()
    for v in ['AA'] + list(release_rates):
        distances[v] = {r: 1 + calc_distance(v, r, connections) for r in release_rates if r != v}
    total_release = set()
    dfs(release_rates.keys())
    return max(total_release)


def aoc2022_day16_part2(puzzle_input):

    def calc_distance(start: str, end: str, connections: dict) -> int:
        queue = [(start, 0)]
        visited = [start]
        while len(queue) > 0:
            node, steps = queue.pop(0)
            steps += 1
            for n in connections[node]:
                if n not in visited:
                    visited.append(n)
                    queue.append((n, steps))
                if n == end:
                    return steps
                
    def calc_release(start: str, end: str, t: int, max_t: int, distances: dict, release_rates: dict) -> int:
        payoff_time = max(max_t - t - distances[start][end], 0)
        total_release = payoff_time * release_rates[end]
        return total_release

    def dfs(unvisited: list, current_v: str='AA', total: int=0, time: int=0, max_time: int=26, elephant: bool=True) -> None:
        
        if elephant and len(unvisited) == 8:
            dfs(unvisited=unvisited, current_v='AA', total=total, max_time=26, elephant=False)
            
        for next_v in unvisited:
            if (distances[current_v][next_v] > max_time - time):
                continue

            unvisited_ = [u for u in unvisited if u != next_v]
            time_      = time + distances[current_v][next_v]
            total_     = total + calc_release(current_v, next_v, time, max_time, distances, release_rates)
            dfs(unvisited_, next_v, total_,time_, max_time)
        
        total_release.add(total)

    regex = r'Valve ([\w]+) has flow rate=([\d]+); tunnels? leads? to valves? (([\w]+,\s)*[\w]+)'
    connections = {}
    release_rates = {}
    for line in puzzle_input.split('\n'):
        valve, rate, connected, _ = re.findall(regex, line)[0]
        connections[valve] = connected.split(', ')
        if rate != '0': 
            release_rates[valve] = int(rate)
            
    distances = dict()
    for v in ['AA'] + list(release_rates):
        distances[v] = {r: 1 + calc_distance(v, r, connections) for r in release_rates if r != v}
    total_release = set()
    dfs(release_rates.keys())
    return max(total_release)


####################################################################################################


def aoc2022_day17_part1(puzzle_input):

    def determine_height(grid):
        for i, line in enumerate(grid):
            if line == list(row):
                return  i - 1
            
    def get_coords(shape, height):
        shape = shape.split()[::-1]
        i, j = 3, height + 4
        return [(x+i, y+j) for y, row in enumerate(shape) for x, char in enumerate(row) if char == '#']

    def move_is_possible(coords, grid):
        return all(grid[y][x] == '.' for x, y in coords)

    def move_sideways(coords, grid):
        jet_idx = next(iter_jet_idx)
        i = 1 if puzzle_input[jet_idx]== '>' else -1
        new_coords = [(x+i, y) for x, y in coords]
        if move_is_possible(new_coords, grid):
            coords = new_coords
        return coords, jet_idx

    def move_down(coords, grid):
        new_coords = [(x, y-1) for x, y in coords]
        if move_is_possible(new_coords, grid):
            return new_coords, False
        return coords, True

    def drop_rock(coords, grid):
        while True:
            coords, jet_idx = move_sideways(coords, grid)
            coords, settled = move_down(coords, grid)
            if settled:
                break
        return coords, jet_idx

    def add_new_rock(grid, shape_index):
        shape = shapes[shape_index]
        height = determine_height(grid)
        coords = get_coords(shape, height)
        coords, jet_idx = drop_rock(coords, grid)
        for x, y in coords:
            grid[y][x] = '#'
        return grid, jet_idx

    iter_jet_idx = cycle(range(len(puzzle_input)))
    shapes = ['####', '.#.\n###\n.#.', '..#\n..#\n###', '#\n#\n#\n#', '##\n##']
    row = '|.......|'
    grid = [['-'] * 9] + [list(row) for _ in range(100_000)] 
    heights = {}
    state_hashes = []
    for rock in range(5000):
        shape_idx = rock % 5
        grid, jet_idx = add_new_rock(grid, shape_idx)
        height = determine_height(grid)
        heights[rock] = height
        hash_value = hash((shape_idx, jet_idx, str(grid[height-1])))
        if hash_value not in state_hashes:
            state_hashes.append(hash_value)
        else:
            cycle_start = state_hashes.index(hash_value)
            cycle_len = len(state_hashes) - cycle_start
            break

    num_cycles = (2022 - cycle_start) // cycle_len
    remainder = (2022 - cycle_start) % cycle_len - 1        ### why -1?
    cycle_height = heights[cycle_start + cycle_len] - heights[cycle_start]
    remainder_height = heights[cycle_start + remainder] - heights[cycle_start]
    return heights[cycle_start] + cycle_height * num_cycles + remainder_height


def aoc2022_day17_part2(puzzle_input):

    def determine_height(grid):
        for i, line in enumerate(grid):
            if line == list(row):
                return  i - 1
            
    def get_coords(shape, height):
        shape = shape.split()[::-1]
        i, j = 3, height + 4
        return [(x+i, y+j) for y, row in enumerate(shape) for x, char in enumerate(row) if char == '#']

    def move_is_possible(coords, grid):
        return all(grid[y][x] == '.' for x, y in coords)

    def move_sideways(coords, grid):
        jet_idx = next(iter_jet_idx)
        i = 1 if puzzle_input[jet_idx]== '>' else -1
        new_coords = [(x+i, y) for x, y in coords]
        if move_is_possible(new_coords, grid):
            coords = new_coords
        return coords, jet_idx

    def move_down(coords, grid):
        new_coords = [(x, y-1) for x, y in coords]
        if move_is_possible(new_coords, grid):
            return new_coords, False
        return coords, True

    def drop_rock(coords, grid):
        while True:
            coords, jet_idx = move_sideways(coords, grid)
            coords, settled = move_down(coords, grid)
            if settled:
                break
        return coords, jet_idx

    def add_new_rock(grid, shape_index):
        shape = shapes[shape_index]
        height = determine_height(grid)
        coords = get_coords(shape, height)
        coords, jet_idx = drop_rock(coords, grid)
        for x, y in coords:
            grid[y][x] = '#'
        return grid, jet_idx

    iter_jet_idx = cycle(range(len(puzzle_input)))
    shapes = ['####', '.#.\n###\n.#.', '..#\n..#\n###', '#\n#\n#\n#', '##\n##']
    row = '|.......|'
    grid = [['-'] * 9] + [list(row) for _ in range(100_000)] 
    heights = {}
    state_hashes = []
    for rock in range(5000):
        shape_idx = rock % 5
        grid, jet_idx = add_new_rock(grid, shape_idx)
        height = determine_height(grid)
        heights[rock] = height
        hash_value = hash((shape_idx, jet_idx, str(grid[height-1])))
        if hash_value not in state_hashes:
            state_hashes.append(hash_value)
        else:
            cycle_start = state_hashes.index(hash_value)
            cycle_len = len(state_hashes) - cycle_start
            break

    num_cycles = (1_000_000_000_000 - cycle_start) // cycle_len
    remainder = (1_000_000_000_000 - cycle_start) % cycle_len - 1        ### why -1?
    cycle_height = heights[cycle_start + cycle_len] - heights[cycle_start]
    remainder_height = heights[cycle_start + remainder] - heights[cycle_start]
    return heights[cycle_start] + cycle_height * num_cycles + remainder_height


####################################################################################################


def aoc2022_day18_part1(puzzle_input):

    lava_cubes = []
    regex = r'(\d+),(\d+),(\d+)'
    for xyz in re.findall(regex, puzzle_input):
        lava_cubes.append(tuple(map(int, xyz)))

    adjacent = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    return sum((x+a, y+b, z+c) not in lava_cubes for x, y, z in lava_cubes for a, b, c in adjacent)


def aoc2022_day18_part2(puzzle_input):

    lava_cubes = []
    regex = r'(\d+),(\d+),(\d+)'
    for xyz in re.findall(regex, puzzle_input):
        lava_cubes.append(tuple(map(int, xyz)))

    adjacent = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    # # I used this to figure out dimensions for x, y, z:
    # for i in range(3):
    #     print(min(lava_cubes, key=lambda x: x[i])[i], max(lava_cubes, key=lambda x: x[i])[i])

    # # expand dimensions by one on each side:
    dim = range(-1, 21)

    n_visible_sides = 0
    queue = [(0, 0, 0)]
    visited = set()

    while queue:
        x, y, z = queue.pop()
        visited.add((x, y, z))
        for a, b, c in adjacent:
            q, r, s = x+a, y+b, z+c
            if q in dim and r in dim and s in dim and not((q, r, s) in visited or (q, r, s) in queue):
                if (q, r, s) in lava_cubes:
                    n_visible_sides += 1
                else:
                    queue.append((q, r, s))

    return n_visible_sides


####################################################################################################


def aoc2022_day19_part1(puzzle_input):
    '''Runtime is around 80 seconds. Not the fastest solution but it works. Not sure how to speed it up further.'''

    regex = re.compile('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')
    blueprints = dict()
    for line in puzzle_input.split('\n'):
        bpt, a, b, c, d, e, f = list(map(int, *regex.findall(line)))
        costs = np.array([[a, 0, 0, 0],[b, 0, 0, 0],[c, d, 0, 0], [e, 0, f, 0]])
        max_demand = np.array([max(a, b, c, e), d, f, math.inf])
        blueprints[bpt] = (costs, max_demand)

    def get_max_geodes(bpt, t_max=24):

        def dfs(robots=np.array([1,0,0,0]), resources=np.array([0,0,0,0]), t=0) -> None:
            '''
            Depth-First-Search algorithm, which increments not by minutes but instead 
            by time until the completion of the next robot.
            
            It filters the available production options by:
            (1) Max production demand for given resource. Any production which exceeds the max 
                possible expenditure per minute of that resource is useless.
            (2) Number of resources gathered. If I own more than I can spend (<16 was enough for 
                my puzzle input) then additional production (apart from geodes) is useless.
            (3) Whether the resources for a given bot are even being produced at all.
            (4) Whether time needed to save up for and build robot exceeds time left.

            Once no more useful options are available it fasts-forward to t_max adding up the 
            ongoing geode production.
            '''

            t_left = t_max - t
            options = [i for i in range(4) if (robots[i] < max_demand[i]) and (i == 3 or resources[i] < 16) and all((robots[j] > 0) or not costs[i,j] for j in range(4))]
            t_deltas = [1 + max(max(0, math.ceil((cost - resources[res]) / robots[res])) for res, cost in enumerate(costs[j]) if cost) for j in options]
            
            for robot, t_delta in zip(options, t_deltas):
                if t_delta >= t_left:
                    continue

                new_t = t + t_delta
                new_resources = resources + t_delta * robots - costs[robot]
                new_robots = robots.copy()
                new_robots[robot] += 1
                dfs(new_robots, new_resources, new_t)

            geodes = resources[3] + robots[3] * t_left
            results.append(geodes)
        

        costs, max_demand = blueprints[bpt]
        results = []
        dfs()
        return max(results)

    return sum(get_max_geodes(bpt) * bpt for bpt in blueprints)


def aoc2022_day19_part2(puzzle_input):
    '''Runtime is around 80 seconds. Not the fastest solution but it works. Not sure how to speed it up further.'''

    regex = re.compile('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')
    blueprints = dict()
    for line in puzzle_input.split('\n'):
        bpt, a, b, c, d, e, f = list(map(int, *regex.findall(line)))
        costs = np.array([[a, 0, 0, 0],[b, 0, 0, 0],[c, d, 0, 0], [e, 0, f, 0]])
        max_demand = np.array([max(a, b, c, e), d, f, math.inf])
        blueprints[bpt] = (costs, max_demand)

    def get_max_geodes(bpt, t_max=24):

        def dfs(robots=np.array([1,0,0,0]), resources=np.array([0,0,0,0]), t=0) -> None:
            '''
            Depth-First-Search algorithm, which increments not by minutes but instead 
            by time until the completion of the next robot.
            
            It filters the available production options by:
            (1) Max production demand for given resource. Any production which exceeds the max 
                possible expenditure per minute of that resource is useless.
            (2) Number of resources gathered. If I own more than I can spend (<16 was enough for 
                my puzzle input) then additional production (apart from geodes) is useless.
            (3) Whether the resources for a given bot are even being produced at all.
            (4) Whether time needed to save up for and build robot exceeds time left.

            Once no more useful options are available it fasts-forward to t_max adding up the 
            ongoing geode production.
            '''

            t_left = t_max - t
            options = [i for i in range(4) if (robots[i] < max_demand[i]) and (i == 3 or resources[i] < 16) and all((robots[j] > 0) or not costs[i,j] for j in range(4))]
            t_deltas = [1 + max(max(0, math.ceil((cost - resources[res]) / robots[res])) for res, cost in enumerate(costs[j]) if cost) for j in options]
            
            for robot, t_delta in zip(options, t_deltas):
                if t_delta >= t_left:
                    continue

                new_t = t + t_delta
                new_resources = resources + t_delta * robots - costs[robot]
                new_robots = robots.copy()
                new_robots[robot] += 1
                dfs(new_robots, new_resources, new_t)

            geodes = resources[3] + robots[3] * t_left
            results.append(geodes)
        

        costs, max_demand = blueprints[bpt]
        results = []
        dfs()
        return max(results)

    return math.prod([get_max_geodes(i, t_max=32) for i in range(1, 4)])


####################################################################################################


def aoc2022_day20_part1(puzzle_input):

    indexed_nums = [(i, n) for i, n in enumerate(map(int, puzzle_input.split('\n')))]
    mixed = indexed_nums.copy()
    l = len(mixed) - 1

    for i, n in indexed_nums:
        idx = mixed.index((i, n))
        new_idx = (idx + n) % l
        mixed.remove((i, n))
        mixed.insert(new_idx, (i, n))

    zero_idx = [i for i, tup in enumerate(mixed) if not tup[1]].pop()
    return sum(mixed[(zero_idx + i) % (l+1)][1] for i in (1000, 2000, 3000))


def aoc2022_day20_part2(puzzle_input):

    dec_key = 811589153
    indexed_nums = [(i, n * dec_key) for i, n in enumerate(map(int, puzzle_input.split('\n')))]
    mixed = indexed_nums.copy()
    l = len(mixed) - 1

    for _ in range(10):   # only once in part 1
        for i, n in indexed_nums:
            idx = mixed.index((i, n))
            new_idx = (idx + n) % l
            mixed.remove((i, n))
            mixed.insert(new_idx, (i, n))

    zero_idx = [i for i, tup in enumerate(mixed) if not tup[1]].pop()
    return sum(mixed[(zero_idx + i) % (l+1)][1] for i in (1000, 2000, 3000))


####################################################################################################


def aoc2022_day21_part1(puzzle_input):

    make_operation = {'+': add, '-': sub, '*': mul, '/': truediv}
    lines = [line.split(': ') for line in puzzle_input.split('\n')]
    monkeys = {monkey: output for monkey, output in lines}

    def get_num(m1):

        output = monkeys[m1]
        if output.isnumeric():
            return int(output)

        m2, op, m3 = output.split()
        m2 = get_num(m2)
        m3 = get_num(m3)
        return int(make_operation[op](m2, m3))

    return get_num('root')


def aoc2022_day21_part2(puzzle_input):

    def get_nums(monkeys):
        for monkey in monkeys:
            if type(monkey) == int or monkey.isnumeric():
                monkey =  int(monkey)
            elif monkey in solved:
                monkey = solved[monkey]
            yield monkey

    make_operation         = {'+': add, '-': sub, '*': mul, '/': truediv}
    make_reverse_operation = {'+': sub, '-': add, '*': truediv, '/': mul}
    lines = [line.split(': ') for line in puzzle_input.split('\n')]
    monkeys = {monkey: output for monkey, output in lines}
    solved = {monkey: int(num) for monkey, num in monkeys.items() if num.isnumeric() and monkey != 'humn'}
    unsolved = {monkey: operation.split() for monkey, operation in monkeys.items() if not operation.isnumeric()}

    while unsolved:

        for m1, (m2, op, m3) in unsolved.items():
            m1, m2, m3 = get_nums((m1, m2, m3))

            if type(m1) == int and type(m2) == int:
                if op in ('+', '*'):
                    solved[m3] = int(make_reverse_operation[op](m1, m2))
                else:
                    solved[m3] = int(make_operation[op](m2, m1))
            
            elif type(m1) == int and type(m3) == int:
                solved[m2] = int(make_reverse_operation[op](m1, m3))

            elif type(m2) == int and type(m3) == int:
                solved[m1] = int(make_operation[op](m2, m3))

            elif m1 == 'root':
                for i, m in enumerate((m2, m3)):
                    if type(m) == int:
                        solved[(m2, m3)[1-i]] = m
                        solved['root'] = 0
                
        newly_solwed = [m1 for m1, (m2, _, m3) in unsolved.items() if all(m in solved for m in (m1, m2, m3))]
        for monkey in newly_solwed:
            del unsolved[monkey]
        
    return solved['humn']


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

