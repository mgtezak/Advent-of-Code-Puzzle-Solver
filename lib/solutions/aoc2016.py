import numpy as np
import string
import hashlib
import re
from math import prod
from copy import deepcopy
from itertools import combinations
from collections import deque




def aoc2016_day1_part1(puzzle_input):
    instructions = puzzle_input.split(', ')
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # North, East, South, West
    x = y = d = 0   # starting out at (0, 0) facing north
    visited = set()
    for ins in instructions:
        turn, dist = ins[0], int(ins[1:])
        if turn == 'R':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
            
        i, j = directions[d]
        for _ in range(dist):
            x += i
            y += j
            visited.add((x, y))

    return abs(x) + abs(y)


def aoc2016_day1_part2(puzzle_input):
    instructions = puzzle_input.split(', ')

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # North, East, South, West

    x = y = d = 0   # starting out at (0, 0) facing north
    visited = set()
    visited_twice = None 

    for ins in instructions:
        turn, dist = ins[0], int(ins[1:])
        if turn == 'R':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
            
        i, j = directions[d]
        for _ in range(dist):
            x += i
            y += j
            if not visited_twice and (x, y) in visited:
                visited_twice = abs(x) + abs(y)
            visited.add((x, y))

    return visited_twice


####################################################################################################


def aoc2016_day2_part1(puzzle_input):
    keypad = ['123', '456', '789']
    bathroom_code = []
    for line in puzzle_input.split():
        x = y = 1
        for char in line:
            if char == 'L':
                x -= 1 if x > 0 else 0
            elif char == 'R':            
                x += 1 if x < 2 else 0
            elif char == 'U':
                y -= 1 if y > 0 else 0
            elif char == 'D':           
                y += 1 if y < 2 else 0
        bathroom_code.append(str(keypad[y][x]))

    return "".join(bathroom_code)


def aoc2016_day2_part2(puzzle_input):
    keypad = ['  1  ', ' 234 ', '56789', ' ABC ', '  D  ']
    bathroom_code = []
    for line in puzzle_input.split():
        x, y = 0, 2    # start at position of '5'
        for char in line:
            if char == 'L':
                x -= 1 if x > 0 and keypad[y][x-1] != ' ' else 0
            elif char == 'R':            
                x += 1 if x < 4 and keypad[y][x+1] != ' ' else 0
            elif char == 'U':
                y -= 1 if y > 0 and keypad[y-1][x] != ' ' else 0
            elif char == 'D':           
                y += 1 if y < 4 and keypad[y+1][x] != ' ' else 0
        bathroom_code.append(keypad[y][x])

    return "".join(bathroom_code)


####################################################################################################


def aoc2016_day3_part1(puzzle_input):
    lines = [list(map(int, line.split())) for line in puzzle_input.split('\n')]

    def validate(triangle):
        half = sum(triangle) / 2
        return True if all(s < half for s in triangle) else False

    return sum(validate(triangle) for triangle in lines)


def aoc2016_day3_part2(puzzle_input):
    lines = [list(map(int, line.split())) for line in puzzle_input.split('\n')]

    def validate(triangle):
        half = sum(triangle) / 2
        return True if all(s < half for s in triangle) else False

    return sum(validate((lines[i][j], lines[i+1][j], lines[i+2][j])) for i in range(0, len(lines), 3) for j in range(3))


####################################################################################################


def aoc2016_day4_part1(puzzle_input):
    lines = puzzle_input.split()

    def parse(lines):
        for line in lines:
            letters = ''.join(line.split('-')[:-1])
            sector_id = int(line.split('-')[-1].split('[')[0])
            checksum = line.split('[')[1].strip(']')
            yield letters, sector_id, checksum

    def get_true_checksum(letters):
        ranking = sorted((-letters.count(letter), letter) for letter in set(letters))
        return ''.join(letter for _, letter in ranking[:5])

    return sum(sector_id for letters, sector_id, checksum in parse(lines) if checksum == get_true_checksum(letters))


def aoc2016_day4_part2(puzzle_input):
    lines = puzzle_input.split()

    def parse(lines):
        for line in lines:
            letters = ''.join(line.split('-')[:-1])
            sector_id = int(line.split('-')[-1].split('[')[0])
            checksum = line.split('[')[1].strip(']')
            yield letters, sector_id, checksum

    def decrypt(letters, sector_id):
        shift = sector_id % 26
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        dictionary = str.maketrans(alphabet, shifted_alphabet)
        return letters.translate(dictionary)

    return [sector_id for letters, sector_id, _ in parse(lines) if 'northpole' in decrypt(letters, sector_id)][0]


