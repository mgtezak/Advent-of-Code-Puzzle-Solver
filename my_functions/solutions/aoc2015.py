import numpy as np
import hashlib
import re
from operator import and_, or_, not_, rshift, lshift
import ast
from itertools import permutations, groupby




def aoc2015_day1_part1(puzzle_input):
    return puzzle_input.count('(') - puzzle_input.count(')')


def aoc2015_day1_part2(puzzle_input):
    floor = 0
    for i, char in enumerate(puzzle_input):
        floor += 1 if char == '(' else -1
        if floor == -1:
            return i + 1
        

####################################################################################################


def aoc2015_day2_part1(puzzle_input):
    lines = [list(map(int, line.split('x'))) for line in puzzle_input.split('\n')]
    total_paper = 0
    for line in lines:
        sides = [line[0]*line[1], line[1]*line[2], line[0]*line[2]]
        total_paper += sum(sides) * 2 + min(sides)
    return total_paper


def aoc2015_day2_part2(puzzle_input):
    lines = [list(map(int, line.split('x'))) for line in puzzle_input.split('\n')]
    total_ribbon = 0
    for line in lines:
        edges = [line[0], line[1], line[2]]
        total_ribbon += np.prod(edges)
        edges.remove(max(edges))
        total_ribbon += sum(edges * 2)
    return total_ribbon


####################################################################################################


def aoc2015_day3_part1(puzzle_input):
    x = y = 0
    directions = {'v': (0, -1), '^': (0, 1), '<': (-1, 0), '>': (1, 0)}
    visited = {(x, y)}
    for move in puzzle_input:
        x += directions[move][0]
        y += directions[move][1]
        visited.add((x, y))
    return len(visited)


def aoc2015_day3_part2(puzzle_input):

    def get_coords(moves: str, x: int=0, y: int=0):
        directions = {'v': (0, -1), '^': (0, 1), '<': (-1, 0), '>': (1, 0)}
        visited = {(x, y)}
        for move in moves:
            x += directions[move][0]
            y += directions[move][1]
            visited.add((x, y))
        return visited

    santa_moves, robo_moves = puzzle_input[0::2], puzzle_input[1::2]
    santa_coords, robo_coords = get_coords(santa_moves), get_coords(robo_moves)
    return len(santa_coords | robo_coords)


####################################################################################################


def aoc2015_day4_part1(puzzle_input):
    num = 0
    while True:
        result = hashlib.md5((puzzle_input + str(num)).encode())
        if result.hexdigest()[:5] == '00000':
            return num
        num += 1


def aoc2015_day4_part2(puzzle_input):
    num = 0
    while True:
        result = hashlib.md5((puzzle_input + str(num)).encode())
        if result.hexdigest()[:6] == '000000':
            return num
        num += 1


####################################################################################################


def aoc2015_day5_part1(puzzle_input):

    def contains_three_vowels(s):
        count = sum([s.count(v) for v in 'aeiou'])
        if count >= 3:
            return True

    def contains_double(s):
        if any(s[i] == s[i+1] for i in range(len(s) - 1)):
            return True

    def contains_naughty(s):
        if any(x in s for x in ['ab', 'cd', 'pq', 'xy']):
            return True    

    def is_nice(s):
        return (
            contains_three_vowels(s) and
            contains_double(s) and
            not contains_naughty(s)
        )

    return sum(1 for s in puzzle_input.split() if is_nice(s))


def aoc2015_day5_part2(puzzle_input):
            
    def has_repeating_pair(s):
        if any(s[i:i+2] == s[j:j+2] for i in range(len(s)-3) for j in range(i+2, len(s)-1)):
            return True

    def repeats_after_gap(s):
        for i in range(len(s) - 2):
            if s[i] == s[i+2]:
                return True

    def is_nice(string):
        return has_repeating_pair(string) and repeats_after_gap(string)
        
    return sum(1 for s in puzzle_input.split() if is_nice(s))


####################################################################################################


def aoc2015_day6_part1(puzzle_input):
    regex = r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)"
    operations = re.findall(regex, puzzle_input)
    grid = np.zeros((1000, 1000))
    for op, *coords in operations:
        x0, y0, x1, y1 = map(int, coords)
        if op == 'turn on':
            grid[x0:x1+1, y0:y1+1] = 1
        elif op == 'turn off':
            grid[x0:x1+1, y0:y1+1] = 0
        else:
            grid[x0:x1+1, y0:y1+1] = 1 - grid[x0:x1+1, y0:y1+1]
    return int(grid.sum())


def aoc2015_day6_part2(puzzle_input):
    regex = r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)"
    operations = re.findall(regex, puzzle_input)
    grid = np.zeros((1000, 1000))
    for op, *coords in operations:
        x0, y0, x1, y1 = map(int, coords)
        if op == 'turn on':
            grid[x0:x1+1, y0:y1+1] += 1
        elif op == 'turn off':
            grid[x0:x1+1, y0:y1+1] = np.maximum(0, grid[x0:x1+1, y0:y1+1] - 1)
        else:
            grid[x0:x1+1, y0:y1+1] += 2
    return int(grid.sum())


