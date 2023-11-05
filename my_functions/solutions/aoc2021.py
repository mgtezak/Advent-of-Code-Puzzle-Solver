import re
import math
from collections import defaultdict, Counter


def aoc2021_day1_part1(puzzle_input):
    measurements = list(map(int, puzzle_input.split('\n')))
    count = 0
    for i, m in enumerate(measurements):
        if i == 0:
            continue
        if m > measurements[i-1]:
            count += 1
    return count


def aoc2021_day1_part2(puzzle_input):
    measurements = list(map(int, puzzle_input.split('\n')))
    windows = [sum(measurements[j] for j in (i-2, i-1, i)) for i in range(2, len(measurements))]
    count = 0
    for i, m in enumerate(windows):
        if i == 0:
            continue
        if m > windows[i-1]:
            count += 1
    return count


########################################################################################


def aoc2021_day2_part1(puzzle_input):
    movements = [(m.split()[0], int(m.split()[1])) for m in puzzle_input.split('\n')]
    x = y = 0
    for c, n in movements:
        if c == 'forward':
            x += n
        elif c == 'up':
            y -= n
        elif c == 'down':
            y += n
    return x * y


def aoc2021_day2_part2(puzzle_input):
    movements = [(m.split()[0], int(m.split()[1])) for m in puzzle_input.split('\n')]
    x = y = aim = 0
    for c, n in movements:
        if c == 'forward':
            x += n
            y += aim * n
        elif c == 'up':
            aim -= n
        elif c == 'down':
            aim += n
    return x * y


########################################################################################


def aoc2021_day3_part1(puzzle_input):
    nums = puzzle_input.split('\n')
    gamma = ''
    for i in range(12):
        if sum(int(nums[j][i]) for j in range(len(nums))) < len(nums)/2:
            gamma += '0'
        else:
            gamma += '1'
    epsilon = ''.join(str(1-int(x)) for x in gamma)
    return int(gamma, 2) * int(epsilon, 2)


def aoc2021_day3_part2(puzzle_input):

    nums = puzzle_input.split('\n')

    nums_ = nums.copy()
    for i in range(12):
        vals = [n[i] for n in nums_]
        if vals.count('0') > len(vals)/2:
            val = '0'
        else:
            val = '1'
        nums_ = [n for n in nums_ if n[i] == val]
        if len(nums_) == 1:
            oxygen_generator = nums_.pop()
            break

    for i in range(12):
        vals = [n[i] for n in nums]
        if vals.count('0') > len(vals)/2:
            val = '1'
        else:
            val = '0'
        nums = [n for n in nums if n[i] == val]
        if len(nums) == 1:
            co2_scrubber = nums.pop()
            break

    return int(oxygen_generator, 2) * int(co2_scrubber, 2)


########################################################################################


def aoc2021_day4_part1(puzzle_input):
    input = puzzle_input.split('\n\n')
    nums = [int(n) for n in input[0].split(',')]
    boards = [[[int(n) for n in row.split()] for row in board.split('\n')] for board in input[1:]]

    marked_rows = {b: {r: 0 for r in range(5)} for b in range(len(boards))}
    marked_cols = {b: {c: 0 for c in range(5)} for b in range(len(boards))}
    marked_cords = {b: set() for b in range(len(boards))}

    def get_score(i, num):
        score = 0
        for r, row in enumerate(boards[i]):
            for c, n in enumerate(row):
                if (r, c) not in marked_cords[i]:
                    score += n
        return score * num

    unfinished = [b for b in range(len(boards))]
    while unfinished:
        num = nums.pop(0)
        for i, board in enumerate(boards):
            if i in unfinished:
                for r, row in enumerate(boards[i]):
                    for c, n in enumerate(row):
                        if n == num:
                            marked_rows[i][r] += 1
                            marked_cols[i][c] += 1
                            marked_cords[i].add((r, c))
                            if marked_rows[i][r] == 5 or marked_cols[i][c] == 5:
                                unfinished.remove(i)
                                if len(unfinished) == len(boards) - 1:
                                    winner = get_score(i, num)
                                elif not unfinished:
                                    loser = get_score(i, num)
    return winner


