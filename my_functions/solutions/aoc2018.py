from datetime import datetime
from collections import Counter, deque, defaultdict
from string import ascii_letters, ascii_uppercase
import re




def aoc2018_day1_part1(puzzle_input):
    return sum(int(line) for line in puzzle_input.split('\n'))


def aoc2018_day1_part2(puzzle_input):
    nums = [int(line) for line in puzzle_input.split('\n')]
    past_frequencies = {0}
    current_freq = 0
    while True:
        for n in nums:
            current_freq += n
            if current_freq in past_frequencies:
                return current_freq
            past_frequencies.add(current_freq)


####################################################################################################


def aoc2018_day2_part1(puzzle_input):
    box_IDs = [line for line in puzzle_input.split('\n')]
    double = triple = 0
    for b in box_IDs:
        double += 1 if any(b.count(letter) == 2 for letter in b) else 0
        triple += 1 if any(b.count(letter) == 3 for letter in b) else 0
    return double * triple


def aoc2018_day2_part2(puzzle_input):
    box_IDs = [line for line in puzzle_input.split('\n')]
    differ_by_1 = None
    for i, b in enumerate(box_IDs):        
        if not differ_by_1:
            for other_b in box_IDs[i+1:]:
                differ = sum(1 if b[i] != other_b[i] else 0 for i in range(len(b)))
                if differ == 1:
                    differ_by_1 = {b, other_b}

    a, b = differ_by_1
    return ''.join(letter for i, letter in enumerate(a) if letter == b[i])


####################################################################################################


def aoc2018_day3_part1(puzzle_input):
    claims = [line.split() for line in puzzle_input.split('\n')]
    claimed = dict()
    for c in claims:
        claim_id = int(c[0].strip('#'))
        left, up = [int(n.strip(':')) for n in c[2].split(',')]
        width, height = [int(n) for n in c[3].split('x')]
        for x in range(left, left + width):
            for y in range(up, up + height):
                if claimed.get((x, y)):
                    claimed[(x, y)].append(claim_id)
                else:
                    claimed[(x, y)] = [claim_id]

    return len([ids for ids in claimed.values() if len(ids) > 1])


def aoc2018_day3_part2(puzzle_input):
    claims = [line.split() for line in puzzle_input.split('\n')]
    claimed = dict()
    for c in claims:
        claim_id = int(c[0].strip('#'))
        left, up = [int(n.strip(':')) for n in c[2].split(',')]
        width, height = [int(n) for n in c[3].split('x')]
        for x in range(left, left + width):
            for y in range(up, up + height):
                if claimed.get((x, y)):
                    claimed[(x, y)].append(claim_id)
                else:
                    claimed[(x, y)] = [claim_id]

    claimed_twice = [ids for ids in claimed.values() if len(ids) > 1]
    all_claim_ids = {n+1 for n in range(len(claims))}
    return all_claim_ids.difference({i for ids in claimed_twice for i in ids}).pop()


####################################################################################################


def aoc2018_day4_part1(puzzle_input):
    data = [line.split() for line in puzzle_input.split('\n')]
    timeline = []
    for line in data:
        date_str = ''.join(line[0] + line[1]).strip('[]') 
        date = datetime.strptime(date_str, '%Y-%m-%d%H:%M')
        timeline.append((date, line[2:]))
    timeline.sort()    
    sleep_record = {}
    guard = None
    asleep = False
    for i, event in enumerate(timeline):
        if event[1][0] == 'Guard':
            guard = int(event[1][1].strip('#'))
            if guard not in sleep_record:
                sleep_record[guard] = []
        elif event[1][0] == 'wakes':
            mins = [m for m in range(asleep, event[0].minute)]
            sleep_record[guard] += mins
            asleep = False
        else:
            asleep = event[0].minute
        
    elf_1 = max(sleep_record, key=lambda x: len(sleep_record.get(x)))
    min_counter = Counter(sleep_record[elf_1])
    minute_1 = max(min_counter, key=min_counter.get)
    return elf_1 * minute_1


