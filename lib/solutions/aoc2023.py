import re
import math
from functools import cmp_to_key
from itertools import cycle
from collections import Counter


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
    pass


def aoc2023_day9_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day10_part1(puzzle_input):
    pass


def aoc2023_day10_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day11_part1(puzzle_input):
    pass


def aoc2023_day11_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day12_part1(puzzle_input):
    pass


def aoc2023_day12_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day13_part1(puzzle_input):
    pass


def aoc2023_day13_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day14_part1(puzzle_input):
    pass


def aoc2023_day14_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day15_part1(puzzle_input):
    pass


def aoc2023_day15_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day16_part1(puzzle_input):
    pass


def aoc2023_day16_part2(puzzle_input):
    pass


####################################################################################################


def aoc2023_day17_part1(puzzle_input):
    pass


def aoc2023_day17_part2(puzzle_input):
    pass


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