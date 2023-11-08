from operator import eq, ne, lt, le, gt, ge
from collections import Counter


def aoc2017_day1_part1(puzzle_input):
    nums = list(map(int, puzzle_input))
    return sum(int(val) for i, val in enumerate(nums) if val == nums[i-1])


def aoc2017_day1_part2(puzzle_input):
    nums = list(map(int, puzzle_input))
    half = int(len(nums) / 2)
    return sum(2 * int(a) for a, b in zip(nums[:half], nums[half:]) if a == b)


####################################################################################################


def aoc2017_day2_part1(puzzle_input):
    nums = [[int(num) for num in row.split()] for row in puzzle_input.split('\n')]
    return sum(max(row) - min(row) for row in nums)


def aoc2017_day2_part2(puzzle_input):
    nums = [[int(num) for num in row.split()] for row in puzzle_input.split('\n')]
    return int(sum(a / b for row in nums for a in row for b in row if a != b and not a % b))


####################################################################################################


def aoc2017_day3_part1(puzzle_input):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # east, north, west, south
    distance = int(puzzle_input) - 1        # since we start at 1, we subtract 1 from the destination value
    x = y = facing = 0          # start at coords (0, 0), facing east, 
    steps = 1                   # distance between current and next corner
    while distance:
        steps = min(steps, distance)
        i, j = directions[facing]    
        x += i * steps
        y += j * steps
        distance -= steps
        facing = (facing + 1) % 4   # turn left by 90 degrees
        if not facing % 2:          # if now facing east or west, increase number of steps to reach next corner
            steps += 1
    return abs(x) + abs(y)