def aoc2021_day4_part2(puzzle_input):
    input = puzzle_input.split('\n\n')
    nums = [int(n) for n in input[0].split(',')]
    boards = [[[int(n) for n in row.split()] for row in board.split('\n')] for board in input[1:]]

    marked_rows = {b: {r: 0 for r in range(5)} for b in range(len(boards))}
    marked_cols = {b: {c: 0 for c in range(5)} for b in range(len(boards))}
    marked_cords = {b: set() for b in range(len(boards))}

    def get_score(i, num):
        score = 0
        for r, row in enumerate(boards[i]):
            for c, n in enumerate(row):
                if (r, c) not in marked_cords[i]:
                    score += n
        return score * num

    unfinished = [b for b in range(len(boards))]
    while unfinished:
        num = nums.pop(0)
        for i, board in enumerate(boards):
            if i in unfinished:
                for r, row in enumerate(boards[i]):
                    for c, n in enumerate(row):
                        if n == num:
                            marked_rows[i][r] += 1
                            marked_cols[i][c] += 1
                            marked_cords[i].add((r, c))
                            if marked_rows[i][r] == 5 or marked_cols[i][c] == 5:
                                unfinished.remove(i)
                                if len(unfinished) == len(boards) - 1:
                                    winner = get_score(i, num)
                                elif not unfinished:
                                    loser = get_score(i, num)
    return loser


########################################################################################


def aoc2021_day5_part1(puzzle_input):
    regex = r'(\d+),(\d+) -> (\d+),(\d+)'
    lines = [tuple(map(int, coords)) for coords in re.findall(regex, puzzle_input)]
    horizontal = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if x1 == x2 or y1 == y2]
    covered = dict()
    for x1, y1, x2, y2 in horizontal:
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                if not covered.get((x, y)):
                    covered[(x, y)] = 0
                covered[(x, y)] += 1
    return len([(x, y) for x, y in covered if covered[(x, y)] > 1])


def aoc2021_day5_part2(puzzle_input):
    regex = r'(\d+),(\d+) -> (\d+),(\d+)'
    lines = [tuple(map(int, coords)) for coords in re.findall(regex, puzzle_input)]
    horizontal = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if x1 == x2 or y1 == y2]
    diagonal = [line for line in lines if line not in horizontal]
    covered = dict()
    for x1, y1, x2, y2 in horizontal:
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                if not covered.get((x, y)):
                    covered[(x, y)] = 0
                covered[(x, y)] += 1

    for x1, y1, x2, y2 in diagonal:
        if (x1 > x2) == (y1 > y2):
            y = min(y1, y2)
            incr = 1
        else:
            y = max(y1, y2)
            incr = -1
        for x in range(min(x1, x2), max(x1, x2)+1):
            if not covered.get((x, y)):
                covered[(x, y)] = 0
            covered[(x, y)] += 1
            y += incr

    return len([(x, y) for x, y in covered if covered[(x, y)] > 1])


########################################################################################


def aoc2021_day6_part1(puzzle_input):
    fish = list(map(int, puzzle_input.split(',')))
    fish_dict = {i: 0 for i in range(9)}
    for f in fish:
        fish_dict[f] += 1
    for _ in range(80):
        new_fish_dict = {i: 0 for i in range(9)}
        for f, count in fish_dict.items():
            if f == 0:
                new_fish_dict[6] += count
                new_fish_dict[8] += count
            else:
                new_fish_dict[f-1] += count
        fish_dict = new_fish_dict
    return sum(fish_dict.values())


