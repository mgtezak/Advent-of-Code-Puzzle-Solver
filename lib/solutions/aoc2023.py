import re
import math
from functools import cmp_to_key, cache
from itertools import cycle, combinations, count
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
import operator

import numpy as np
import sympy as sp
import networkx as nx


def aoc2023_day1_part1(puzzle_input):

    total = 0

    for line in puzzle_input.split('\n'):
        digits = re.findall(r'(\d)', line)
        total += int(digits[0] + digits[-1])

    return total


def aoc2023_day1_part2(puzzle_input):

    def get_digit(x):
        return x if x.isnumeric() else str(letter_digits.index(x))
    
    letter_digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'  
    total = 0

    for line in puzzle_input.split('\n'):
        digits = re.findall(regex, line)
        total += int(get_digit(digits[0]) + get_digit(digits[-1]))

    return total


####################################################################################################


def aoc2023_day2_part1(puzzle_input):

    possible = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = 0
    for id, game in enumerate(puzzle_input.split('\n'), start=1):
        game = game.split(': ')[1]
        for hand in game.split('; '):
            is_impossible = False
            for subset in hand.split(', '):
                n, color = subset.split()
                if int(n) > possible[color]:
                    is_impossible = True
                    break
            if is_impossible:
                break
        else:
            possible_games += id

    return possible_games


def aoc2023_day2_part2(puzzle_input):
    power = 0
    for game in puzzle_input.split('\n'):
        game = game.split(': ')[1]
        max_number = {'red': 0, 'green': 0, 'blue': 0}
        for hand in game.split('; '):
            for subset in hand.split(', '):
                n, color = subset.split()
                max_number[color] = max(int(n), max_number[color])

        power += max_number['red'] * max_number['green'] * max_number['blue']

    return power


####################################################################################################


def aoc2023_day3_part1(puzzle_input):

    lines = puzzle_input.split('\n')

    symbol_regex = r'[^.\d]'
    symbol_adjacent = set()
    for i, line in enumerate(lines):
        for m in re.finditer(symbol_regex, line):
            j = m.start()
            symbol_adjacent |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}

    number_regex = r'\d+'
    part_num_sum = 0
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            if any((i, j) in symbol_adjacent for j in range(*m.span())):
                part_num_sum += int(m.group())

    return part_num_sum


def aoc2023_day3_part2(puzzle_input):

    lines = puzzle_input.split('\n')

    gear_regex = r'\*'
    gears = dict()
    for i, line in enumerate(lines):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []

    number_regex = r'\d+'
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            for r in range(i-1, i+2):
                for c in range(m.start()-1, m.end()+1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))

    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += math.prod(nums)

    return gear_ratio_sum


####################################################################################################


def aoc2023_day4_part1(puzzle_input):
    regex = r':(.*?)\|(.*)'
    points = 0
    for line in puzzle_input.split('\n'):
        nums = re.search(regex, line)
        win_nums = set(map(int, nums.group(1).split()))
        true_nums = set(map(int, nums.group(2).split()))
        n_matches = len(win_nums & true_nums)
        if n_matches:
            points += 2 ** (n_matches - 1)

    return points


def aoc2023_day4_part2(puzzle_input):
    lines = puzzle_input.split('\n')
    cards = [1] * len(lines)
    regex = r':(.*?)\|(.*)'
    for i, line in enumerate(lines):
        nums = re.search(regex, line)
        win_nums = set(map(int, nums.group(1).split()))
        true_nums = set(map(int, nums.group(2).split()))
        n_matches = len(win_nums & true_nums)
        for j in range(i + 1, i + 1 + n_matches):
            cards[j] += cards[i]
    
    return sum(cards)


####################################################################################################


def aoc2023_day5_part1(puzzle_input):
    segments = puzzle_input.split('\n\n')
    seeds = re.findall(r'\d+', segments[0])

    min_location = float('inf')
    for x in map(int, seeds):
        for seg in segments[1:]:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
                destination, start, delta = map(int, conversion)
                if x in range(start, start + delta):
                    x += destination - start
                    break

        min_location = min(x, min_location)

    return min_location


def aoc2023_day5_part2(puzzle_input):
    segments = puzzle_input.split('\n\n')
    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))
  
    return min_location


####################################################################################################


def aoc2023_day6_part1(puzzle_input):
    times, distances = puzzle_input.split('\n')
    times = list(map(int, re.findall('\d+', times)))
    distances = list(map(int, re.findall('\d+', distances)))
    total = 1
    for t, d in zip(times, distances):
        wins = 0
        speed = 0
        for acceleration in range(1, t):
            speed += 1
            travelled = (t-acceleration) * speed
            if travelled > d:
                wins += (travelled > d)
            elif wins:
                break

        total *= wins
    
    return total


def aoc2023_day6_part2(puzzle_input):
    time, distance = puzzle_input.split('\n')
    time = int(''.join(re.findall('\d+', time)))
    distance = int(''.join(re.findall('\d+', distance)))
    exact_acceleration = (time - math.sqrt((time**2 - 4*distance))) / 2
    min_acceleration = int(exact_acceleration + 1)
    return time - 2*min_acceleration + 1


####################################################################################################