def aoc2017_day3_part2(puzzle_input):
    puzzle_input = int(puzzle_input)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # east, north, west, south
    def get_neighbors(x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                yield x+i, y+j

    x = y = facing = 0      # start at coords (0, 0), facing east, 
    steps = steps_left = 1  # distance between corners. distance from current position to next corner.
    squares = {(0, 0): 1}
    square_val = 1
    while square_val <= puzzle_input:
        i, j = directions[facing]    
        x += i
        y += j
        steps_left -= 1
        if not steps_left:
            facing = (facing + 1) % 4   # turn left by 90 degrees
            if not facing % 2:          # if now facing east or west, increase number of steps to reach next corner
                steps += 1
            steps_left = steps
        square_val = sum(squares.get((i, j), 0) for i, j in get_neighbors(x, y))
        squares[(x, y)] = square_val
    return square_val


####################################################################################################


def aoc2017_day4_part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    return sum(len(set(line)) == len(line) for line in lines)


def aoc2017_day4_part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    lines = [[''.join(sorted(word)) for word in line] for line in lines]
    return sum(len(set(line)) == len(line) for line in lines)


####################################################################################################


def aoc2017_day5_part1(puzzle_input):
    lines = [int(line) for line in puzzle_input.split('\n')]
    pos = 0
    steps = 0
    while pos in range(0, len(lines)):
        steps += 1
        move = lines[pos]
        lines[pos] += 1
        pos += move
    return steps


# VERY SLOW:
def aoc2017_day5_part2(puzzle_input):
    lines = [int(line) for line in puzzle_input.split('\n')]
    pos = 0
    steps = 0
    while pos in range(0, len(lines)):
        steps += 1
        move = lines[pos]
        lines[pos] += 1 if lines[pos] < 3 else -1 
        pos += move
    return steps


####################################################################################################


def aoc2017_day6_part1(puzzle_input):
    blocks = [int(x) for x in puzzle_input.split()]
    visited = dict()
    cycles = 0
    loop_detected = False

    while not loop_detected:
        visited[tuple(blocks)] = cycles
        cycles += 1

        qty = max(blocks)
        pos = blocks.index(qty)
        blocks[pos] -= qty
        for i in range(qty):
            blocks[(pos + 1 + i) % 16] += 1

        if tuple(blocks) in visited:
            return cycles


def aoc2017_day6_part2(puzzle_input):
    blocks = [int(x) for x in puzzle_input.split()]
    visited = dict()
    cycles = 0
    loop_detected = False

    while not loop_detected:
        visited[tuple(blocks)] = cycles
        cycles += 1

        qty = max(blocks)
        pos = blocks.index(qty)
        blocks[pos] -= qty
        for i in range(qty):
            blocks[(pos + 1 + i) % 16] += 1

        if tuple(blocks) in visited:
            loop_detected = cycles

    return loop_detected - visited[tuple(blocks)]


####################################################################################################


def aoc2017_day7_part1(puzzle_input):
    nodes = dict()
    for line in puzzle_input.split('\n'):
        line = [s.strip(',()') for s in line.split()]
        node, weight = line[0], int(line[1])
        branches = [] if len(line) == 2 else line[3:]
        nodes[node] = (weight, branches)

    return (set(nodes) - set(n for k in nodes for n in nodes[k][1])).pop()


def aoc2017_day7_part2(puzzle_input):
    nodes = dict()
    for line in puzzle_input.split('\n'):
        line = [s.strip(',()') for s in line.split()]
        node, weight = line[0], int(line[1])
        branches = [] if len(line) == 2 else line[3:]
        nodes[node] = (weight, branches)

    node = (set(nodes) - set(n for k in nodes for n in nodes[k][1])).pop()

    def calc_weight(node): # node's own weight plus weight of branches
        return nodes[node][0] + sum(calc_weight(n) for n in nodes[node][1])

    def is_balanced(node): # True if each branch has the same weight
        return True if len(set(calc_weight(n) for n in nodes[node][1])) == 1 else False

    def calc_avg_weight(node): # average weight of a branch
        return sum(calc_weight(n) for n in nodes[node][1]) / len(nodes[node][1])

    while not is_balanced(node):
        sorted_branches = sorted(nodes[node][1], key=lambda x: -abs(calc_weight(x) - calc_avg_weight(node))) # puts the outlier in front of the list
        outlier = sorted_branches[0]
        node = outlier

    deviation = calc_weight(outlier) - calc_weight(sorted_branches[1])
    return nodes[outlier][0] - deviation


####################################################################################################


def aoc2017_day8_part1(puzzle_input):

    lines = [line.split() for line in puzzle_input.split('\n')]

    ops = {
        '==': eq,
        '!=': ne,
        '<':  lt,
        '<=': le,
        '>':  gt,
        '>=': ge
    }

    def check(condition):
        key, comp, amt = condition
        first, compare, second = d[key], ops[comp], int(amt)
        return compare(first, second)

    def perform(operation):
        key, sig, amt = operation
        d[key] += int(amt) if sig == 'inc' else -int(amt)

    d = dict()
    for line in lines:
        r1, r2, operation, condition = line[0], line[4], line[:3], line[4:]
        for r in (r1, r2):
            if r not in d:
                d[r] = 0
        if check(condition):
            perform(operation)

    return max(d.values())


def aoc2017_day8_part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]

    ops = {
        '==': eq,
        '!=': ne,
        '<':  lt,
        '<=': le,
        '>':  gt,
        '>=': ge
    }

    def check(condition):
        key, comp, amt = condition
        first, compare, second = d[key], ops[comp], int(amt)
        return compare(first, second)

    def perform(operation):
        key, sig, amt = operation
        d[key] += int(amt) if sig == 'inc' else -int(amt)

    d = dict()
    max_value = 0
    for line in lines:
        r1, r2, operation, condition = line[0], line[4], line[:3], line[4:]
        for r in (r1, r2):
            if r not in d:
                d[r] = 0
        if check(condition):
            perform(operation)
        if d[r1] > max_value:
            max_value = d[r1]

    return max_value


####################################################################################################


def aoc2017_day9_part1(puzzle_input):
    score = 0
    level = 0
    garbage = False
    ignore_next = False
    for c in puzzle_input:
        if garbage:
            if ignore_next:
                ignore_next = False
            elif c == '!':
                ignore_next = True
            elif c == '>':
                garbage = False
        elif c == '{':
            level += 1
        elif c == '}':
            score += level
            level -= 1
        elif c == '<':
            garbage = True
    return score


def aoc2017_day9_part2(puzzle_input):
    score = 0
    level = 0
    garbage = False
    ignore_next = False
    garbage_chars = 0   # part 2
    for c in puzzle_input:
        if garbage:
            if ignore_next:
                ignore_next = False
            elif c == '!':
                ignore_next = True
            elif c == '>':
                garbage = False
            else:
                garbage_chars += 1   # part 2
        elif c == '{':
            level += 1
        elif c == '}':
            score += level
            level -= 1
        elif c == '<':
            garbage = True
    return garbage_chars


####################################################################################################


def aoc2017_day10_part1(puzzle_input):
    lengths = list(map(int, puzzle_input.split(',')))
    circle = [n for n in range(256)]
    pos = 0
    skip_size = 0
    for l in lengths:
        substring = [circle[i % 256] for i in range(pos, pos + l)]
        while substring:
            circle[pos] = substring.pop()
            pos = (pos + 1) % 256
        pos = (pos + skip_size) % 256
        skip_size += 1
        
    return circle[0] * circle[1]