def aoc2021_day6_part2(puzzle_input):
    fish = list(map(int, puzzle_input.split(',')))
    fish_dict = {i: 0 for i in range(9)}
    for f in fish:
        fish_dict[f] += 1
    for _ in range(256):
        new_fish_dict = {i: 0 for i in range(9)}
        for f, count in fish_dict.items():
            if f == 0:
                new_fish_dict[6] += count
                new_fish_dict[8] += count
            else:
                new_fish_dict[f-1] += count
        fish_dict = new_fish_dict
    return sum(fish_dict.values())


########################################################################################

# part 1 and two switched
def aoc2021_day7_part1(puzzle_input):

    def calc_fuel(pos):
        fuel = 0
        for c in crabs:
            dist = abs(pos - c)
            fuel += dist    
        return fuel
    
    crabs = list(map(int, puzzle_input.split(',')))
    i = 0
    results = []
    while True:
        fuel = calc_fuel(i)
        if results and fuel > results[-1]:
            break
        results.append(fuel)
        i += 1
    return int(results.pop())
    

def aoc2021_day7_part2(puzzle_input):

    def calc_fuel(pos):
        fuel = 0
        for c in crabs:
            dist = abs(pos - c)
            fuel += dist * (dist+1) / 2 
        return fuel
    
    crabs = list(map(int, puzzle_input.split(',')))
    i = 0
    results = []
    while True:
        fuel = calc_fuel(i)
        if results and fuel > results[-1]:
            break
        results.append(fuel)
        i += 1
    return int(results.pop())


########################################################################################


def aoc2021_day8_part1(puzzle_input):
    lines = puzzle_input.split('\n')
    unique_nums = 0
    for line in lines:
        _, output = line.split(' | ')
        for v in output.split():
            if len(v) in (2, 3, 4, 7):
                unique_nums += 1
    return unique_nums

def aoc2021_day8_part2(puzzle_input):
    lines = puzzle_input.split('\n')

    '''
    0:  6  abc efg
    1:  2    c  f   unique
    2:  5  a cde g
    3:  5  a cd fg
    4:  4   bcd f   unique
    5:  5  ab d fg
    6:  6  ab defg
    7:  3  a c  f   unique
    8:  7  abcdefg  unique
    9:  6  abcd fg
    '''

    num_translation = {
        'abcefg': 0, 
        'cf': 1, 
        'acdeg': 2, 
        'acdfg': 3, 
        'bcdf': 4, 
        'abdfg': 5, 
        'abdefg': 6, 
        'acf': 7, 
        'abcdefg': 8, 
        'abcdfg': 9
        }

    output_sum = 0
    for line in lines:
        translation = dict()
        patterns, output = line.split(' | ')
        patterns = sorted(patterns.split(), key=lambda x: len(x))
        
        c_f = set(patterns[0])
        a_c_f = set(patterns[1])
        b_c_d_f = set(patterns[2])
        c_d_e = set(c for i in (6,7,8) for c in 'abcdefg' if c not in patterns[i])
        b_d = b_c_d_f.difference(a_c_f)
        d_e = c_d_e.difference(c_f)

        translation[a_c_f.difference(c_f).pop()] = 'a'
        translation[(b_d.difference(d_e)).pop()] = 'b'
        translation[(c_d_e & c_f).pop()] = 'c'
        translation[(b_d & d_e).pop()] = 'd'
        translation[(d_e.difference(b_d)).pop()] = 'e'
        translation[(c_f.difference(c_d_e)).pop()] = 'f'
        translation[set(patterns[9]).difference(set(translation)).pop()] = 'g'

        output_num = ''
        for n in output.split():
            t = ''
            for c in n:
                t += translation[c]
            t = ''.join(sorted(t))
            output_num += str(num_translation[t])

        output_sum += int(output_num)

    return output_sum


########################################################################################


def aoc2021_day9_part1(puzzle_input):
    grid = [[int(n) for n in row] for row in puzzle_input.split('\n')]
    x_range = range(len(grid[0]))
    y_range = range(len(grid))

    def get_neighbors(x, y):
        adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i, j in adj:
            if x+i in x_range and y+j in y_range:
                yield x+i, y+j

    risk_level_sum = 0
    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            if all(height < grid[j][i] for i, j in get_neighbors(x, y)):
                risk_level_sum += height + 1
    return risk_level_sum