def aoc2018_day4_part2(puzzle_input):
    data = [line.split() for line in puzzle_input.split('\n')]

    timeline = []
    for line in data:
        date_str = ''.join(line[0] + line[1]).strip('[]') 
        date = datetime.strptime(date_str, '%Y-%m-%d%H:%M')
        timeline.append((date, line[2:]))
    timeline.sort()    

    sleep_record = {}
    guard = None
    asleep = False
    for i, event in enumerate(timeline):
        if event[1][0] == 'Guard':
            guard = int(event[1][1].strip('#'))
            if guard not in sleep_record:
                sleep_record[guard] = []
        elif event[1][0] == 'wakes':
            mins = [m for m in range(asleep, event[0].minute)]
            sleep_record[guard] += mins
            asleep = False
        else:
            asleep = event[0].minute
        
    elf_1 = max(sleep_record, key=lambda x: len(sleep_record.get(x)))
    min_counter = Counter(sleep_record[elf_1])
    minute_1 = max(min_counter, key=min_counter.get)

    elf_2 = minute_2 = max_count = 0
    for elf in sleep_record:
        if sleep_record[elf] == []:
            continue
        min_counter = Counter(sleep_record[elf])
        if max(min_counter.values()) > max_count:
            max_count = max(min_counter.values())
            minute_2 = max(min_counter, key=min_counter.get)
            elf_2 = elf
    return elf_2 * minute_2


####################################################################################################


def aoc2018_day5_part1(puzzle_input):
    remaining = []
    for char in puzzle_input:
        if remaining and abs(ord(char) - ord(remaining[-1])) == 32:
            remaining.pop()
        else :
            remaining.append(char)
    return len(remaining)


def aoc2018_day5_part2(puzzle_input):

    def calc_remaining_len(del_letters: tuple=()) -> int:
        remaining = []
        for char in puzzle_input:
            if remaining and abs(ord(char) - ord(remaining[-1])) == 32:
                remaining.pop()
            elif char not in del_letters:
                remaining.append(char)
        return len(remaining)

    alphabet = ascii_letters
    return min(calc_remaining_len((alphabet[i], alphabet[i+26])) for i in range(26))


####################################################################################################


def aoc2018_day6_part1(puzzle_input):
    coords = [tuple(map(int, line.split(', '))) for line in puzzle_input.split('\n')]
    areas = {(x, y): 0 for x, y in coords}
    
    x_vals = sorted(x for x, _ in coords)
    y_vals = sorted(y for _, y in coords)
    x_min, x_max = x_vals[0], x_vals[-1]
    y_min, y_max = y_vals[0], y_vals[-1]

    def get_nearest_coord(x, y):
        distances = {(v, w): abs(x-v) + abs(y-w) for v, w in coords}
        sorted_distances = sorted(distances.items(), key=lambda x: x[1])
        if sorted_distances[0][1] == sorted_distances[1][1]:
            return None
        return sorted_distances[0][0]

    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            nearest = get_nearest_coord(x, y)
            if nearest in areas:
                if x in (x_min, x_max) or y in (y_min, y_max):
                    del areas[nearest]
                else:
                    areas[nearest] += 1

    return max(areas.values())


def aoc2018_day6_part2(puzzle_input):
    coords = [tuple(map(int, line.split(', '))) for line in puzzle_input.split('\n')]
    areas = {(x, y): 0 for x, y in coords}
    proximity_region = []

    x_vals = sorted(x for x, _ in coords)
    y_vals = sorted(y for _, y in coords)
    x_min, x_max = x_vals[0], x_vals[-1]
    y_min, y_max = y_vals[0], y_vals[-1]

    def get_nearest_coord(x, y):
        distances = {(v, w): abs(x-v) + abs(y-w) for v, w in coords}
        sorted_distances = sorted(distances.items(), key=lambda x: x[1])
        if sum(distances.values()) < 10_000:
            proximity_region.append(1)
        if sorted_distances[0][1] == sorted_distances[1][1]:
            return None
        return sorted_distances[0][0]

    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            nearest = get_nearest_coord(x, y)
            if nearest in areas:
                if x in (x_min, x_max) or y in (y_min, y_max):
                    del areas[nearest]
                else:
                    areas[nearest] += 1

    return sum(proximity_region)