def aoc2017_day10_part2(puzzle_input):
    ascii_codes = [ord(char) for char in puzzle_input]
    suffix = [17, 31, 73, 47, 23]
    lengths = ascii_codes + suffix
    circle = [n for n in range(256)]
    pos = 0
    skip_size = 0
    for _ in range(64):
        for l in lengths:
            substring = [circle[i % 256] for i in range(pos, pos + l)]
            while substring:
                circle[pos] = substring.pop()
                pos = (pos + 1) % 256
            pos = (pos + skip_size) % 256
            skip_size += 1
    knot_hash = ''
    for i in range(16):
        block_val = 0 
        for n in circle[(i * 16): i * 16 + 16]:
            block_val ^= n
        knot_hash += hex(block_val)[2:].zfill(2)
    return knot_hash


####################################################################################################


def aoc2017_day11_part1(puzzle_input):
    count = Counter(puzzle_input.split(','))
    x = count['s']  + count['se'] - count['n']  - count['nw']
    y = count['ne'] + count['se'] - count['sw'] - count['nw']
    if x * y <= 0:      # different signs: cannot move diagonally
        return abs(x) + abs(y)
    return min(abs(x), abs(y)) + abs(x-y)


def aoc2017_day11_part2(puzzle_input):

    def get_distance(x, y):
        if x * y <= 0:
            return abs(x) + abs(y)
        return min(abs(x), abs(y)) + abs(x-y)
        
    x = y = max_distance = 0
    for step in puzzle_input.split(','):
        if step in ('n', 'nw'):
            x -= 1
        elif step in ('s', 'se'):
            x += 1
        if step in ('sw', 'nw'):
            y -= 1
        elif step in ('ne', 'se'):
            y += 1
        max_distance = max(get_distance(x, y), max_distance)
    
    return max_distance


####################################################################################################


def aoc2017_day12_part1(puzzle_input):
    graph = {}
    for line in puzzle_input.split('\n'):
        node, paths = line.split(' <-> ')
        graph[int(node)] = [int(p) for p in paths.split(', ')]

    count = 0
    queue = set([0])
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)
        queue |= set(n for n in graph[node]) - queue - visited
        count += 1

    return count


def aoc2017_day12_part2(puzzle_input):
    graph = {}
    for line in puzzle_input.split('\n'):
        node, paths = line.split(' <-> ')
        graph[int(node)] = [int(p) for p in paths.split(', ')]

    count = 0
    visited = set()
    for node, paths in graph.items():
        if node in visited:
            continue
        count += 1
        queue = set([node])
        while queue:
            node = queue.pop()
            visited.add(node)
            queue |= set(n for n in graph[node]) - queue - visited
    return count 


####################################################################################################


def aoc2017_day13_part1(puzzle_input):
    layers = [(int(l), int(r)) for l, r in re.findall('(\d+): (\d+)', puzzle_input)]
    
    total = 0
    for l, r in layers:
        if l % ((r - 1) * 2) == 0:
            total += l * r

    return total


def aoc2017_day13_part2(puzzle_input):
    layers = [(int(l), int(r)) for l, r in re.findall('(\d+): (\d+)', puzzle_input)]
    
    delay = 0
    while True:
        for l, r in layers:
            if (l + delay) % ((r - 1) * 2) == 0:
                delay += 1
                break
        else:
            break

    return delay


####################################################################################################


def aoc2017_day14_part1(puzzle_input):
    pass


def aoc2017_day14_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day15_part1(puzzle_input):
    pass


def aoc2017_day15_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day16_part1(puzzle_input):
    pass


def aoc2017_day16_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day17_part1(puzzle_input):
    pass


def aoc2017_day17_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day18_part1(puzzle_input):
    pass


def aoc2017_day18_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day19_part1(puzzle_input):
    pass


def aoc2017_day19_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day20_part1(puzzle_input):
    pass


def aoc2017_day20_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day21_part1(puzzle_input):
    pass


def aoc2017_day21_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day22_part1(puzzle_input):
    pass


def aoc2017_day22_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day23_part1(puzzle_input):
    pass


def aoc2017_day23_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day24_part1(puzzle_input):
    pass


def aoc2017_day24_part2(puzzle_input):
    pass


####################################################################################################


def aoc2017_day25_part1(puzzle_input):
    pass


def aoc2017_day25_part2(puzzle_input):
    pass