def aoc2021_day9_part2(puzzle_input):
    grid = [[int(n) for n in row] for row in puzzle_input.split('\n')]
    x_range = range(len(grid[0]))
    y_range = range(len(grid))

    def get_neighbors(x, y):
        adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i, j in adj:
            if x+i in x_range and y+j in y_range:
                yield x+i, y+j

    def add_basin():
        size = 0
        queue = [unvisited.pop()]
        while queue:
            x, y = queue.pop()
            if grid[y][x] == 9:
                continue
            size += 1
            for i, j in get_neighbors(x, y):
                if (i, j) in unvisited:
                    unvisited.remove((i, j))
                    queue.append((i, j))
        basins.append(size) 

    unvisited = [(x, y) for x in x_range for y in y_range]  
    basins = []
    while unvisited:
        add_basin()

    return math.prod(sorted(basins)[-3:]) 


########################################################################################


def aoc2021_day10_part1(puzzle_input):
    lines = puzzle_input.split('\n')

    # Part 1:
    syntax_err_score = 0
    syntax_err = dict(zip(')]}>', [3, 57, 1197, 25137]))


    # Part 2:
    autocomp_scores = []
    autocomp = dict(zip('([{<', [1, 2, 3, 4]))

    brackets = dict(zip(')]}>', '([{<'))
    for line in lines:
        open_brackets = []
        for b in line:
            if b in '([{<':
                open_brackets.append(b)
            else:
                if open_brackets.pop() == brackets[b]:
                    continue
                else:   # line must be corrupted (part 1)
                    syntax_err_score += syntax_err[b]
                    break

        else:   # line must be uncorrupted but incomplete (part 2)
            score = 0
            while open_brackets:
                score = 5 * score + autocomp[open_brackets.pop()]
            autocomp_scores.append(score)

    middle_autocomp_score = sorted(autocomp_scores)[len(autocomp_scores)//2]

    return syntax_err_score


def aoc2021_day10_part2(puzzle_input):
    lines = puzzle_input.split('\n')

    # Part 1:
    syntax_err_score = 0
    syntax_err = dict(zip(')]}>', [3, 57, 1197, 25137]))


    # Part 2:
    autocomp_scores = []
    autocomp = dict(zip('([{<', [1, 2, 3, 4]))

    brackets = dict(zip(')]}>', '([{<'))
    for line in lines:
        open_brackets = []
        for b in line:
            if b in '([{<':
                open_brackets.append(b)
            else:
                if open_brackets.pop() == brackets[b]:
                    continue
                else:   # line must be corrupted (part 1)
                    syntax_err_score += syntax_err[b]
                    break

        else:   # line must be uncorrupted but incomplete (part 2)
            score = 0
            while open_brackets:
                score = 5 * score + autocomp[open_brackets.pop()]
            autocomp_scores.append(score)

    return sorted(autocomp_scores)[len(autocomp_scores)//2]


########################################################################################


def aoc2021_day11_part1(puzzle_input):
    grid = [[int(n) for n in row] for row in puzzle_input.split()]
    rows, cols = len(grid), len(grid[0])
    flashes = 0
    for _ in range(100):
        flashing = set()
        for r in range(rows):
            for c in range(cols):
                grid[r][c] += 1
                if grid[r][c] >= 10:
                    flashing.add((r, c))
        while flashing:
            r, c = flashing.pop()
            if grid[r][c] == 0:
                continue
            grid[r][c] = 0
            flashes += 1
            for x in range(max(0, r-1), min(rows, r+2)):
                for y in range(max(0, c-1), min(cols, c+2)):
                    if (x == r and y == c) or (grid[x][y] == 0):
                        continue
                    grid[x][y] += 1
                    if grid[x][y] >= 10:
                        flashing.add((x, y))
    return flashes


def aoc2021_day11_part2(puzzle_input):
    grid = [[int(n) for n in row] for row in puzzle_input.split()]
    rows, cols = len(grid), len(grid[0])
    n_octos = rows * cols
    step = 0
    while True:
        step += 1
        flashing = set()
        flashes = 0
        for r in range(rows):
            for c in range(cols):
                grid[r][c] += 1
                if grid[r][c] >= 10:
                    flashing.add((r, c))
        while flashing:
            r, c = flashing.pop()
            if grid[r][c] == 0:
                continue
            grid[r][c] = 0
            flashes += 1
            for x in range(max(0, r-1), min(rows, r+2)):
                for y in range(max(0, c-1), min(cols, c+2)):
                    if (x == r and y == c) or (grid[x][y] == 0):
                        continue
                    grid[x][y] += 1
                    if grid[x][y] >= 10:
                        flashing.add((x, y))

        if flashes == n_octos:
            return step


########################################################################################


def aoc2021_day_12_part1(puzzle_input):
    graph = defaultdict(list)
    for a, b in re.findall(r'(\w+)-(\w+)', puzzle_input):
        graph[a].append(b)
        graph[b].append(a)

    paths = []
    def dfs(node, path):
        if node == 'end':
            paths.append(path)
            return
        for adj in graph[node]:
            if adj in path:
                continue
            if adj.isupper():
                dfs(adj, path.copy())
            else:
                dfs(adj, path + [adj])

    dfs('start', ['start'])
    return len(paths)


def aoc2021_day_12_part2(puzzle_input):
    graph = defaultdict(list)
    for a, b in re.findall(r'(\w+)-(\w+)', puzzle_input):
        graph[a].append(b)
        graph[b].append(a)

    paths = []
    def dfs(node, path, exception_used):
        if node == 'end':
            paths.append(path)
            return
        for adj in graph[node]:
            if adj == 'start':
                continue
            if adj.isupper():
                dfs(adj, path.copy(), exception_used)
            elif adj not in path:
                dfs(adj, path + [adj], exception_used)
            elif not exception_used: 
                dfs(adj, path + [adj], True)

    dfs('start', ['start'], False)
    return len(paths)


########################################################################################


def aoc2021_day13_part1(puzzle_input):
    # Parse input
    dots, instructions = puzzle_input.split('\n\n')
    dots = [(int(x), int(y)) for x, y in re.findall(r'(\d+),(\d+)', dots)]

    # Create initial transparent
    width = max(dots)[0] + 1
    height = max(dots, key=lambda x: x[1])[1] + 1
    grid = [[' '] * width for _ in range(height)]
    for x, y in dots:
        grid[y][x] = '#'

    # Folding functions
    def fold_up(idx):
        for x in range(width):
            for y in range(1, height-idx):
                if grid[idx + y][x] == '#':
                    grid[idx - y][x] = '#'
        return grid[:idx][:], height // 2

    def fold_left(idx):
        for x in range(1, width-idx):
            for y in range(height):
                if grid[y][idx + x] == '#':
                    grid[y][idx - x] = '#'
        return [row[:idx] for row in grid], width // 2

    # Execute first folding instruction
    match = re.search(r'(x|y)=(\d+)', instructions.split('\n')[0])
    if match.group(1) == 'x':   # vertical folding line
        grid, width = fold_left(int(match.group(2)))
    else:                       # horizontal folding line
        grid, height = fold_up(int(match.group(2)))

    return sum(sum(ele == '#' for ele in row) for row in grid)


def aoc2021_day13_part2(puzzle_input):
    # Parse input
    dots, instructions = puzzle_input.split('\n\n')
    dots = [(int(x), int(y)) for x, y in re.findall(r'(\d+),(\d+)', dots)]

    # Create initial transparent
    width = max(dots)[0] + 1
    height = max(dots, key=lambda x: x[1])[1] + 1
    grid = [[' '] * width for _ in range(height)]
    for x, y in dots:
        grid[y][x] = '#'

    # Folding functions
    def fold_up(idx):
        for x in range(width):
            for y in range(1, height-idx):
                if grid[idx + y][x] == '#':
                    grid[idx - y][x] = '#'
        return grid[:idx][:], height // 2

    def fold_left(idx):
        for x in range(1, width-idx):
            for y in range(height):
                if grid[y][idx + x] == '#':
                    grid[y][idx - x] = '#'
        return [row[:idx] for row in grid], width // 2
    
    # Execute folding instructions
    for axis, idx in re.findall(r'(x|y)=(\d+)', instructions):
        if axis == 'x':     # vertical line
            grid, width = fold_left(int(idx))
        else:               # horizontal line
            grid, height = fold_up(int(idx))

    return '\n'.join(''.join(row) for row in grid)


########################################################################################


def aoc2021_day14_part1(puzzle_input):

    # Parse input
    molecule, reactions = puzzle_input.split('\n\n')

    # Create replacement dictionary
    replace = {}
    for x, y, z in re.findall('(\w)(\w) -> (\w)', reactions):
        replace[x + y] = z + y

    # Execute 10 transitions steps
    for _ in range(10):
        new_molecule = molecule[0]
        for i in range(len(molecule)-1):
            new_molecule += replace[molecule[i:i+2]]
        molecule = new_molecule

    # Return difference between most and least frequent letter
    letter_counts = sorted(Counter(molecule).values())
    return letter_counts[-1] - letter_counts[0]


def aoc2021_day14_part2(puzzle_input):
    
    # Parse input
    molecule, reactions = puzzle_input.split('\n\n')

    # Create replacement dictionary
    replace = {}
    for x, y, z in re.findall('(\w)(\w) -> (\w)', reactions):
        replace[x + y] = [x + z, z + y]

    # Count (overlapping) pairs
    pairs = defaultdict(int)
    for i in range(len(molecule)-1):
        pairs[molecule[i:i+2]] += 1

    # Execute 40 transition steps
    for _ in range(40):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            for new_pair in replace[pair]:
                new_pairs[new_pair] += count
        pairs = new_pairs

    # Count individual letters in pairs
    letters = defaultdict(int)
    letters[molecule[0]] = 1
    for pair, count in pairs.items():
        letters[pair[1]] += count

    # Return difference between most and least frequent letter
    letter_counts = sorted(letters.values())
    return letter_counts[-1] - letter_counts[0]


########################################################################################


def aoc2021_day15_part1(puzzle_input):
    pass

def aoc2021_day15_part2(puzzle_input):
    pass

########################################################################################



def aoc2021_day16_part1(puzzle_input):
    pass

def aoc2021_day16_part2(puzzle_input):
    pass

########################################################################################


def aoc2021_day17_part1(puzzle_input):
    pass

def aoc2021_day17_part2(puzzle_input):
    pass

########################################################################################


def aoc2021_day18_part1(puzzle_input):
    pass

def aoc2021_day18_part2(puzzle_input):
    pass

########################################################################################


def aoc2021_day19_part1(puzzle_input):
    pass

def aoc2021_day19_part2(puzzle_input):
    pass

########################################################################################


def aoc2021_day20_part1(puzzle_input):
    pass

def aoc2021_day20_part2(puzzle_input):
    pass
########################################################################################



def aoc2021_day21_part1(puzzle_input):
    pass

def aoc2021_day21_part2(puzzle_input):
    pass
########################################################################################



def aoc2021_day22_part1(puzzle_input):
    pass

def aoc2021_day22_part2(puzzle_input):
    pass
########################################################################################



def aoc2021_day23_part1(puzzle_input):
    pass

def aoc2021_day23_part2(puzzle_input):
    pass

########################################################################################


def aoc2021_day24_part1(puzzle_input):
    pass

def aoc2021_day24_part2(puzzle_input):
    pass

########################################################################################


def aoc2021_day25_part1(puzzle_input):
    pass

def aoc2021_day25_part2(puzzle_input):
    pass