####################################################################################################


# SLOW:
def aoc2016_day5_part1(puzzle_input):
    pw = ''
    i = 1
    while len(pw) < 8:
        hash = hashlib.md5((puzzle_input + str(i)).encode()).hexdigest()
        if hash.startswith('00000'):
            pw += hash[5]
        i += 1
    return pw


# VERY SLOW:
def aoc2016_day5_part2(puzzle_input):
    pw = {}
    i = 1
    while len(pw) < 8:
        hash = hashlib.md5((puzzle_input + str(i)).encode()).hexdigest()
        if (hash.startswith('00000') and \
            hash[5].isnumeric() and \
            int(hash[5]) in range(8) and \
            int(hash[5]) not in pw):                    
                pw[int(hash[5])] = hash[6]
        i += 1
    return ''.join(pw[i] for i in range(8))


####################################################################################################


def aoc2016_day6_part1(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    msg = ''
    for i in range(8):
        letters = [line[i] for line in lines]
        most_freq = sorted((letters.count(l), l) for l in letters)[-1][1]
        msg += most_freq
    return msg


def aoc2016_day6_part2(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    msg = ''
    for i in range(8):
        letters = [line[i] for line in lines]
        least_freq = sorted((letters.count(l), l) for l in letters)[0][1]
        msg += least_freq
    return msg


####################################################################################################


def aoc2016_day7_part1(puzzle_input):

    def contains_abba(string):
        for i in range(len(string)-3):
            a, b, c, d = string[i], string[i+1], string[i+2], string[i+3]
            if a != b and a == d and b == c:
                return True

    def supports_TLS(ip_address):
        if not contains_abba(ip_address):
            return False
        bracketed = re.split('\W', ip_address)[1::2]
        for x in bracketed:
            if contains_abba(x):
                return False
        return True

    return sum(supports_TLS(ip) for ip in puzzle_input.split('\n'))


def aoc2016_day7_part2(puzzle_input):

    def get_bab(string):
        bab_set = set()
        for i in range(len(string)-2):
            a, b, c = string[i], string[i+1], string[i+2]
            if a == c and a != b:
                bab_set.add(b + a + b)  
        return bab_set

    def contains_bab(string, bab_set):
        for bab in bab_set:
            if bab in string:
                return True

    def supports_SSL(ip_address):
        unbracketed = re.split('\W', ip_address)[::2]
        bracketed = re.split('\W', ip_address)[1::2]
        bab_set = set()
        for u in unbracketed:
            bab_set.update(get_bab(u))
        for b in bracketed:
            if contains_bab(b, bab_set):
                return True
        return False
        
    return sum(supports_SSL(ip) for ip in puzzle_input.split('\n'))


####################################################################################################


def aoc2016_day8_part1(puzzle_input):
    instructions = [line.split() for line in puzzle_input.split('\n')]
    display = np.zeros((6, 50))

    for i in instructions:
        if i[0] == 'rect':
            cols, rows = int(i[1].split('x')[0]), int(i[1].split('x')[1])
            for x in range(cols):
                for y in range(rows):
                    display[y][x] = 1

        elif i[1] == 'row':
            row_index = int(i[2].strip('y='))
            right = int(i[-1])
            row = list(display[row_index])
            row = row[-right:] + row[:-right]
            display[row_index] = row

        elif i[1] == 'column':
            col = int(i[2].strip('x='))
            down = int(i[-1])
            lights = []
            for row in range(6):
                lights.append(display[row][col])
            lights = lights[-down:] + lights[:-down]
            for row in range(6):
                display[row][col] = lights[row]

    return int(display.sum())


def aoc2016_day8_part2(puzzle_input):
    instructions = [line.split() for line in puzzle_input.split('\n')]
    display = np.zeros((6, 50))
    for i in instructions:
        if i[0] == 'rect':
            cols, rows = int(i[1].split('x')[0]), int(i[1].split('x')[1])
            for x in range(cols):
                for y in range(rows):
                    display[y][x] = 1

        elif i[1] == 'row':
            row_index = int(i[2].strip('y='))
            right = int(i[-1])
            row = list(display[row_index])
            row = row[-right:] + row[:-right]
            display[row_index] = row
            
        elif i[1] == 'column':
            col = int(i[2].strip('x='))
            down = int(i[-1])
            lights = []
            for row in range(6):
                lights.append(display[row][col])
            lights = lights[-down:] + lights[:-down]
            for row in range(6):
                display[row][col] = lights[row]

    # formatted = ''
    # for row in display:
    #     row = ['#' if element == 1 else ' ' for element in row]
    #     formatted += ''.join(row) + '\n'
    # return formatted
    return '\n'.join(''.join(['#' if element == 1 else ' ' for element in row]) for row in display)


####################################################################################################


def aoc2016_day9_part1(puzzle_input):
    length = 0
    while puzzle_input:
        marker = re.search(r'\((\d+)x(\d+)\)', puzzle_input)
        if marker:
            start, stop = marker.span()
            chars, repeat = map(int, marker.groups())
            length += start + chars * repeat
            puzzle_input = puzzle_input[stop+chars:]

        else:
            length += len(puzzle_input)
            break
        
    return length
        

def aoc2016_day9_part2(puzzle_input):

    def decompress(compressed):
        length = 0
        while compressed:
            marker = re.search(r'\((\d+)x(\d+)\)', compressed)
            if marker:
                start, stop = marker.span()
                chars, repeat = map(int, marker.groups())
                length += start + decompress(compressed[stop: stop + chars]) * repeat
                compressed = compressed[stop+chars:]

            else:
                length += len(compressed)
                break
            
        return length
                
    return decompress(puzzle_input)


####################################################################################################


def aoc2016_day10_part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]

    def give_to(type, id, val):
        if type == 'bot':
            if bots.get(id):
                bots[id].append(val)
                fully_loaded.append(id)
            else:
                bots[id] = [val]
        else:
            outputs[id] = val

    bots = {}
    outputs = {}
    fully_loaded = []

    for line in lines:
        if line[0] == 'value':
            val, bot_id = line[1], line[-1]
            give_to('bot', bot_id, int(val))

    while fully_loaded:
        bot_id = fully_loaded.pop()
        for line in lines:
            if line[0] == 'bot' and line[1] == bot_id:
                low, high = sorted(bots[bot_id])
                if (low, high) == (17, 61):
                    return bot_id
                
                give_to(line[5], line[6], low)
                give_to(line[-2], line[-1], high)


def aoc2016_day10_part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]

    def give_to(type, id, val):
        if type == 'bot':
            if bots.get(id):
                bots[id].append(val)
                fully_loaded.append(id)
            else:
                bots[id] = [val]
        else:
            outputs[id] = val

    bots = {}
    outputs = {}
    fully_loaded = []

    for line in lines:
        if line[0] == 'value':
            val, bot_id = line[1], line[-1]
            give_to('bot', bot_id, int(val))

    while fully_loaded:
        bot_id = fully_loaded.pop()
        for line in lines:
            if line[0] == 'bot' and line[1] == bot_id:
                low, high = sorted(bots[bot_id])
                give_to(line[5], line[6], low)
                give_to(line[-2], line[-1], high)

    return prod(outputs[str(i)] for i in range(3))


