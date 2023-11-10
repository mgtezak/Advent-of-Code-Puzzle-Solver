# Third party imports
import numpy as np
import sympy

# Native imports
import hashlib
import re
from operator import and_, or_, not_, rshift, lshift
import ast
from itertools import permutations, groupby, combinations
import string
import json
import random
from dataclasses import dataclass



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

    def is_valid(pw):
        '''check whether pw has two non-overlapping repeated letters and an alphabetical straight'''
        if len(re.findall(r'([a-z])\1', pw)) >= 2 and any(pw[i:i+3] in alphabet for i in range(6)):
            return True
        
    def increment(pw):
        '''alphabetically increments pw from right to left'''
        pw = list(pw)
        for i in range(7, -1, -1):
            next_index = (altered_alphabet.index(pw[i]) + 1) % 23
            pw[i] = altered_alphabet[next_index]
            if pw[i] == 'a':
                break
        return ''.join(pw)

    alphabet = string.ascii_lowercase
    altered_alphabet = re.sub('[iol]', '', alphabet) # removing forbidden letters
    
    pw = puzzle_input
    while not is_valid(pw):
        pw = increment(pw)

    return pw


def aoc2015_day11_part2(puzzle_input):

    def is_valid(pw):
        '''check whether pw has two non-overlapping repeated letters and an alphabetical straight'''
        if len(re.findall(r'([a-z])\1', pw)) >= 2 and any(pw[i:i+3] in alphabet for i in range(6)):
            return True
        
    def increment(pw):
        '''alphabetically increments pw from right to left'''
        pw = list(pw)
        for i in range(7, -1, -1):
            next_index = (altered_alphabet.index(pw[i]) + 1) % 23
            pw[i] = altered_alphabet[next_index]
            if pw[i] == 'a':
                break
        return ''.join(pw)

    alphabet = string.ascii_lowercase
    altered_alphabet = re.sub('[iol]', '', alphabet) # removing forbidden letters

    pw = puzzle_input
    for _ in range(2):
        while not is_valid(pw):
            pw = increment(pw)
        pw = increment(pw)

    return pw


####################################################################################################


def aoc2015_day12_part1(puzzle_input):

    def sum_of_item(item):

        if type(item) == list:
            return sum([sum_of_item(i) for i in item])

        if type(item) == dict:
            return sum([sum_of_item(i) for i in item.values()])

        if type(item) == str:
            return 0

        if type(item) == int:
            return item
        
    doc = json.loads(puzzle_input)
    return sum_of_item(doc)


def aoc2015_day12_part2(puzzle_input):

    def sum_of_item(item):

        if type(item) == list:
            return sum([sum_of_item(i) for i in item])

        if type(item) == dict:
            if 'red' in item.values():
                return 0
            return sum([sum_of_item(i) for i in item.values()])

        if type(item) == str:
            return 0

        if type(item) == int:
            return item
        
    doc = json.loads(puzzle_input)
    return sum_of_item(doc)


####################################################################################################


def aoc2015_day13_part1(puzzle_input):

    lines = [line.strip('.').split() for line in puzzle_input.split('\n')]

    preferences = []
    for line in lines:
        sub, obj = line[0], line[-1]
        pref =  int(line[3]) * (1 if line[2] == 'gain' else -1)
        preferences.append((sub, obj, pref))

    guests = set(line[0] for line in lines)
    compare_happiness = []
    for perm in permutations(guests):
        happiness = 0
        for i, guest in enumerate(perm):
            neighbor = perm[i-1]
            happiness += sum([pref[2] for pref in preferences if (guest in pref and neighbor in pref)])
        compare_happiness.append(happiness)

    return max(compare_happiness)