def aoc2023_day7_part1(puzzle_input):

    def get_type(hand):
        counts = sorted(Counter(hand).values(), reverse=True)
        if counts[0] == 5:
            return 6
        if counts[0] == 4:
            return 5
        if counts[0] == 3 and counts[1] == 2:
            return 4
        if counts[0] == 3:
            return 3
        if counts[0] == 2 and counts[1] == 2:
            return 2
        if counts[0] == 2:
            return 1
        return 0  
      
    def compare(a, b):
        type_a = get_type(a[0])
        type_b = get_type(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (cards.index(card_a) > cards.index(card_b))
            return 1 if a_wins else -1

    cards = '23456789TJQKA'
    regex = r'(\w{5}) (\d+)'
    hands = re.findall(regex, puzzle_input)
    hands.sort(key=cmp_to_key(compare))
    total = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        total += rank * int(bid)

    return total


def aoc2023_day7_part2(puzzle_input):

    def get_type(hand):
        jokers = hand.count('J')
        hand = [c for c in hand if c != 'J']
        counts = sorted(Counter(hand).values(), reverse=True)
        if not counts:
            counts = [0]
        if counts[0] + jokers == 5:
            return 6
        if counts[0] + jokers == 4:
            return 5
        if counts[0] + jokers == 3 and counts[1] == 2:
            return 4
        if counts[0] + jokers == 3:
            return 3
        if counts[0] == 2 and (jokers or counts[1] == 2):
            return 2
        if counts[0] == 2 or jokers:
            return 1
        return 0
    
    def compare(a, b):
        type_a = get_type(a[0])
        type_b = get_type(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (cards.index(card_a) > cards.index(card_b))
            return 1 if a_wins else -1

    cards = 'J23456789TQKA'
    regex = r'(\w{5}) (\d+)'
    hands = re.findall(regex, puzzle_input)
    hands.sort(key=cmp_to_key(compare))
    total = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        total += rank * int(bid)

    return total


####################################################################################################


def aoc2023_day8_part1(puzzle_input):
    directions, connections = puzzle_input.split('\n\n')
    directions = cycle(0 if d == 'L' else 1 for d in directions)
    graph = {}
    regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    for node, left, right in re.findall(regex, connections):
        graph[node] = [left, right]

    node = 'AAA'
    for steps, d in enumerate(directions, start=1):
        node = graph[node][d]
        if node == 'ZZZ':
            break

    return steps


def aoc2023_day8_part2(puzzle_input):
    directions, connections = puzzle_input.split('\n\n')
    directions = [0 if d == 'L' else 1 for d in directions]
    graph = {}
    regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    for node, left, right in re.findall(regex, connections):
        graph[node] = [left, right]

    starting_nodes = [node for node in graph if node[2] == 'A']
    cycles = []
    for node in starting_nodes:
        for steps, d in enumerate(cycle(directions), start=1):
            node = graph[node][d]
            if node[2] == 'Z':
                cycles.append(steps)
                break

    return math.lcm(*cycles)


####################################################################################################


def aoc2023_day9_part1(puzzle_input):
    total = 0
    for line in puzzle_input.split('\n'):
        nums = [int(n) for n in line.split()]
        final_nums = []

        while set(nums) != set([0]):
            final_nums.append(nums[-1])
            nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]

        total += sum(final_nums)

    return total


def aoc2023_day9_part2(puzzle_input):
    total = 0
    for line in puzzle_input.split('\n'):
        nums = [int(n) for n in line.split()]
        first_nums = []
        
        while set(nums) != set([0]):
            first_nums.append(nums[0])
            nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]

        for i, num in enumerate(first_nums):
            total += num if i % 2 == 0 else -num

    return total


####################################################################################################


def aoc2023_day10_part1(puzzle_input):

    grid = puzzle_input.split()
    graph = {}
    for x, line in enumerate(grid):
        for y, tile in enumerate(line):
            adjacent = []
            if tile in '-J7S':
                adjacent.append((x, y-1))
            if tile in '-FLS':
                adjacent.append((x, y+1))
            if tile in '|F7S':
                adjacent.append((x+1, y))      
            if tile in '|LJS':
                adjacent.append((x-1, y))
            if tile == 'S':
                visited = set([(x, y)])
                q = set([(x, y)])
            graph[(x, y)] = adjacent

    steps = -1
    while q:
        nxt = set()
        for x1, y1 in q:
            for x2, y2 in graph[(x1, y1)]:
                if (x2, y2) not in visited and (x1, y1) in graph.get((x2, y2), []): 
                    nxt.add((x2, y2))
                    visited.add((x2, y2))
        q = nxt
        steps += 1

    return steps


def aoc2023_day10_part2(puzzle_input):
    
    grid = puzzle_input.split()
    graph = {}
    for x, line in enumerate(grid):
        for y, tile in enumerate(line):
            adjacent = []
            if tile in '-J7S':
                adjacent.append((x, y-1))
            if tile in '-FLS':
                adjacent.append((x, y+1))
            if tile in '|F7S':
                adjacent.append((x+1, y))      
            if tile in '|LJS':
                adjacent.append((x-1, y))
            if tile == 'S':
                tile_q = set([(x, y)])
            graph[(x, y)] = adjacent

    pipes = set()
    while tile_q:
        nxt = set()
        for x1, y1 in tile_q:
            for x2, y2 in graph[(x1, y1)]:
                if (x1, y1) not in graph.get((x2, y2), []):
                    continue
                pipe = (*sorted((x1, x2)), *sorted((y1, y2)))
                if pipe not in pipes:
                    pipes.add(pipe)
                    nxt.add((x2, y2))
        tile_q = nxt

    m, n = len(grid), len(grid[0])
    visited = set()
    corner_q = [(0, 0)]

    while corner_q:
        x, y = corner_q.pop()
        requirements = (x > 0, y < n, x < m, y > 0)
        adjacent = ((x-1, y), (x, y+1), (x+1, y), (x, y-1))
        tile_pairs = ((x-1, x-1, y-1, y),   # up
                      (x-1, x, y, y),       # right
                      (x, x, y-1, y),       # down
                      (x-1, x, y-1, y-1))   # left
        for req, corner, tile_pair in zip(requirements, adjacent, tile_pairs):
            if req and corner not in visited and tile_pair not in pipes:
                visited.add(corner)
                corner_q.append(corner)

    total = m * n - len(pipes)
    for i in range(m):
        for j in range(n):
            corners = ((i, j), (i+1, j), (i, j+1), (i+1, j+1))
            if all(c in visited for c in corners):
                total -= 1

    return total