####################################################################################################


def aoc2016_day11_part1(puzzle_input):


    def is_valid(floor):
        microchips = set(i[:2] for i in floor if i[2] == 'M')
        if not microchips or len(microchips) == len(floor):
            return True
        generators = set(i[:2] for i in floor if i[2] == 'G')
        return not (microchips - generators)


    def is_victorious(state):
        return all(state[i] == set() for i in range(3))


    def move(state, obj, floor, nxt_floor):
        new_state = deepcopy(state)

        new_state[floor] -= obj
        if not is_valid(new_state[floor]):
            return False
        
        new_state[nxt_floor] |= obj
        if not is_valid(new_state[nxt_floor]):
            return False
        
        return new_state


    def get_hash(floor, state):
        pair_map = [[None, None] for _ in range(len(pairs))]
        i = 0
        for i, line in enumerate(state):
            for ele in line:
                pair_map[pairs[ele[:2]]][ele[2]=='G'] = str(i)
        return '.'.join(sorted(','.join(pair) for pair in pair_map)) + f'!{floor}'


    def get_valid_moves(state, floor, nxt_floor, n_objs):
        valid_moves = []
        for obj in combinations(state[floor], n_objs):

            nxt_state = move(state, set(obj), floor, nxt_floor)
            if not nxt_state:
                continue

            state_hash = get_hash(nxt_floor, nxt_state)
            if state_hash in hashmap:
                continue

            hashmap.add(state_hash)
            valid_moves.append((nxt_floor, nxt_state))

        return valid_moves


    state = []
    for line in puzzle_input.split('\n'):
        line = re.sub(r'-compatible|enerator|icrochip', '', line)
        state.append(set(name.upper() + type.upper() for name, type in re.findall(r'(\w{2})\w+ (g|m)', line)))
    
    pairs = {x: i for i, x in enumerate(re.findall(r'(\w\w)G', ' '.join(' '.join(row) for row in state)))}

    hashmap = set()
    queue = deque([(0, state)])
    steps = 0
    while queue:
        for _ in range(len(queue)):
            floor, state = queue.popleft()

            if is_victorious(state):
                return steps
            
            if floor < 3:   # if you can move 2 objs up, don't bother moving only 1 up
                if move_2_up := get_valid_moves(state, floor, floor+1, 2):  
                    queue.extend(move_2_up)
                else:
                    queue.extend(get_valid_moves(state, floor, floor+1, 1))

            if floor > 0:   # never move more than 1 obj down
                queue.extend(get_valid_moves(state, floor, floor-1, 1))

        steps += 1