####################################################################################################


def aoc2018_day7_part1(puzzle_input):
    instructions = [line.split() for line in puzzle_input.split('\n')]
    requirements = {}
    all_steps = set()

    for i in instructions:
        earlier, later = i[1], i[7]
        all_steps |= {earlier, later}
        if requirements.get(later):
            requirements[later].append(earlier)
        else:
            requirements[later] = [earlier]

    possible_steps = [s for s in all_steps if s not in requirements]
    order_of_steps = ''
    while possible_steps:
        possible_steps = sorted(possible_steps, reverse=True)
        cur_step = possible_steps.pop()
        order_of_steps += cur_step
        for step in requirements:
            if cur_step in requirements[step]:
                requirements[step].remove(cur_step)
                if not requirements[step]:
                    possible_steps.append(step)

    return order_of_steps


def aoc2018_day7_part2(puzzle_input):

    instructions = [line.split() for line in puzzle_input.split('\n')]
    requirements = {}
    all_steps = set()

    for i in instructions:
        earlier, later = i[1], i[7]
        all_steps |= {earlier, later}
        if requirements.get(later):
            requirements[later].append(earlier)
        else:
            requirements[later] = [earlier]

    possible_steps = [s for s in all_steps if s not in requirements]
    time_required = {s: 61 + ascii_uppercase.index(s) for s in all_steps}
    time_elapsed = 0
    idle = 5
    in_progress = {}

    while True:
        possible_steps = sorted(possible_steps, reverse=True)
        for w in range(idle):
            if possible_steps:
                next_step = possible_steps.pop()
                in_progress[next_step] = time_required[next_step]
                idle -= 1

        in_progress = {step: time for step, time in in_progress.items() if time}
        if not in_progress:
            break

        time_elapsed += 1
        for cur_step in in_progress:
            in_progress[cur_step] -= 1
            if not in_progress[cur_step]:
                idle += 1
                for step in requirements:
                    if cur_step in requirements[step]:
                        requirements[step].remove(cur_step)
                        if not requirements[step]:
                            possible_steps.append(step)

    return time_elapsed


####################################################################################################


def aoc2018_day8_part1(puzzle_input):
    nums = list(map(int, puzzle_input.split()))

    def parse(nums):
        n_children, n_metadata = nums[:2]
        nums = nums[2:]
        total = 0
        if n_children:
            vals = []
            for _ in range(n_children):
                t, v, nums = parse(nums)
                total += t
                vals.append(v)
            val = sum(vals[i-1] for i in nums[:n_metadata] if i-1 in range(len(vals)))
        else:
            val = sum(nums[:n_metadata])
        total += sum(nums[:n_metadata])
        return total, val, nums[n_metadata:]

    return parse(nums)[0]


def aoc2018_day8_part2(puzzle_input):
    nums = list(map(int, puzzle_input.split()))

    def parse(nums):
        n_children, n_metadata = nums[:2]
        nums = nums[2:]
        total = 0
        if n_children:
            vals = []
            for _ in range(n_children):
                t, v, nums = parse(nums)
                total += t
                vals.append(v)
            val = sum(vals[i-1] for i in nums[:n_metadata] if i-1 in range(len(vals)))
        else:
            val = sum(nums[:n_metadata])
        total += sum(nums[:n_metadata])
        return total, val, nums[n_metadata:]

    return parse(nums)[1]


####################################################################################################