def aoc2015_day13_part2(puzzle_input):

    lines = [line.strip('.').split() for line in puzzle_input.split('\n')]
    guests = set(line[0] for line in lines)
    guests.add('I')
    lines.extend([f'I would gain 0 happiness units by sitting next to {guest}'.split() for guest in guests])
    lines.extend([f'{guest} would gain 0 happiness units by sitting next to I'.split() for guest in guests])

    preferences = []
    for line in lines:
        sub, obj = line[0], line[-1]
        pref =  int(line[3]) * (1 if line[2] == 'gain' else -1)
        preferences.append((sub, obj, pref))

    compare_happiness = []
    for perm in permutations(guests):
        happiness = 0
        for i, guest in enumerate(perm):
            neighbor = perm[i-1]
            happiness += sum([pref[2] for pref in preferences if (guest in pref and neighbor in pref)])
        compare_happiness.append(happiness)

    return max(compare_happiness)
    

####################################################################################################


def aoc2015_day14_part1(puzzle_input):

    def get_distance(r):
        name, speed, fly_secs, rest_secs = r[0], int(r[3]), int(r[6]), int(r[-2])
        full_fly_cycles = (2503 // (fly_secs + rest_secs)) * fly_secs
        partial_fly_cycle = min(fly_secs, 2503 % (fly_secs + rest_secs))
        full_distance = (full_fly_cycles + partial_fly_cycle) * speed
        return (full_distance, name)

    reindeers = [line.split() for line in puzzle_input.split('.\n')]
    winners = sorted([get_distance(r) for r in reindeers])
    winners = [r for r in winners if r[0] == winners[-1][0]] ### select multiple if multiple in first place
    return winners[0][0]


def aoc2015_day14_part2(puzzle_input):
    
    def get_distance(r, total_secs):
        name, speed, fly_secs, rest_secs = r[0], int(r[3]), int(r[6]), int(r[-2])
        full_fly_cycles = (total_secs // (fly_secs + rest_secs)) * fly_secs
        partial_fly_cycle = min(fly_secs, total_secs % (fly_secs + rest_secs))
        full_distance = (full_fly_cycles + partial_fly_cycle) * speed
        return (full_distance, name)

    def get_winnner_by_distance(total_secs):
        winners = sorted([get_distance(r, total_secs) for r in reindeers])
        winners = [r for r in winners if r[0] == winners[-1][0]] ### select multiple if multiple in first place
        return winners

    reindeers = [line.split() for line in puzzle_input.split('.\n')]
    points = {r[0]: 0 for r in reindeers}        
    for accumulated_secs in range(1, 2504):
        winners = get_winnner_by_distance(accumulated_secs)
        for r in winners:
            points[r[1]] += 1

    return max(points.values())


####################################################################################################


def aoc2015_day15_part1(puzzle_input):

    def get_score(recipe: list) -> int:
        '''calculate total score of cookie'''
        capacity = sum([recipe[i] * lines[i][0] for i in range(len(lines))])
        durability = sum([recipe[i] * lines[i][1] for i in range(len(lines))])
        flavor = sum([recipe[i] * lines[i][2] for i in range(len(lines))])
        texture = sum([recipe[i] * lines[i][3] for i in range(len(lines))])
        score = capacity * durability * flavor * texture
        return score

    def make_child_recipe(recipe: list) -> list:
        '''alter recipe by randomly adding and removing 10 teaspoons of ingredients'''
        child = recipe.copy()
        for _ in range(10):
            child[random.randint(0, 3)] += 1
        for _ in range(10):
            child[random.randint(0, 3)] -= 1
        return child

    def improve_recipe(parent: list) -> list:
        '''compare parent recipe and 5 of its children and return the one with the best score'''
        recipes =  [parent] + [make_child_recipe(parent) for _ in range(5)]
        best_recipe = max(recipes, key=lambda r: get_score(r))
        return best_recipe


    lines = [list(map(int, re.findall('(-?\d)', line))) for line in puzzle_input.split('\n')]
    recipe = [30, 30, 20, 20]
    for _ in range(100):
        recipe = improve_recipe(recipe)

    return get_score(recipe)


def aoc2015_day15_part2(puzzle_input):

    def get_score(recipe: list) -> int:
        '''calculate total score of cookie'''
        capacity = sum([recipe[i] * lines[i][0] for i in range(len(lines))])
        durability = sum([recipe[i] * lines[i][1] for i in range(len(lines))])
        flavor = sum([recipe[i] * lines[i][2] for i in range(len(lines))])
        texture = sum([recipe[i] * lines[i][3] for i in range(len(lines))])
        score = capacity * durability * flavor * texture
        return score

    def make_child_recipe(recipe: list) -> list:
        '''Alter recipe by randomly adding and removing 10 teaspoons of ingredients.'''
        child = recipe.copy()
        for _ in range(5):
            child[random.randint(0, 1)] += 1
        for _ in range(5):
            child[random.randint(0, 1)] -= 1
        for _ in range(5):
            child[random.randint(2, 3)] += 1
        for _ in range(5):
            child[random.randint(2, 3)] -= 1  
        return child

    def improve_recipe(parent: list) -> list:
        '''Compare parent recipe and 5 of its children and return the one with the best score'''
        recipes =  [parent] + [make_child_recipe(parent) for _ in range(5)]
        best_recipe = max(recipes, key=lambda r: get_score(r))
        return best_recipe

    lines = [list(map(int, re.findall('(-?\d)', line))) for line in puzzle_input.split('\n')]
    recipe = [30, 30, 20, 20]
    for _ in range(100):
        recipe = improve_recipe(recipe)

    return get_score(recipe)


####################################################################################################


def aoc2015_day16_part1(puzzle_input):

    regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
    sues = {int(i): {a: int(b), c: int(d), e: int(f)} for i, a, b, c, d, e, f in re.findall(regex, puzzle_input)}
    evidence = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    for sue, items in sues.items():
        for i, count in items.items():
            if count != evidence[i]:
                break
        else:
            return sue
        

def aoc2015_day16_part2(puzzle_input):

    regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
    sues = {int(i): {a: int(b), c: int(d), e: int(f)} for i, a, b, c, d, e, f in re.findall(regex, puzzle_input)}
    evidence = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    for sue, items in sues.items():
        for i, count in items.items():
            if i in ('cats', 'trees'):
                if count <= evidence[i]:
                    break
            elif i in ('pomeranians', 'goldfish'):
                if count >= evidence[i]:
                    break
            elif count != evidence[i]:
                break
        else:
            return sue


####################################################################################################


def aoc2015_day17_part1(puzzle_input):

    def dfs(i: int, current: list, total: int) -> None:
        '''recursive depth-first-search algorithm that keeps adding containers until target is either reached or surpassed'''

        if total == 150:
            combinations.append(current.copy())
            return

        elif i >= len(containers) or total > 150:
            return

        current.append(containers[i])
        dfs(i + 1, current, total + containers[i])
        current.pop()
        dfs(i + 1, current, total)

    containers = list(map(int, puzzle_input.split('\n')))
    combinations = []
    dfs(0, [], 0)
    return len(combinations)


def aoc2015_day17_part2(puzzle_input):

    def dfs(i: int, current: list, total: int) -> None:
        '''recursive depth-first-search algorithm that keeps adding containers until target is either reached or surpassed'''

        if total == 150:
            combinations.append(current.copy())
            return

        elif i >= len(containers) or total > 150:
            return

        current.append(containers[i])
        dfs(i + 1, current, total + containers[i])
        current.pop()
        dfs(i + 1, current, total)

    containers = list(map(int, puzzle_input.split('\n')))
    combinations = []
    dfs(0, [], 0)
    comb_lengths = sorted([len(c) for c in combinations])
    min_length = [l for l in comb_lengths if l == comb_lengths[0]]
    return len(min_length)


####################################################################################################


def aoc2015_day18_part1(puzzle_input):
    '''Need to redo this with numpy!'''

    def get_neighbors(x, y):
        return [(x+i, y+j) for i in range(-1,2) for j in range(-1,2) if x+i in range(len(grid)) and y+j in range(len(grid)) and (i,j) != (0,0)]

    def get_num_lit_neighbors(x, y, grid):
        return sum([grid[j][i] == 1 for i, j in get_neighbors(x, y)])

    def switch(grid):
        new_grid = [[0] * 100 for _ in range(100)]
        for y in range(len(grid)):
            for x in range(len(grid)):
                if (get_num_lit_neighbors(x, y, grid) == 3) or (grid[y][x] == 1 and get_num_lit_neighbors(x, y, grid) == 2):
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
        return new_grid

    grid = [[0] * 100 for _ in range(100)]
    for y, line in enumerate(puzzle_input.split('\n')):
        for x, val in enumerate(line):
            if val == '#':
                grid[y][x] = 1

    for _ in range(100):
        grid = switch(grid)

    return sum(sum(row) for row in grid)


def aoc2015_day18_part2(puzzle_input):
    '''Need to redo this with numpy!'''

    def get_neighbors(x, y):
        return [(x+i, y+j) for i in range(-1,2) for j in range(-1,2) if x+i in range(len(grid)) and y+j in range(len(grid)) and (i,j) != (0,0)]

    def get_num_lit_neighbors(x, y, grid):
        return sum([grid[j][i] == 1 for i, j in get_neighbors(x, y)])

    def switch(grid):
        new_grid = [[0] * 100 for _ in range(100)]
        corners = [(0, 0), (99, 0), (0, 99), (99, 99)]
        for y in range(len(grid)):
            for x in range(len(grid)):
                if ((x, y) in corners) or (get_num_lit_neighbors(x, y, grid) == 3) or (grid[y][x] == 1 and get_num_lit_neighbors(x, y, grid) == 2):
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
        return new_grid

    grid = [[0] * 100 for _ in range(100)]
    for y, line in enumerate(puzzle_input.split('\n')):
        for x, val in enumerate(line):
            if val == '#':
                grid[y][x] = 1

    for _ in range(100):
        grid = switch(grid)

    return sum(sum(row) for row in grid)


####################################################################################################


def aoc2015_day19_part1(puzzle_input):

    lines = puzzle_input.split('\n')
    replacements = [line.split(' => ') for line in lines[:-2]]
    formula = lines[-1]

    molecules = set()
    for x, y in replacements:
        for i in range(len(formula)):
            if formula[i:i+len(x)] == x:
                mol = formula[:i] + y + formula[i+len(x):]
                molecules.add(mol)

    return len(molecules)


def aoc2015_day19_part2(puzzle_input):

    def convert(formula: str) -> str:
        for x, y in replacements:
            for i in range(len(formula)):
                if formula[i:i+len(y)] == y:
                    mol = formula[:i] + x + formula[i+len(y):]
                    yield mol
                    
    def dfs(i: int, visited: list, last: list, mol: str) -> None:
        if mol == 'e':
            num.append(i)
            return
        else:
            for new_mol in convert(mol):
                if new_mol in visited:
                    continue
                else:
                    visited.append(new_mol)
                    last.append(new_mol)
                    dfs(i + 1, visited, last, new_mol)
                    return
            last.pop()
            dfs(i-1, visited, last, last[-1]) 

    lines = puzzle_input.split('\n')
    replacements = [line.split(' => ') for line in lines[:-2]]
    formula = lines[-1]
    num = []
    dfs(0, [formula], [formula], formula)
    return num[0]


####################################################################################################


def aoc2015_day20_part1(puzzle_input):

    num = int(puzzle_input)
    i = 700000
    while True:
        i += 1
        presents = sum(sympy.divisors(i)) * 10
        if presents >= num:
            break
    
    return i


def aoc2015_day20_part2(puzzle_input):
    
    num = int(puzzle_input)
    i = 700000
    while True:
        i += 1
        presents = sum([div for div in sympy.divisors(i) if div > i / 50]) * 11
        if presents >= num:
            break
    
    return i


####################################################################################################


def aoc2015_day21_part1(puzzle_input):

    # Parse input and equipment stats
    boss_hp, boss_dmg, boss_arm = map(int, re.findall(r'(\d+)', puzzle_input))
    equips = '''\
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''
    equips = [[int(x) if x.isnumeric() else x for x in re.split('\s\s+', e)] for e in equips.split('\n')]

    weapons = equips[1:6]
    armor = equips[8:13]
    rings = equips[15:-1]

    armor.append(['No Armor', 0, 0, 0]) 
    rings.append(['No Ring', 0, 0, 0])


    def fight(player_dmg: int, player_arm: int, boss_hp: int=boss_hp) -> str:
        '''Simulates fight with given equipment and stats. Returns string about who wins.'''
        player_hp = 100
        player_net_dmg = player_dmg - boss_arm if player_dmg > 1 else 1
        boss_net_dmg = boss_dmg - player_arm if boss_dmg > player_arm else 1
        while True:
            boss_hp -= player_net_dmg
            if boss_hp <= 0:
                return 'player wins'
            player_hp -= boss_net_dmg
            if player_hp <= 0:
                return 'boss wins'

    # Get every possible equipment combination    
    equip_combs = []
    for w in weapons:
        for a in armor:
            for r1 in rings:
                for r2 in rings:
                    if r2 == r1 and r1[0] != 'No Ring':
                        continue
                    cost = w[1] + a[1] + r1[1] + r2[1]
                    dmg = w[2] + r1[2] + r2[2]
                    arm = a[3] + r1[3] + r2[3]
                    equip_combs.append((w, a, r1, r2, dmg, arm, cost))

    # Iterate through equipment combinations sorted by cost and return the cheapest
    for c in sorted(equip_combs, key=lambda x: x[-1]):
        result = fight(c[4], c[5])
        if result == 'player wins':
            break 
        
    return c[-1]


def aoc2015_day21_part2(puzzle_input):

    # Parse input and equipment stats
    boss_hp, boss_dmg, boss_arm = map(int, re.findall(r'(\d+)', puzzle_input))
    equips = '''\
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''
    equips = [[int(x) if x.isnumeric() else x for x in re.split('\s\s+', e)] for e in equips.split('\n')]

    weapons = equips[1:6]
    armor = equips[8:13]
    rings = equips[15:-1]

    armor.append(['No Armor', 0, 0, 0]) 
    rings.append(['No Ring', 0, 0, 0])

    def fight(player_dmg: int, player_arm: int, boss_hp: int=boss_hp) -> str:
        '''Simulates fight with given equipment and stats. Returns string about who wins.'''
        player_hp = 100
        player_net_dmg = player_dmg - boss_arm if player_dmg > 1 else 1
        boss_net_dmg = boss_dmg - player_arm if boss_dmg > player_arm else 1
        while True:
            boss_hp -= player_net_dmg
            if boss_hp <= 0:
                return 'player wins'
            player_hp -= boss_net_dmg
            if player_hp <= 0:
                return 'boss wins'

    # Get every possible equipment combination    
    equip_combs = []
    for w in weapons:
        for a in armor:
            for r1 in rings:
                for r2 in rings:
                    if r2 == r1 and r1[0] != 'No Ring':
                        continue
                    cost = w[1] + a[1] + r1[1] + r2[1]
                    dmg = w[2] + r1[2] + r2[2]
                    arm = a[3] + r1[3] + r2[3]
                    equip_combs.append((w, a, r1, r2, dmg, arm, cost))

    # Iterate through equipment combinations sorted by cost in reverse and return the most expensive
    for c in sorted(equip_combs, key=lambda x: -x[-1]):
        result = fight(c[4], c[5])
        if result == 'boss wins':
            break

    return c[-1]


####################################################################################################


def aoc2015_day22_part1(puzzle_input):
    """
    I'm kind of brute forcing it by playing the game a very large number of times 
    (500_000 seems to do the trick) using a completely random strategy. 
    Maybe not the most elegant or efficient solution.
    """

    boss_hp, boss_dmg = map(int, re.findall(r'(\d+)', puzzle_input))

    @dataclass
    class GameState:
        hard_mode: bool
        best_score: int
        boss_hp: int
        player_turn: int = 1
        poison: int = 0
        shield: int = 0
        recharge: int = 0
        mana: int = 500
        spent_mana: int = 0
        player_hp: int = 50
        

    def play_game(s: GameState) -> int | bool:
        
        if s.poison > 0:
            s.poison -= 1
            s.boss_hp -= 3
            if s.boss_hp <= 0:  # Player wins!
                return s.spent_mana
        
        if s.shield > 0:
            s.shield -= 1
    
        if s.recharge > 0:
            s.mana += 101
            s.recharge -= 1
            
        if s.player_turn:
            if s.hard_mode:
                s.player_hp -= 1
                if not s.player_hp:  # Boss wins!
                    return False

            while True:
                spell = random.choice(['magic missle', 'drain', 'shield', 'poison', 'recharge'])

                if spell == 'magic missle':
                    cost = 53
                    if s.mana < cost:
                        return False
                    s.boss_hp -= 4

                elif spell=='drain':
                    cost = 73
                    if s.mana < cost:
                        continue
                    s.boss_hp -= 2
                    s.player_hp += 2

                elif spell=='shield':
                    cost = 113
                    if s.mana < cost or s.shield:
                        continue
                    s.shield = 6

                elif spell=='poison':
                    cost = 173
                    if s.mana < cost or s.poison:
                        continue
                    s.poison = 6

                elif spell=='recharge':
                    cost = 229
                    if s.mana < cost or s.recharge:
                        continue
                    s.recharge = 5

                break
            
            s.mana -= cost
            s.spent_mana += cost
            if s.best_score and s.spent_mana > s.best_score:
                return False  # Player might still win but not optimally!
            
            if s.boss_hp <= 0:
                return s.spent_mana  # Player wins!
        
        else:  # Boss' turn
            player_armor = 7 if s.shield else 0
            s.player_hp -= max(boss_dmg - player_armor, 1)

            if s.player_hp <= 0:  # Boss wins!
                return False

        s.player_turn = 1 - s.player_turn
        return play_game(s)

    best_score = None
    for _ in range(500_000):
        score = play_game(GameState(hard_mode=False, best_score=best_score, boss_hp=boss_hp))
        if score and (not best_score or best_score > score):
            best_score = score
        
    return best_score


def aoc2015_day22_part2(puzzle_input):
    """
    I'm kind of brute forcing it by playing the game a very large number of times 
    (500_000 seems to do the trick) using a completely random strategy. 
    Maybe not the most elegant or efficient solution.
    """

    boss_hp, boss_dmg = map(int, re.findall(r'(\d+)', puzzle_input))

    @dataclass
    class GameState:
        hard_mode: bool
        best_score: int
        boss_hp: int
        player_turn: int = 1
        poison: int = 0
        shield: int = 0
        recharge: int = 0
        mana: int = 500
        spent_mana: int = 0
        player_hp: int = 50
        

    def play_game(s: GameState) -> int | bool:
        
        if s.poison > 0:
            s.poison -= 1
            s.boss_hp -= 3
            if s.boss_hp <= 0:  # Player wins!
                return s.spent_mana
        
        if s.shield > 0:
            s.shield -= 1
    
        if s.recharge > 0:
            s.mana += 101
            s.recharge -= 1
            
        if s.player_turn:
            if s.hard_mode:
                s.player_hp -= 1
                if not s.player_hp:  # Boss wins!
                    return False

            while True:
                spell = random.choice(['magic missle', 'drain', 'shield', 'poison', 'recharge'])

                if spell == 'magic missle':
                    cost = 53
                    if s.mana < cost:
                        return False
                    s.boss_hp -= 4

                elif spell=='drain':
                    cost = 73
                    if s.mana < cost:
                        continue
                    s.boss_hp -= 2
                    s.player_hp += 2

                elif spell=='shield':
                    cost = 113
                    if s.mana < cost or s.shield:
                        continue
                    s.shield = 6

                elif spell=='poison':
                    cost = 173
                    if s.mana < cost or s.poison:
                        continue
                    s.poison = 6

                elif spell=='recharge':
                    cost = 229
                    if s.mana < cost or s.recharge:
                        continue
                    s.recharge = 5

                break
            
            s.mana -= cost
            s.spent_mana += cost
            if s.best_score and s.spent_mana > s.best_score:
                return False  # Might still win but not optimally
            
            if s.boss_hp <= 0:
                return s.spent_mana  # Player wins!
        
        else:  # Boss' turn
            player_armor = 7 if s.shield else 0
            s.player_hp -= max(boss_dmg - player_armor, 1)

            if s.player_hp <= 0:  # Boss wins!
                return False

        s.player_turn = 1 - s.player_turn
        return play_game(s)

    best_score = None
    for _ in range(500_000):
        score = play_game(GameState(hard_mode=True, best_score=best_score, boss_hp=boss_hp))
        if score and (not best_score or best_score > score):
            best_score = score
        
    return best_score


####################################################################################################


def aoc2015_day23_part1(puzzle_input):
    ins = [line.split() for line in puzzle_input.split('\n')]
    d = {'a': 0, 'b': 0}
    i = 0
    while i in range(len(ins)):
        if ins[i][0] == 'hlf':
            d[ins[i][1]] /= 2
        elif ins[i][0] == 'tpl':
            d[ins[i][1]] *= 3
        elif ins[i][0] == 'inc':
            d[ins[i][1]] += 1
        elif ins[i][0] == 'jmp':
            i += int(ins[i][1])
            continue
        elif ins[i][0] == 'jie':
            if d[ins[i][1].strip(',')] % 2 == 0:
                i += int(ins[i][2])
                continue
        elif ins[i][0] == 'jio':
            if d[ins[i][1].strip(',')] == 1:
                i += int(ins[i][2])
                continue
        i += 1
    return d['b']


def aoc2015_day23_part2(puzzle_input):
    ins = [line.split() for line in puzzle_input.split('\n')]
    d = {'a': 1, 'b': 0}
    i = 0
    while i in range(len(ins)):
        if ins[i][0] == 'hlf':
            d[ins[i][1]] /= 2
        elif ins[i][0] == 'tpl':
            d[ins[i][1]] *= 3
        elif ins[i][0] == 'inc':
            d[ins[i][1]] += 1
        elif ins[i][0] == 'jmp':
            i += int(ins[i][1])
            continue
        elif ins[i][0] == 'jie':
            if d[ins[i][1].strip(',')] % 2 == 0:
                i += int(ins[i][2])
                continue
        elif ins[i][0] == 'jio':
            if d[ins[i][1].strip(',')] == 1:
                i += int(ins[i][2])
                continue
        i += 1
    return d['b']


####################################################################################################


def aoc2015_day24_part1(puzzle_input):

    data = list(map(int, puzzle_input.split()))
    target = sum(data) / 3
    i = 0
    valid_combs = []
    while not valid_combs: 
        i += 1
        valid_combs = [c for c in combinations(data, i) if sum(c) == target]  

    return min(np.prod(c) for c in valid_combs)


def aoc2015_day24_part2(puzzle_input):

    data = list(map(int, puzzle_input.split()))
    target = sum(data) / 4
    i = 0
    valid_combs = []
    while not valid_combs: 
        i += 1
        valid_combs = [c for c in combinations(data, i) if sum(c) == target]  

    return min(np.prod(c) for c in valid_combs)


####################################################################################################


def aoc2015_day25_part1(puzzle_input):

    instruction = puzzle_input.split()
    x, y = [int(instruction[i].strip(',.')) for i in (-1, -3)]
    col = row = i = 1
    while (col, row) != (x, y):
        if col > 1:
            row += 1
            col -= 1
        else:
            col = row + 1
            row = 1
        i += 1
    
    code = 20151125
    for _ in range(i-1):
        code *= 252533
        code %= 33554393

    return code