####################################################################################################


def aoc2023_day11_part1(puzzle_input):
    grid = [[ele for ele in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])

    i = 0
    while i < len(grid):
        if '#' not in grid[i]:
            grid.insert(i, ['.'] * n)
            m += 1
            i += 2
        else:
            i += 1

    j = 0
    while j < len(grid[0]):
        if '#' not in [grid[i][j] for i in range(m)]:
            for i in range(m):
                grid[i].insert(j, '.')
            n += 1
            j += 2
        else:
            j += 1

    galaxies = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == '#']
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        total += abs(x1-x2) + abs(y1-y2)
    
    return total


def aoc2023_day11_part2(puzzle_input):
    grid = [[ele for ele in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])

    empty_rows = [i for i in range(m) if '#' not in grid[i]]
    empty_cols = [j for j in range(n) if all(grid[i][j] == '.' for i in range(m))]
    galaxies = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == '#']
    
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        add_rows = 999_999 * sum(r in range(x1, x2) for r in empty_rows)
        add_cols = 999_999 * sum(c in range(y1, y2) for c in empty_cols)
        total += x2 - x1 + add_rows + y2 - y1 + add_cols

    return total


####################################################################################################


def aoc2023_day12_part1(puzzle_input):

    @cache
    def dfs(sequence, groups):
        if not groups:
            return '#' not in sequence
        seq_len = len(sequence)
        group_len = groups[0]
        if seq_len - sum(groups) - len(groups) + 1 < 0:
            return 0
        has_holes = any(sequence[x] == '.' for x in range(group_len))
        if seq_len == group_len:
            return 0 if has_holes else 1
        can_use = not has_holes and (sequence[group_len] != '#')
        if sequence[0] == '#':
            return dfs(sequence[group_len+1:].lstrip('.'), tuple(groups[1:])) if can_use else 0
        skip = dfs(sequence[1:].lstrip('.'), groups)
        if not can_use:
            return skip
        return skip + dfs(sequence[group_len+1:].lstrip('.'), tuple(groups[1:]))
                        
    total = 0
    for line in puzzle_input.split('\n'):
        sequence, groups = line.split()
        groups = [int(g) for g in groups.split(',')]
        total += dfs(sequence, tuple(groups))
        
    return total


def aoc2023_day12_part2(puzzle_input):

    @cache
    def dfs(sequence, groups):
        if not groups:
            return '#' not in sequence
        seq_len = len(sequence)
        group_len = groups[0]
        if seq_len - sum(groups) - len(groups) + 1 < 0:
            return 0
        has_holes = any(sequence[x] == '.' for x in range(group_len))
        if seq_len == group_len:
            return 0 if has_holes else 1
        can_use = not has_holes and (sequence[group_len] != '#')
        if sequence[0] == '#':
            return dfs(sequence[group_len+1:].lstrip('.'), tuple(groups[1:])) if can_use else 0
        skip = dfs(sequence[1:].lstrip('.'), groups)
        if not can_use:
            return skip
        return skip + dfs(sequence[group_len+1:].lstrip('.'), tuple(groups[1:]))
        
    total = 0
    for line in puzzle_input.split('\n'):
        sequence, groups = line.split()
        sequence = '?'.join([sequence] * 5).lstrip('.')
        groups = [int(g) for g in groups.split(',')] * 5
        total += dfs(sequence, tuple(groups))
    
    return total


####################################################################################################


def aoc2023_day13_part1(puzzle_input):

    def get_mirror_row(grid):
        n_rows = grid.shape[0]
        for r in range(1, n_rows):
            span = min(r, n_rows-r)
            top = grid[r-span : r][::-1]
            bottom = grid[r : r+span]
            if np.array_equal(top, bottom):
                return r
        return None
    
    def get_mirror_col(grid):
        n_cols = grid.shape[1]
        for c in range(1, n_cols):
            span = min(c, n_cols-c)
            left = grid[:, c-span:c][:, ::-1]
            right = grid[:, c:c+span]
            if np.array_equal(left, right):
                return c
        return None

    grids = puzzle_input.split('\n\n')
    total = 0
    for grid in grids:
        grid = np.array([list(row) for row in grid.split('\n')])
        if (r := get_mirror_row(grid)) is not None:
            total += r * 100
        else:
            total += get_mirror_col(grid)

    return total


def aoc2023_day13_part2(puzzle_input):

    def get_smudge_row(grid):
        n_rows = grid.shape[0]
        for r in range(1, n_rows):
            span = min(r, n_rows-r)
            top = grid[r-span : r][::-1]
            bottom = grid[r : r+span]
            if (top != bottom).sum() == 1:
                return r
        return None
    
    def get_smudge_col(grid):
        n_cols = grid.shape[1]
        for c in range(1, n_cols):
            span = min(c, n_cols-c)
            left = grid[:, c-span:c][:, ::-1]
            right = grid[:, c:c+span]
            if (left != right).sum() == 1:
                return c
        return None

    grids = puzzle_input.split('\n\n')
    total = 0
    for grid in grids:
        grid = np.array([list(row) for row in grid.split('\n')])
        if (r := get_smudge_row(grid)) is not None:
            total += r * 100
        else:
            total += get_smudge_col(grid)

    return total