def aoc2016_day11_part2(puzzle_input):


    def is_valid(floor):
        microchips = set(i[:2] for i in floor if i[2] == 'M')
        if not microchips or len(microchips) == len(floor):
            return True
        generators = set(i[:2] for i in floor if i[2] == 'G')
        return not (microchips - generators)


    def is_victorious(state):
        return all(state[i] == set() for i in range(3))


    def move(state, obj, floor, nxt_floor):
        new_state = deepcopy(state)

        new_state[floor] -= obj
        if not is_valid(new_state[floor]):
            return False
        
        new_state[nxt_floor] |= obj
        if not is_valid(new_state[nxt_floor]):
            return False
        
        return new_state


    def get_hash(floor, state):
        pair_map = [[None, None] for _ in range(len(pairs))]
        i = 0
        for i, line in enumerate(state):
            for ele in line:
                pair_map[pairs[ele[:2]]][ele[2]=='G'] = str(i)
        return '.'.join(sorted(','.join(pair) for pair in pair_map)) + f'!{floor}'


    def get_valid_moves(state, floor, nxt_floor, n_objs):
        valid_moves = []
        for obj in combinations(state[floor], n_objs):

            nxt_state = move(state, set(obj), floor, nxt_floor)
            if not nxt_state:
                continue

            state_hash = get_hash(nxt_floor, nxt_state)
            if state_hash in hashmap:
                continue

            hashmap.add(state_hash)
            valid_moves.append((nxt_floor, nxt_state))

        return valid_moves


    state = []
    for line in puzzle_input.split('\n'):
        line = re.sub(r'-compatible|enerator|icrochip', '', line)
        state.append(set(name.upper() + type.upper() for name, type in re.findall(r'(\w{2})\w+ (g|m)', line)))
    
    state[0] |= {'ELG', 'ELM', 'DIG', 'DIM'}
    pairs = {x: i for i, x in enumerate(re.findall(r'(\w\w)G', ' '.join(' '.join(row) for row in state)))}

    hashmap = set()
    queue = deque([(0, state)])
    steps = 0
    while queue:
        for _ in range(len(queue)):
            floor, state = queue.popleft()

            if is_victorious(state):
                return steps
            
            if floor < 3:   # if you can move 2 objs up, don't bother moving only 1 up
                if move_2_up := get_valid_moves(state, floor, floor+1, 2):  
                    queue.extend(move_2_up)
                else:
                    queue.extend(get_valid_moves(state, floor, floor+1, 1))

            if floor > 0:   # never move more than 1 obj down
                queue.extend(get_valid_moves(state, floor, floor-1, 1))

        steps += 1


####################################################################################################


def aoc2016_day12_part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    registry = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    i = 0 
    while i < len(lines):
        l = lines[i]
        if l[0] == 'cpy':
            registry[l[2]] = int(l[1]) if l[1].isnumeric() else registry[l[1]]
        elif l[0] == 'inc':
            registry[l[1]] += 1
        elif l[0] == 'dec':
            registry[l[1]] -= 1
        elif (l[1].isalpha() and registry[l[1]]) or (l[1].isnumeric() and l[1] != '0'):
            i += int(l[2]) - 1
        i += 1
    return registry['a']