def aoc2018_day9_part1(puzzle_input):
    regex = r"(\d+) players; last marble is worth (\d+) points"
    n_players, last_marble = [int(n) for n in re.findall(regex, puzzle_input)[0]]
    circle = deque([0])
    scores = defaultdict(int)

    for n in range(1, last_marble + 1):
        if not n % 23:
            circle.rotate(7)
            scores[n % n_players] += n + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(n)

    return max(scores.values())


def aoc2018_day9_part2(puzzle_input):
    regex = r"(\d+) players; last marble is worth (\d+) points"
    n_players, last_marble = [int(n) for n in re.findall(regex, puzzle_input)[0]]
    last_marble *= 100
    circle = deque([0])
    scores = defaultdict(int)

    for n in range(1, last_marble + 1):
        if not n % 23:
            circle.rotate(7)
            scores[n % n_players] += n + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(n)

    return max(scores.values())


####################################################################################################


def aoc2018_day10_part1(puzzle_input):
    regex = r'position=<\s*(-?\d+),\s+(-?\d+)> velocity=<\s*(-?\d+),\s+(-?\d+)>'
    points = [tuple(map(int, line)) for line in re.findall(regex, puzzle_input)]
    while True:
        new_points = [(x+i, y+j, i, j) for x, y, i, j in points]
        if min(new_points) < min(points):
            break
        points = new_points
    x_coords = [p[0] for p in points]
    x_min = min(x_coords)
    x_span = abs(max(x_coords) - x_min)
    y_coords = [p[1] for p in points]
    y_min = min(y_coords)
    y_span = abs(max(y_coords) - y_min)
    grid = [[' ' for _ in range(x_span+1)] for _ in range(y_span+1)]
    for x, y, *_ in points:
        grid[y-y_min][x-x_min] = '#'
    return '\n'.join(''.join(row) for row in grid)


def aoc2018_day10_part2(puzzle_input):
    regex = r'position=<\s*(-?\d+),\s+(-?\d+)> velocity=<\s*(-?\d+),\s+(-?\d+)>'
    points = [tuple(map(int, line)) for line in re.findall(regex, puzzle_input)]
    seconds = 0
    while True:
        new_points = [(x+i, y+j, i, j) for x, y, i, j in points]
        if min(new_points) < min(points):
            break
        points = new_points
        seconds += 1
    x_coords = [p[0] for p in points]
    x_min = min(x_coords)
    x_span = abs(max(x_coords) - x_min)
    y_coords = [p[1] for p in points]
    y_min = min(y_coords)
    y_span = abs(max(y_coords) - y_min)
    grid = [[' ' for _ in range(x_span+1)] for _ in range(y_span+1)]
    for x, y, *_ in points:
        grid[y-y_min][x-x_min] = '#'
    return seconds


####################################################################################################


def aoc2018_day11_part1(puzzle_input):
    pass


def aoc2018_day11_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day12_part1(puzzle_input):
    pass


def aoc2018_day12_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day13_part1(puzzle_input):
    pass


def aoc2018_day13_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day14_part1(puzzle_input):
    pass


def aoc2018_day14_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day15_part1(puzzle_input):
    pass


def aoc2018_day15_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day16_part1(puzzle_input):
    pass


def aoc2018_day16_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day17_part1(puzzle_input):
    pass


def aoc2018_day17_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day18_part1(puzzle_input):
    pass


def aoc2018_day18_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day19_part1(puzzle_input):
    pass


def aoc2018_day19_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day20_part1(puzzle_input):
    pass


def aoc2018_day20_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day21_part1(puzzle_input):
    pass


def aoc2018_day21_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day22_part1(puzzle_input):
    pass


def aoc2018_day22_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day23_part1(puzzle_input):
    pass


def aoc2018_day23_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day24_part1(puzzle_input):
    pass


def aoc2018_day24_part2(puzzle_input):
    pass


####################################################################################################


def aoc2018_day25_part1(puzzle_input):
    pass


def aoc2018_day25_part2(puzzle_input):
    pass