####################################################################################################


def aoc2023_day14_part1(puzzle_input):
    grid = [list(row) for row in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    for c in range(n):
        lim = 0
        for r in range(m):
            if grid[r][c] == '#':
                lim = r + 1
            elif grid[r][c] == 'O':
                if r > lim:
                    grid[lim][c] = 'O'
                    grid[r][c] = '.'
                lim += 1

    total_load = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 'O':
                total_load += m - r

    return total_load


def aoc2023_day14_part2(puzzle_input):
   
    def spin_cycle():
        # north
        for c in range(n):
            lim = 0
            for r in range(m):
                if grid[r][c] == '#':
                    lim = r + 1
                elif grid[r][c] == 'O':
                    if r > lim:
                        grid[lim][c] = 'O'
                        grid[r][c] = '.'
                    lim += 1
        # west
        for r in range(m):
            lim = 0
            for c in range(n):
                if grid[r][c] == '#':
                    lim = c + 1
                elif grid[r][c] == 'O':
                    if c > lim:
                        grid[r][lim] = 'O'
                        grid[r][c] = '.'
                    lim += 1
        # south
        for c in range(n):
            lim = m - 1
            for r in reversed(range(m)):
                if grid[r][c] == '#':
                    lim = r - 1
                elif grid[r][c] == 'O':
                    if r < lim:
                        grid[lim][c] = 'O'
                        grid[r][c] = '.'
                    lim -= 1
        # east
        for r in range(m):
            lim = n - 1
            for c in reversed(range(n)):
                if grid[r][c] == '#':
                    lim = c - 1
                elif grid[r][c] == 'O':
                    if c < lim:
                        grid[r][lim] = 'O'
                        grid[r][c] = '.'
                    lim -= 1

    # record loads over 300 spin cycles
    grid = [list(row) for row in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    loads = []
    history = {}
    for i in range(300):
        spin_cycle()
        total_load = sum((grid[r][c]=='O') * (m-r) for r in range(m) for c in range(n))
        loads.append(total_load)

        # check for repetition cycle
        if i > 20:
            state_hash = str(loads[-20:])
            if state_hash in history:
                rep_cycle_start = history[state_hash]
                rep_cycle_length = i - rep_cycle_start
                break
            history[state_hash] = i

    target = 1_000_000_000
    offset = (target - rep_cycle_start) % rep_cycle_length - 1  # -1 because initial load was not recorded 
    return loads[rep_cycle_start + offset]


####################################################################################################


def aoc2023_day15_part1(puzzle_input):
    total = 0
    for step in puzzle_input.split(','):
        current_val = 0
        for char in step:
            current_val += ord(char)
            current_val *= 17
            current_val %= 256
        total += current_val

    return total


def aoc2023_day15_part2(puzzle_input):

    labels = defaultdict(list)
    lenses = defaultdict(list)
    regex = r'(\w+)(=|-)(\d+)?'
    for label, op, focal_len in re.findall(regex, puzzle_input):
        hash = 0
        for char in label:
            hash = (hash + ord(char)) * 17 % 256

        if label in labels[hash]:
            i = labels[hash].index(label)
            if op == '-':
                labels[hash].pop(i)
                lenses[hash].pop(i)
            else:
                lenses[hash][i] = int(focal_len)
        elif op == '=':
            labels[hash].append(label)
            lenses[hash].append(int(focal_len))

    total = 0
    for box, lenses in lenses.items():
        for i, focal_len in enumerate(lenses, start=1):
            total += (box+1) * i * focal_len
        
    return total


####################################################################################################


def aoc2023_day16_part1(puzzle_input):

    grid = [list(r) for r in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    visited = set()
    energized = set()
    queue = set([(0, 0, 'right')])   
    while queue:
        x, y, direction = queue.pop()
        energized.add((x, y))
        tile = grid[x][y]

        if y < n-1 and (x, y+1, 'right') not in visited and (
                (direction == 'right' and tile in '.-') or 
                (direction == 'up' and tile in '/-') or
                (direction == 'down' and tile in '\\-')):
            queue.add((x, y+1, 'right'))
            visited.add((x, y+1, 'right'))

        if x > 0 and (x-1, y, 'up') not in visited and (
                (direction == 'up' and tile in '.|') or 
                (direction == 'right' and tile in '/|') or
                (direction == 'left' and tile in '\\|')):
            queue.add((x-1, y, 'up'))
            visited.add((x-1, y, 'up'))

        if y > 0 and (x, y-1, 'left') not in visited and (
                (direction == 'left' and tile in '.-') or 
                (direction == 'up' and tile in '\\-') or
                (direction == 'down' and tile in '/-')):
            queue.add((x, y-1, 'left'))
            visited.add((x, y-1, 'left'))

        if x < m-1 and (x+1, y, 'down') not in visited and (
                (direction == 'down' and tile in '.|') or 
                (direction == 'right' and tile in '\\|') or
                (direction == 'left' and tile in '/|')):
            queue.add((x+1, y, 'down'))     
            visited.add((x+1, y, 'down'))

    return len(energized)


def aoc2023_day16_part2(puzzle_input):

    grid = [list(r) for r in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    initial = ({(x, 0, 'right') for x in range(m)} |
               {(x, n-1, 'left') for x in range(m)} |
               {(m-1, y, 'up') for y in range(n)} |
               {(0, y, 'down') for y in range(n)})
    
    best = 0
    for i in initial:
        visited = set()
        energized = set()
        queue = set([i])   
        while queue:
            x, y, direction = queue.pop()
            energized.add((x, y))
            tile = grid[x][y]

            if y < n-1 and (x, y+1, 'right') not in visited and (
                    (direction == 'right' and tile in '.-') or 
                    (direction == 'up' and tile in '/-') or
                    (direction == 'down' and tile in '\\-')):
                queue.add((x, y+1, 'right'))
                visited.add((x, y+1, 'right'))

            if x > 0 and (x-1, y, 'up') not in visited and (
                    (direction == 'up' and tile in '.|') or 
                    (direction == 'right' and tile in '/|') or
                    (direction == 'left' and tile in '\\|')):
                queue.add((x-1, y, 'up'))
                visited.add((x-1, y, 'up'))

            if y > 0 and (x, y-1, 'left') not in visited and (
                    (direction == 'left' and tile in '.-') or 
                    (direction == 'up' and tile in '\\-') or
                    (direction == 'down' and tile in '/-')):
                queue.add((x, y-1, 'left'))
                visited.add((x, y-1, 'left'))

            if x < m-1 and (x+1, y, 'down') not in visited and (
                    (direction == 'down' and tile in '.|') or 
                    (direction == 'right' and tile in '\\|') or
                    (direction == 'left' and tile in '/|')):
                queue.add((x+1, y, 'down'))     
                visited.add((x+1, y, 'down'))

        best = max(best, len(energized))

    return best


####################################################################################################


def aoc2023_day17_part1(puzzle_input):
    grid = [[int(d) for d in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    # tuple: (heat-loss, x-coord, y-coord, length-of-current-run, x-direction, y-direction)
    q = [(0, 0, 0, 0, 0, 0)] 
    visited = set()
    while q:
        loss, x, y, k, dx, dy = heappop(q)

        if x == m-1 and y == n-1:
            break

        if any((x, y, k_, dx, dy) in visited for k_ in range(1, k+1)):
            continue
    
        visited.add((x, y, k, dx, dy))
        for new_dx, new_dy in directions:
            straight = (new_dx == dx and new_dy == dy)
            new_x, new_y = x + new_dx, y + new_dy

            if any((new_dx == -dx and new_dy == -dy,
                    k == 3 and straight,
                    new_x < 0, new_y < 0, 
                    new_x == m, new_y == n)):
                continue

            new_k = k + 1 if straight else 1            
            heappush(q, (loss + grid[new_x][new_y], new_x, new_y, new_k, new_dx, new_dy))

    return loss


def aoc2023_day17_part2(puzzle_input):
    grid = [[int(d) for d in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    # tuple: (heat-loss, x-coord, y-coord, length-of-current-run, x-direction, y-direction)
    q = [(0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 1, 0)] 
    visited = set()
    while q:
        loss, x, y, k, dx, dy = heappop(q)

        if x == m-1 and y == n-1:
            if k < 4:
                continue
            break

        if (x, y, k, dx, dy) in visited:
            continue
    
        visited.add((x, y, k, dx, dy))

        for new_dx, new_dy in directions:
            straight = (new_dx == dx and new_dy == dy)
            new_x, new_y = x + new_dx, y + new_dy

            if any((new_dx == -dx and new_dy == -dy,
                    k == 10 and straight,
                    k < 4 and not straight,
                    new_x < 0, new_y < 0, 
                    new_x == m, new_y == n)):
                continue

            new_k = k + 1 if straight else 1
            heappush(q, (loss + grid[new_x][new_y], new_x, new_y, new_k, new_dx, new_dy))

    return loss


####################################################################################################


def aoc2023_day18_part1(puzzle_input):
    regex = r'(\w) (\d+)'
    directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    x = y = 0
    visited = set([(0, 0)])
    for d, steps in re.findall(regex, puzzle_input):
        dx, dy = directions[d]
        for _ in range(int(steps)):
            x += dx
            y += dy
            visited.add((x, y))
    
    # get top-left corner tile and start depth-first-search from its bottom-right neighbor
    x, y = min(visited)
    queue = [(x+1, y+1)]
    while queue:
        x1, y1 = queue.pop()
        for dx, dy in directions.values():
            x2, y2 = x1+dx, y1+dy
            if (x2, y2) not in visited:
                queue.append((x2, y2))
                visited.add((x2, y2))

    return len(visited)


def aoc2023_day18_part2(puzzle_input):
    regex = r'\(#([a-z0-9]+)([0-3])\)'
    directions = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    x = y = 0
    corners = [(0, 0)]
    boundary_area = 0
    for steps, d in re.findall(regex, puzzle_input):
        steps = int(steps, 16)
        dx, dy = directions[int(d)]
        x += dx * steps
        y += dy * steps
        boundary_area += steps
        corners.append((x, y))

    # Shoelace method
    interior_area = 0
    for i in range(len(corners)-1):
        (x1, y1), (x2, y2) =  corners[i:i+2]
        interior_area += x1*y2 - x2*y1
    interior_area = abs(interior_area) // 2

    # Pick's theorem
    total_area = interior_area + boundary_area//2 + 1

    return total_area


####################################################################################################


def aoc2023_day19_part1(puzzle_input):
    workflows, parts = puzzle_input.split('\n\n')
    work_regex = r'(\w+)\{([^}]+)\}'
    cond_regex = r'(\w+)(<|>)(\d+):(\w+)'
    flow = {}
    for name, rules in re.findall(work_regex, workflows):
        conditional = re.findall(cond_regex, rules)
        final = rules.split(',')[-1]
        flow[name] = conditional + [final]

    part_regex = r'x=(\d+),m=(\d+),a=(\d+),s=(\d+)'
    comp = {'>': operator.gt, '<': operator.lt}
    total_accepted = 0
    for part in re.findall(part_regex, parts):
        part = dict(zip('xmas', map(int, part)))
        curr = 'in'
        while curr not in ('A', 'R'):
            for cat, op, amt, res in flow[curr][:-1]:
                if comp[op](part[cat], int(amt)):
                    curr = res
                    break
            else:
                curr = flow[curr][-1]

        if curr == 'A':
            total_accepted += sum(part.values())

    return total_accepted


def aoc2023_day19_part2(puzzle_input):
    workflows, parts = puzzle_input.split('\n\n')
    work_regex = r'(\w+)\{([^}]+)\}'
    cond_regex = r'(\w+)(<|>)(\d+):(\w+)'
    flow = {}
    for name, rules in re.findall(work_regex, workflows):
        conditional = []
        for cat, op, amt, res in re.findall(cond_regex, rules):
            conditional.append(('xmas'.index(cat), op, int(amt), res))
        final = rules.split(',')[-1]
        flow[name] = conditional + [final]

    start = ('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000))
    queue = [start]
    total_accepted = 0
    while queue:
        curr, *intervals = queue.pop()
        if curr in ('A', 'R'):
            if curr == 'A':
                total_accepted += math.prod(hi-lo+1 for lo, hi in intervals)
            continue

        for cat_idx, op, amt, res in flow[curr][:-1]:
            lo, hi = intervals[cat_idx]

            # All passthrough, no transfer
            if (op == '>' and amt >= hi) or (op == '<' and amt <= lo):
                continue

            # All transfer no passthrough
            if (op == '>' and amt < lo) or (op == '<' and amt > hi):
                queue.append((res, *intervals))
                break

            # Some of both
            if op == '>':
                transfer = (amt+1, hi)
                passthrough = (lo, amt)
            else:
                transfer = (lo, amt-1)
                passthrough = (amt, hi)
            intervals[cat_idx] = passthrough
            intervals2 = intervals.copy()
            intervals2[cat_idx] = transfer
            queue.append((res, *intervals2))
        
        else: # Remaining is transferred
            queue.append((flow[curr][-1], *intervals))

    return total_accepted


####################################################################################################


def aoc2023_day20_part1(puzzle_input):
    graph = {}
    flip_flop = {}
    memory = {}
    for line in puzzle_input.split('\n'):
        source, destinations = line.split(' -> ')
        destinations = destinations.split(', ')
        graph[source.lstrip('%&')] = destinations
        if source.startswith('%'):
            flip_flop[source[1:]] = 0   # each flip flip is off (0) by default
        elif source.startswith('&'):
            memory[source[1:]] = {}

    for conjunction in memory.keys():   # get source modules for conjunctions 
        for source, destinatons in graph.items():
            if conjunction in destinatons:
                memory[conjunction][source] = 0   # initialize memory at low (0)

    signal_count = [0, 0]       # [low, high]
    for _ in range(1000):
        signal_count[0] += 1    # initial low signal from button to broadcaster
        queue = deque([('broadcaster', in_module, 0) for in_module in graph['broadcaster']])
        while queue:
            out_module, in_module, signal = queue.popleft()
            signal_count[signal] += 1

            if in_module in flip_flop and signal == 0:
                flip_flop[in_module] = 1 - flip_flop[in_module]
                out_signal = flip_flop[in_module]

            elif in_module in memory:
                memory[in_module][out_module] = signal
                out_signal = 1 if 0 in memory[in_module].values() else 0

            else:   # no output
                continue
            
            queue.extend([(in_module, nxt, out_signal) for nxt in graph[in_module]])

    return math.prod(signal_count)


def aoc2023_day20_part2(puzzle_input):
    graph = {}
    flip_flop = {}
    memory = {}
    for line in puzzle_input.split('\n'):
        source, destinations = line.split(' -> ')
        destinations = destinations.split(', ')
        graph[source.lstrip('%&')] = destinations
        if source.startswith('%'):
            flip_flop[source[1:]] = 0   # each flip flip is off (0) by default
        elif source.startswith('&'):
            memory[source[1:]] = {}

    for conjunction in memory.keys():   # get source modules for conjunctions 
        for source, destinatons in graph.items():
            if conjunction in destinatons:
                memory[conjunction][source] = 0   # initialize memory at low (0)

    final_layer = [m1 for m1 in graph if 'rx' in graph[m1]]
    assert len(final_layer) == 1, "Assumption #1: There is only 1 module pointing to rx"
    assert final_layer[0] in memory, "Assumption #2: The final module before rx is a conjunction"

    semi_final_layer = set(module for module in graph if final_layer[0] in graph[module])
    cycle_lengths = []  # Assumption #3: The modules on semi_final_layer signal high in regular intervals / cycles
    
    for button_push in count(1):
        queue = deque([('broadcaster', in_module, 0) for in_module in graph['broadcaster']])
        while queue:
            out_module, in_module, signal = queue.popleft()

            if in_module in flip_flop and signal == 0:
                flip_flop[in_module] = 1 - flip_flop[in_module]
                out_signal = flip_flop[in_module]

            elif in_module in memory:
                memory[in_module][out_module] = signal
                out_signal = 1 if 0 in memory[in_module].values() else 0
                if in_module in semi_final_layer and out_signal == 1:
                    cycle_lengths.append(button_push)
                    semi_final_layer.remove(in_module)

            else:   # no output
                continue
            
            queue.extend([(in_module, nxt, out_signal) for nxt in graph[in_module]])

        if not semi_final_layer:
            break

    return math.lcm(*cycle_lengths)


####################################################################################################


def aoc2023_day21_part1(puzzle_input):
    grid = [list(row) for row in puzzle_input.split('\n')]
    n, m = len(grid), len(grid[0])
    for x, row in enumerate(grid):
        if 'S' in row:
            start = (x, row.index('S'))
            break
    
    visited = set()
    queue = deque([start])
    total = 0
    for step in range(1, 65):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if i < 0 or j < 0 or i == n or j == m or (i, j) in visited or grid[i][j] == '#':
                    continue
                visited.add((i, j))
                queue.append((i, j))
                if step % 2 == 0:
                    total += 1

    return total


def aoc2023_day21_part2(puzzle_input):
    grid = [list(row) for row in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    assert m == n and grid[n//2][n//2] == 'S', "The grid needs to be square with S exactly in the middle"

    # After having crossed the border of the first grid, all further border crossings are seperated by n steps (length/width of grid)
    # Therefore, the total number of grids to traverse in any direction is 26_501_365 // n = x_final
    # Assumption: at step 26_501_365 another border crossing is taking place
    # If so, then it follows that the first crossing takes place at 26_501_365 % n = remainder
    x_final, remainder = divmod(26_501_365, n)
    border_crossings = [remainder, remainder + n, remainder + 2*n]

    visited = set()
    queue = deque([(n//2, n//2)])
    total = [0, 0]  # [even, odd]
    Y = []
    for step in range(1, border_crossings[-1]+1):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if (i, j) in visited or grid[i%m][j%n] == '#':
                    continue

                visited.add((i, j))
                queue.append((i, j))
                total[step % 2] += 1

        if step in border_crossings:
            Y.append(total[step % 2])

    X = [0, 1, 2]
    coefficients = np.polyfit(X, Y, deg=2)      # get coefficients for quadratic equation y = a*x^2 + bx + c
    y_final = np.polyval(coefficients, x_final) # using coefficients, get y value at x_final
    return y_final.round().astype(int)


####################################################################################################


def aoc2023_day22_part1(puzzle_input):
    regex = r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)'
    blocks = []
    for block in re.findall(regex, puzzle_input):
        x1, y1, z1, x2, y2, z2 = map(int, block)
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        z1, z2 = sorted((z1, z2))
        blocks.append((x1, y1, z1, x2, y2, z2))

    blocks.sort(key=lambda x: x[2]) # sort by z1: distance to ground
    X = max(b[3] for b in blocks) + 1
    Y = max(b[4] for b in blocks) + 1
    Z = max(b[5] for b in blocks) + 1
    
    stack = [[['empty' for _ in range(X)] for _ in range(Y)] for _ in range(Z)]
    supported_by = {}
    for block_id, (x1, y1, z1, x2, y2, z2) in enumerate(blocks):
        # Let block fall until it receives support
        for z in range(Z):
            support = set(stack[z][y][x] for x in range(x1, x2+1) for y in range(y1, y2+1)) - {'empty'}
            if support:
                supported_by[block_id] = support
                break
        # Add block above its support
        height = z2 - z1 + 1
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z_ in range(z-height, z):
                    stack[z_][y][x] = block_id

    # If a block only has a single supporting block, then this supporting block is indispensible
    indispensible = set.union(*[x for x in supported_by.values() if len(x)==1])
    return len(blocks) - len(indispensible)


def aoc2023_day22_part2(puzzle_input):
    regex = r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)'
    blocks = []
    for block in re.findall(regex, puzzle_input):
        x1, y1, z1, x2, y2, z2 = map(int, block)
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        z1, z2 = sorted((z1, z2))
        blocks.append((x1, y1, z1, x2, y2, z2))

    blocks.sort(key=lambda x: x[2]) # sort by z1: distance to ground
    X = max(b[3] for b in blocks) + 1
    Y = max(b[4] for b in blocks) + 1
    Z = max(b[5] for b in blocks) + 1
    N = len(blocks)

    stack = [[['empty' for _ in range(X)] for _ in range(Y)] for _ in range(Z)]
    supported_by = {}
    for block_id, (x1, y1, z1, x2, y2, z2) in enumerate(blocks): 
        # Let block fall until it receives support
        for z in range(Z):
            support = set(stack[z][y][x] for x in range(x1, x2+1) for y in range(y1, y2+1)) - {'empty'}
            if support:
                supported_by[block_id] = support
                break
        # Add block above its support
        height = z2 - z1 + 1
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z_ in range(z-height, z):
                    stack[z_][y][x] = block_id

    # Disintegrate indispensible blocks & examine the resulting chain reactions
    indispensible = set.union(*[x for x in supported_by.values() if len(x)==1])
    total = 0
    for i in indispensible:
        disintegrated = set([i])
        for j in range(i+1, N):
            if j in supported_by and supported_by[j].issubset(disintegrated):
                disintegrated.add(j)
        total += len(disintegrated) - 1

    return total


####################################################################################################


def aoc2023_day23_part1(puzzle_input):
    grid = [list(row) for row in puzzle_input.split('\n')]
    start = (1, 1)       # starting at second tile to prevent the search from going backwards and out of bounds
    target = (len(grid)-1, len(grid[0])-2)

    # create graph where the nodes are the intersections of the grid
    graph = defaultdict(list)
    queue = [(start, start, {start, (0, 1)}, 0)]
    while queue:
        curr_xy, prev_node, visited, slope = queue.pop()
        if curr_xy == target:
            graph[prev_node].append((curr_xy, len(visited)-1))
            continue

        (x, y) = curr_xy
        neighbors = []
        directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        upward_slopes = '^v<>'
        for (i, j), upward in zip(directions, upward_slopes):
            if (i, j) not in visited and (tile := grid[i][j]) != '#':
                tile_slope = 0 if tile == '.' else 1 if tile == upward else -1
                neighbors.append(((i, j), tile_slope))
        
        if len(neighbors) == 1:                                 # neither intersection nor dead end
            nxt_xy, tile_slope = neighbors.pop()
            if tile_slope:
                assert slope + tile_slope != 0, "assumed not to happen: an upward and a downward slope in a single path"
                slope = tile_slope
            queue.append((nxt_xy, prev_node, visited|{nxt_xy}, slope))

        elif len(neighbors) > 1:                                # found an intersection (= node)
            steps = len(visited) - 1
            if (curr_xy, steps) in graph[prev_node] or \
                  (prev_node, steps) in graph[curr_xy]:         # already been here
                continue
            if slope < 1:
                graph[prev_node].append((curr_xy, steps))
            if slope > -1:
                graph[curr_xy].append((prev_node, steps))    
            while neighbors:                                    # traverse paths from current node
                nxt_xy, tile_slope = neighbors.pop()
                queue.append((nxt_xy, curr_xy, {curr_xy, nxt_xy}, tile_slope))

    # traverse graph
    possible_paths = []
    queue = [(start, 0, {start})]
    while queue:
        curr, steps, visited = queue.pop()
        if curr == target:
            possible_paths.append(steps)
            continue
        for nxt, add_steps in graph[curr]:
            if nxt not in visited:
                queue.append((nxt, steps+add_steps, visited|{nxt}))

    return max(possible_paths)


def aoc2023_day23_part2(puzzle_input):
    grid = [list(row) for row in puzzle_input.split('\n')]
    start = (1, 1)       # starting at second tile to prevent the search from going backwards and out of bounds
    target = (len(grid)-1, len(grid[0])-2)

    # create graph where the nodes are the intersections of the grid
    graph = defaultdict(list)
    queue = [(start, start, {start, (0, 1)})] 
    while queue:
        curr_xy, prev_node, visited = queue.pop()
        if curr_xy == target:
            final_node = prev_node
            final_steps = len(visited)-1
            continue

        (x, y) = curr_xy
        neighbors = []
        for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if (i, j) not in visited and grid[i][j] != '#':
                neighbors.append((i, j))
        
        if len(neighbors) == 1:                                 # neither intersection nor dead end
            nxt_xy = neighbors.pop()
            queue.append((nxt_xy, prev_node, visited|{nxt_xy}))

        elif len(neighbors) > 1:                                # found an intersection ( node)
            steps = len(visited) - 1
            if (curr_xy, steps) in graph[prev_node]:            # already been here
                continue
            graph[prev_node].append((curr_xy, steps))
            graph[curr_xy].append((prev_node, steps))    
            while neighbors:                                    # start new paths from current node
                nxt_xy = neighbors.pop()
                queue.append((nxt_xy, curr_xy, {curr_xy, nxt_xy}))

    # traverse graph
    max_steps = 0
    queue = [(start, 0, {start})]
    while queue:
        curr, steps, visited = queue.pop()
        if curr == final_node:
            max_steps = max(steps, max_steps)
            continue
        for nxt, distance in graph[curr]:
            if nxt not in visited:
                queue.append((nxt, steps+distance, visited|{nxt}))

    return max_steps + final_steps


####################################################################################################


def aoc2023_day24_part1(puzzle_input):
    hailstones = []
    for line in puzzle_input.split('\n'):
        nums = line.replace('@', ',').split(',')
        hailstones.append(tuple(map(int, nums)))

    lo, hi = 2e14, 4e14
    total = 0
    for h1, h2 in combinations(hailstones, 2):
        x1, y1, _, dx1, dy1, _ = h1
        x2, y2, _, dx2, dy2, _ = h2
        m1 = dy1 / dx1
        m2 = dy2 / dx2
        if m1 == m2:   # they move in parallel and never meet
            continue
        b1 = y1 - m1*x1
        b2 = y2 - m2*x2
        x = (b2-b1) / (m1-m2)
        y = m1*x + b1
        if all((lo <= x <= hi,  # x and y need to be in range
                lo <= y <= hi,
                (x > x1 and dx1 > 0) or (x < x1 and dx1 < 0),  # itersection needs to happen in the future
                (x > x2 and dx2 > 0) or (x < x2 and dx2 < 0))):
            total += 1

    return total


def aoc2023_day24_part2(puzzle_input):
    first_three_hailstones = []
    for line in puzzle_input.split('\n')[:3]:
        nums = line.replace('@', ',').split(',')
        first_three_hailstones.append(tuple(map(int, nums)))

    unknowns = sp.symbols('x y z dx dy dz t1 t2 t3')
    x, y, z, dx, dy, dz, *time = unknowns

    equations = []  # build system of 9 equations with 9 unknowns
    for t, h in zip(time, first_three_hailstones):
        equations.append(sp.Eq(x + t*dx, h[0] + t*h[3]))
        equations.append(sp.Eq(y + t*dy, h[1] + t*h[4]))
        equations.append(sp.Eq(z + t*dz, h[2] + t*h[5]))

    solution = sp.solve(equations, unknowns).pop()
    return sum(solution[:3])


####################################################################################################


def aoc2023_day25_part1(puzzle_input):
    graph = nx.Graph()
    for line in puzzle_input.split('\n'):
        node1, connected = line.split(': ')
        for node2 in connected.split():
            graph.add_edge(node1, node2, capacity=1)

    for node1, node2 in combinations(graph.nodes, 2):
        cuts, partitions = nx.minimum_cut(graph, node1, node2)
        if cuts == 3:
            break

    return math.prod(partitions)