def aoc2016_day12_part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    registry = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    i = 0 
    while i < len(lines):
        l = lines[i]
        if l[0] == 'cpy':
            registry[l[2]] = int(l[1]) if l[1].isnumeric() else registry[l[1]]
        elif l[0] == 'inc':
            registry[l[1]] += 1
        elif l[0] == 'dec':
            registry[l[1]] -= 1
        elif (l[1].isalpha() and registry[l[1]]) or (l[1].isnumeric() and l[1] != '0'):
            i += int(l[2]) - 1
        i += 1
    return registry['a']


####################################################################################################


def aoc2016_day13_part1(puzzle_input):
    puzzle_input = int(puzzle_input)

    def is_wall(x, y):
        result = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
        return bool(bin(result).count('1') % 2)

    visited = {(1, 1)}
    q = deque([(1, 1, 0)])
    while q:
        x, y, steps = q.popleft()
        if x == 31 and y == 39:
            break
        for i, j in {(x+1, y), (x-1, y), (x, y+1), (x, y-1)} - visited:
            if i < 0 or j < 0 or is_wall(i, j):
                continue
            q.append((i, j, steps+1))
            visited.add((i, j))

    return steps


def aoc2016_day13_part2(puzzle_input):
    puzzle_input = int(puzzle_input)

    def is_wall(x, y):
        result = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
        return bool(bin(result).count('1') % 2)

    visited = {(1, 1)}
    q = deque([(1, 1, 50)])
    while q:
        x, y, steps = q.popleft()
        if not steps:
            continue
        for i, j in {(x+1, y), (x-1, y), (x, y+1), (x, y-1)} - visited:
            if i < 0 or j < 0 or is_wall(i, j):
                continue
            q.append((i, j, steps-1))
            visited.add((i, j))

    return len(visited)


####################################################################################################


def aoc2016_day14_part1(puzzle_input):
    keys = []
    triplets = {char: [] for char in '0123456789abcdef'}
    i = 0
    while True:
        hash = hashlib.md5(f'{puzzle_input}{i}'.encode()).hexdigest()

        # Check for quintuples
        for char in re.findall(r'([a-f0-9])\1\1\1\1', hash):
            while triplets[char] and triplets[char][0] < i - 1000:
                triplets[char].pop(0)
            keys.extend(triplets[char])
            triplets[char] = []
            keys.sort()

        # Check for triplets 
        if match := re.search(r'([a-f0-9])\1\1', hash):
            triplets[match.group(0)[0]].append(i)

        if len(keys) >= 64 and i > keys[63] + 1000:
            break

        i += 1

    return keys[63]


def aoc2016_day14_part2(puzzle_input):
    keys = []
    triplets = {char: [] for char in '0123456789abcdef'}
    i = 0
    while True:
        hash = f'{puzzle_input}{i}'
        for _ in range(2017):
            hash = hashlib.md5(hash.encode()).hexdigest()
        
        # Check for quintuples
        for char in re.findall(r'([a-f0-9])\1\1\1\1', hash):
            while triplets[char] and triplets[char][0] < i - 1000:
                triplets[char].pop(0)
            keys.extend(triplets[char])
            triplets[char] = []
            keys.sort()

        # Check for triplets 
        if match := re.search(r'([a-f0-9])\1\1', hash):
            triplets[match.group(0)[0]].append(i)

        if len(keys) >= 64 and i > keys[63] + 1000:
            break

        i += 1

    return keys[63]



####################################################################################################


def aoc2016_day15_part1(puzzle_input):
    pass


def aoc2016_day15_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day16_part1(puzzle_input):
    pass


def aoc2016_day16_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day17_part1(puzzle_input):
    pass


def aoc2016_day17_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day18_part1(puzzle_input):
    pass


def aoc2016_day18_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day19_part1(puzzle_input):
    pass


def aoc2016_day19_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day20_part1(puzzle_input):
    pass


def aoc2016_day20_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day21_part1(puzzle_input):
    pass


def aoc2016_day21_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day22_part1(puzzle_input):
    pass


def aoc2016_day22_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day23_part1(puzzle_input):
    pass


def aoc2016_day23_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day24_part1(puzzle_input):
    pass


def aoc2016_day24_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day25_part1(puzzle_input):
    pass


def aoc2016_day25_part2(puzzle_input):
    pass