####################################################################################################


def aoc2015_day7_part1(puzzle_input):

    operators = {
        'AND': and_,
        'OR': or_,
        'NOT': not_,
        'RSHIFT': rshift,
        'LSHIFT': lshift
    }
    
    def calculate(wire):
        if wire.isnumeric():
            return int(wire)
        if wire not in results:
            ops = instructions[wire]
            if len(ops) == 1:
                val = calculate(ops[0])
            else:
                gate = ops[-2]
                if gate == 'NOT':
                    val = ~calculate(ops[1])
                else:
                    val = operators[gate](calculate(ops[0]), calculate(ops[2]))
            results[wire] = val
        return results[wire]
    
    instructions = dict()
    results = dict()
    for line in puzzle_input.split('\n'):
        (ops, val) = line.split(' -> ')
        instructions[val] = ops.split()
        
    return calculate('a')


def aoc2015_day7_part2(puzzle_input):
    operators = {
        'AND': and_,
        'OR': or_,
        'NOT': not_,
        'RSHIFT': rshift,
        'LSHIFT': lshift
    }
    
    def calculate(wire):
        if wire.isnumeric():
            return int(wire)
        if wire not in results:
            ops = instructions[wire]
            if len(ops) == 1:
                val = calculate(ops[0])
            else:
                gate = ops[-2]
                if gate == 'NOT':
                    val = ~calculate(ops[1])
                else:
                    val = operators[gate](calculate(ops[0]), calculate(ops[2]))
            results[wire] = val
        return results[wire]
    
    instructions = dict()
    results = dict()
    for line in puzzle_input.split('\n'):
        (ops, val) = line.split(' -> ')
        instructions[val] = ops.split()

    a = calculate('a')
    results = {'b': a}
    return calculate('a')


####################################################################################################


def aoc2015_day8_part1(puzzle_input):
    str_chars = 0
    for line in puzzle_input.split():
        if line[0] != '"' or line[-1] != '"': # checking if there's no danger in using literal eval 
            return      
        str_chars += len(line) - len(ast.literal_eval(line))
    return str_chars


def aoc2015_day8_part2(puzzle_input):
    return sum(2 + line.count('\\') + line.count('"') for line in puzzle_input.split())


####################################################################################################


def aoc2015_day9_part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    locs = {line[0] for line in lines} | {lines[-1][2]}
    perms = list(permutations(locs))
    distances = {}
    for p in perms:
        total_distance = 0
        for i in range(7):
            start = p[i]
            stop = p[i+1]
            dist = [int(line[-1]) for line in lines if start in line and stop in line][0]
            total_distance += dist
        distances[p] = total_distance
    return min(distances.values())


def aoc2015_day9_part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    locs = {line[0] for line in lines} | {lines[-1][2]}
    perms = list(permutations(locs))
    distances = {}
    for p in perms:
        total_distance = 0
        for i in range(7):
            start = p[i]
            stop = p[i+1]
            dist = [int(line[-1]) for line in lines if start in line and stop in line][0]
            total_distance += dist
        distances[p] = total_distance
    return max(distances.values())


####################################################################################################


def aoc2015_day10_part1(puzzle_input):
    for _ in range(40):
        puzzle_input = ''.join(str(len(list(g))) + str(n) for n, g in groupby(puzzle_input))
    return len(puzzle_input)


def aoc2015_day10_part2(puzzle_input):
    for _ in range(50):
        puzzle_input = ''.join(str(len(list(g))) + str(n) for n, g in groupby(puzzle_input))
    return len(puzzle_input)


####################################################################################################


def aoc2015_day11_part1(puzzle_input):
    pass


def aoc2015_day11_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day12_part1(puzzle_input):
    pass


def aoc2015_day12_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day13_part1(puzzle_input):
    pass


def aoc2015_day13_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day14_part1(puzzle_input):
    pass


def aoc2015_day14_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day15_part1(puzzle_input):
    pass


def aoc2015_day15_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day16_part1(puzzle_input):
    pass


def aoc2015_day16_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day17_part1(puzzle_input):
    pass


def aoc2015_day17_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day18_part1(puzzle_input):
    pass


def aoc2015_day18_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day19_part1(puzzle_input):
    pass


def aoc2015_day19_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day20_part1(puzzle_input):
    pass


def aoc2015_day20_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day21_part1(puzzle_input):
    pass


def aoc2015_day21_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day22_part1(puzzle_input):
    pass


def aoc2015_day22_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day23_part1(puzzle_input):
    pass


def aoc2015_day23_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day24_part1(puzzle_input):
    pass


def aoc2015_day24_part2(puzzle_input):
    pass


####################################################################################################


def aoc2015_day25_part1(puzzle_input):
    pass


def aoc2015_day25_part2(puzzle_input):
    pass



