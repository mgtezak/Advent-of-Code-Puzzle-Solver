import re
import math
from functools import cmp_to_key, cache
from itertools import cycle, combinations
from collections import Counter, defaultdict
from heapq import heappop, heappush

import numpy as np


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
    pass


def aoc2023_day18_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day19_part1(puzzle_input):
    pass


def aoc2023_day19_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day20_part1(puzzle_input):
    pass


def aoc2023_day20_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day21_part1(puzzle_input):
    pass


def aoc2023_day21_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day22_part1(puzzle_input):
    pass


def aoc2023_day22_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day23_part1(puzzle_input):
    pass


def aoc2023_day23_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day24_part1(puzzle_input):
    pass


def aoc2023_day24_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day25_part1(puzzle_input):
    pass


def aoc2023_day25_part2(puzzle_input):
    pass