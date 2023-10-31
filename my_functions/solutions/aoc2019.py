from collections import defaultdict
from itertools import permutations
import math



def aoc2019_day1_part1(puzzle_input):
    data = puzzle_input.split('\n')

    def calculate_fuel(x):
        fuel = x // 3 - 2
        return max(0, fuel)

    return sum(calculate_fuel(int(x)) for x in data)


def aoc2019_day1_part2(puzzle_input):
    data = puzzle_input.split('\n')

    def calculate_fuel(x):
        fuel = x // 3 - 2
        fuel = max(0, fuel)
        if fuel >= 9:
            fuel += calculate_fuel(fuel)
        return fuel

    return sum(calculate_fuel(int(x)) for x in data)


####################################################################################################


def aoc2019_day2_part1(puzzle_input):
        nums = list(map(int, puzzle_input.split(',')))
        nums[1], nums[2] = 12, 2
        for i in range(len(nums)):
            val = nums[i]
            if i % 4 == 0:  
                if val == 1:
                    nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
                elif val == 2:
                    nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
                elif val == 99:
                    break
        return nums[0]


def aoc2019_day2_part2(puzzle_input):
    instructions = list(map(int, puzzle_input.split(',')))

    def run_intcode(noun, verb):
        nums = instructions.copy()
        nums[1], nums[2] = noun, verb
        for i, val in enumerate(nums):
            if i % 4 == 0:  
                if val == 1:
                    nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
                elif val == 2:
                    nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
                elif val == 99:
                    break
        return nums[0]
            
    for noun in range(100):
        for verb in range(100):
            if run_intcode(noun, verb) == 19690720:
                return 100 * noun + verb


####################################################################################################


def aoc2019_day3_part1(puzzle_input):
    wires = [wire.split(',') for wire in puzzle_input.split('\n')]

    def get_path(wire):
        x = y = steps = 0
        visited = {}
        directions = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
        for cmd in wire:
            distance = int(cmd[1:])
            for _ in range(distance):
                x += directions[cmd[0]][0]
                y += directions[cmd[0]][1]      
                steps += 1
                if (x, y) not in visited:
                    visited[(x, y)] = steps
        return visited

    path_1 = get_path(wires[0])
    path_2 = get_path(wires[1])
    isecs = {abs(x) + abs(y): path_1[(x, y)] + path_2[(x, y)] for x, y in path_1 if (x, y) in path_2}
    return min(isecs)


def aoc2019_day3_part2(puzzle_input):
    wires = [wire.split(',') for wire in puzzle_input.split('\n')]

    def get_path(wire):
        x = y = steps = 0
        visited = {}
        directions = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
        for cmd in wire:
            distance = int(cmd[1:])
            for _ in range(distance):
                x += directions[cmd[0]][0]
                y += directions[cmd[0]][1]      
                steps += 1
                if (x, y) not in visited:
                    visited[(x, y)] = steps
        return visited

    path_1 = get_path(wires[0])
    path_2 = get_path(wires[1])
    isecs = {abs(x) + abs(y): path_1[(x, y)] + path_2[(x, y)] for x, y in path_1 if (x, y) in path_2}
    return min(isecs.values())


####################################################################################################


def aoc2019_day4_part1(puzzle_input):

    def passes(n):   
        s = str(n)
        if any(int(s[i]) > int(s[i+1]) for i in range(5)):
            return False
        groups = [s.count(digit) for digit in set(s)]
        return max(groups) >= 2

    start, end = [int(n) for n in puzzle_input.split('-')]
    return len([n for n in range(start, end) if passes(n)])


def aoc2019_day4_part2(puzzle_input):

    def passes(n):   
        s = str(n)
        if any(int(s[i]) > int(s[i+1]) for i in range(5)):
            return False
        groups = [s.count(digit) for digit in set(s)]
        return 2 in groups

    start, end = [int(n) for n in puzzle_input.split('-')]
    return len([n for n in range(start, end) if passes(n)])


####################################################################################################


def aoc2019_day5_part1(puzzle_input):
    intcode = list(map(int, puzzle_input.split(',')))
    nums = intcode.copy()
    i = 0
    while nums[i] != 99:
        n = str(nums[i])
        args = {
            1: nums[nums[i+1]] if len(n) < 3 or n[-3] == '0' else nums[i+1],
            2: nums[nums[i+2]] if n[-1] != '4' and (len(n) < 4 or n[-4] == '0') else nums[i+2]}

        if n[-1] == '1':
            nums[nums[i+3]] = args[1] + args[2]
            i += 4

        elif n[-1] == '2':
            nums[nums[i+3]] = args[1] * args[2]
            i += 4

        elif n[-1] == '3':
            nums[nums[i+1]] = 1
            i += 2

        elif n[-1] == '4':
            output_val = args[1]
            i += 2

    return output_val            


def aoc2019_day5_part2(puzzle_input):
    nums = list(map(int, puzzle_input.split(',')))
    i = 0
    while nums[i] != 99:
        n = str(nums[i])
        args = {
            1: nums[nums[i+1]] if len(n) < 3 or n[-3] == '0' else nums[i+1],
            2: nums[nums[i+2]] if n[-1] != '4' and (len(n) < 4 or n[-4] == '0') else nums[i+2]}

        if n[-1] == '1':
            nums[nums[i+3]] = args[1] + args[2]
            i += 4

        elif n[-1] == '2':
            nums[nums[i+3]] = args[1] * args[2]
            i += 4

        elif n[-1] == '3':
            nums[nums[i+1]] = 5
            i += 2

        elif n[-1] == '4':
            output_val = args[1]
            i += 2

        elif n[-1] == '5': # part 2
            i = args[2] if args[1] else i + 3

        elif n[-1] == '6': # part 2
            i = args[2] if not args[1] else i + 3

        elif n[-1] == '7': # part 2
            nums[nums[i+3]] = 1 if args[1] < args[2] else 0
            i += 4

        elif n[-1] == '8': # part 2
            nums[nums[i+3]] = 1 if args[1] == args[2] else 0
            i += 4

    return output_val            


####################################################################################################


def aoc2019_day6_part1(puzzle_input):
    lines = [o.split(')') for o in puzzle_input.split('\n')]
    orbits = defaultdict(list)
    for x, y in lines:
        orbits[y].append(x)

    def get_orbits(y):
        if orbits[y] == ['COM']:
            return ['COM']
        return orbits[y] + [get_orbits(x) for x in orbits[y]][0]

    return sum(len(get_orbits(y)) for y in orbits)


def aoc2019_day6_part2(puzzle_input):
    lines = [o.split(')') for o in puzzle_input.split('\n')]
    orbits = defaultdict(list)
    for x, y in lines:
        orbits[y].append(x)

    def get_orbits(y):
        if orbits[y] == ['COM']:
            return ['COM']
        return orbits[y] + [get_orbits(x) for x in orbits[y]][0]

    santa = get_orbits('SAN')
    me = get_orbits('YOU')
    return len([x for x in santa + me if not (x in santa and x in me)])


####################################################################################################


def aoc2019_day7_part1(puzzle_input):
    intcode = list(map(int, puzzle_input.split(',')))

    def run_intcode(input_vals, nums=intcode.copy(), i=0):
        while nums[i] != 99:
            n = str(nums[i])

            if n[-1] == '1':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = val1 + val2
                i += 4

            elif n[-1] == '2':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = val1 * val2
                i += 4

            elif n[-1] == '3':
                if input_vals:
                    nums[nums[i+1]] = input_vals.pop(0)
                    i += 2
                else:
                    return output_val, nums, i

            elif n[-1] == '4':
                output_val = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                i += 2

            elif n[-1] == '5':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                if val1:
                    i = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                else:
                    i += 3

            elif n[-1] == '6':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                if not val1:
                    i = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                else:
                    i += 3

            elif n[-1] == '7':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = 1 if val1 < val2 else 0
                i += 4

            elif n[-1] == '8':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = 1 if val1 == val2 else 0
                i += 4

        return output_val, nums, 'done'            


    def get_thruster_signal(perm):
        output = 0
        i = 0
        amp = 0
        states = {x: [None, None] for x in range(5)}

        while states[4][1] != 'done':
            if perm:
                n = perm.pop(0)
                input = [n, output]
                nums = intcode.copy()
                i = 0
            else:
                input = [output]
                nums, i = states[amp]

            output, nums, i = run_intcode(input, nums, i)
            
            states[amp] = [nums, i]
            amp = (amp + 1) % 5

        return output

    perms1 = list(permutations([0, 1, 2, 3, 4]))
    return max(get_thruster_signal(list(p)) for p in perms1)


def aoc2019_day7_part2(puzzle_input):
    intcode = list(map(int, puzzle_input.split(',')))

    def run_intcode(input_vals, nums=intcode.copy(), i=0):
        while nums[i] != 99:
            n = str(nums[i])

            if n[-1] == '1':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = val1 + val2
                i += 4

            elif n[-1] == '2':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = val1 * val2
                i += 4

            elif n[-1] == '3':
                if input_vals:
                    nums[nums[i+1]] = input_vals.pop(0)
                    i += 2
                else:
                    return output_val, nums, i

            elif n[-1] == '4':
                output_val = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                i += 2

            elif n[-1] == '5':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                if val1:
                    i = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                else:
                    i += 3

            elif n[-1] == '6':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                if not val1:
                    i = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                else:
                    i += 3

            elif n[-1] == '7':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = 1 if val1 < val2 else 0
                i += 4

            elif n[-1] == '8':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = 1 if val1 == val2 else 0
                i += 4

        return output_val, nums, 'done'            

    def get_thruster_signal(perm):
        output = 0
        i = 0
        amp = 0
        states = {x: [None, None] for x in range(5)}

        while states[4][1] != 'done':
            if perm:
                n = perm.pop(0)
                input = [n, output]
                nums = intcode.copy()
                i = 0
            else:
                input = [output]
                nums, i = states[amp]

            output, nums, i = run_intcode(input, nums, i)
            
            states[amp] = [nums, i]
            amp = (amp + 1) % 5

        return output

    perms2 = list(permutations([5, 6, 7, 8, 9]))
    return max(get_thruster_signal(list(p)) for p in perms2)


####################################################################################################


def aoc2019_day8_part1(puzzle_input):
    pixels = puzzle_input
    n = 25 * 6
    layers = []
    while pixels:
        layers.append(pixels[:n])
        pixels = pixels[n:]
    least_zeros = min((layer.count('0'), layer) for layer in layers)[1]
    return least_zeros.count('1') * least_zeros.count('2')


def aoc2019_day8_part2(puzzle_input):
    pixels = puzzle_input
    n = 25 * 6
    layers = []
    while pixels:
        layers.append(pixels[:n])
        pixels = pixels[n:]
    image = defaultdict(str)
    for layer in layers:
        for i, p in enumerate(layer):
            if p in ('0', '1') and not image[i]:
                image[i] = ' ' if p == '0' else '#'

    lines = [[] for _ in range(6)]
    for i in range(n):
        line = i // 25
        lines[line].append(image[i])

    return '\n'.join(''.join(line) for line in lines)


####################################################################################################


def aoc2019_day9_part1(puzzle_input):

    intcode = [int(n) for n in puzzle_input.split(',')]

    nums = defaultdict(int)

    for i, n in enumerate(intcode):
        nums[i] = n

    i = 0
    relative_i = 0
    while nums[i] != 99:
        n = str(nums[i])

        args = {
            1: nums[nums[i+1]] if len(n) < 3 or n[-3] == '0' else nums[i+1] if n[-3] == '1' else nums[relative_i + nums[i+1]],
            2: None if n[-1] == '4' else nums[nums[i+2]] if len(n) < 4 or n[-4] == '0' else nums[i+2] if n[-4] == '1' else nums[relative_i + nums[i+2]]}
        
        write_to = {
            1: nums[i+1] if len(n) < 3 or n[-3] != '2' else relative_i + nums[i+1],
            3: nums[i+3] if len(n) < 5 or n[-5] != '2' else relative_i + nums[i+3]}

        if n[-1] == '1':
            nums[write_to[3]] = args[1] + args[2]
            i += 4

        elif n[-1] == '2':
            nums[write_to[3]] = args[1] * args[2]
            i += 4

        elif n[-1] == '3': 
            nums[write_to[1]] = 1
            i += 2

        elif n[-1] == '4':
            output_val = args[1]
            i += 2

        elif n[-1] == '5':
            i = args[2] if args[1] else i + 3

        elif n[-1] == '6':
            i = args[2] if not args[1] else i + 3

        elif n[-1] == '7': 
            nums[write_to[3]] = 1 if args[1] < args[2] else 0
            i += 4

        elif n[-1] == '8': 
            nums[write_to[3]] = 1 if args[1] == args[2] else 0
            i += 4

        elif n[-1:] == '9':
            relative_i += args[1]
            i += 2

    return output_val


def aoc2019_day9_part2(puzzle_input):

    intcode = [int(n) for n in puzzle_input.split(',')]

    nums = defaultdict(int)

    for i, n in enumerate(intcode):
        nums[i] = n

    i = 0
    relative_i = 0
    while nums[i] != 99:
        n = str(nums[i])

        args = {
            1: nums[nums[i+1]] if len(n) < 3 or n[-3] == '0' else nums[i+1] if n[-3] == '1' else nums[relative_i + nums[i+1]],
            2: None if n[-1] == '4' else nums[nums[i+2]] if len(n) < 4 or n[-4] == '0' else nums[i+2] if n[-4] == '1' else nums[relative_i + nums[i+2]]}
        
        write_to = {
            1: nums[i+1] if len(n) < 3 or n[-3] != '2' else relative_i + nums[i+1],
            3: nums[i+3] if len(n) < 5 or n[-5] != '2' else relative_i + nums[i+3]}

        if n[-1] == '1':
            nums[write_to[3]] = args[1] + args[2]
            i += 4

        elif n[-1] == '2':
            nums[write_to[3]] = args[1] * args[2]
            i += 4

        elif n[-1] == '3': 
            nums[write_to[1]] = 2
            i += 2

        elif n[-1] == '4':
            output_val = args[1]
            i += 2

        elif n[-1] == '5':
            i = args[2] if args[1] else i + 3

        elif n[-1] == '6':
            i = args[2] if not args[1] else i + 3

        elif n[-1] == '7': 
            nums[write_to[3]] = 1 if args[1] < args[2] else 0
            i += 4

        elif n[-1] == '8': 
            nums[write_to[3]] = 1 if args[1] == args[2] else 0
            i += 4

        elif n[-1:] == '9':
            relative_i += args[1]
            i += 2

    return output_val


####################################################################################################


def aoc2019_day10_part1(puzzle_input):

    asteroids = [(x, y) for y, line in enumerate(puzzle_input.split("\n")) for x, pos in enumerate(line) if pos == '#']

    def check_visibility(x1, y1, x2, y2) -> bool:
        '''Make sure the two asteroids aren't the same. Then check vertically, horizontally, 
        with positive and with negative slope whether or not there's another asteroid in the way'''

        if (x1, y1) == (x2, y2):
            return False

        x_min, x_max, y_min, y_max = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
        dx, dy = abs(x2-x1), abs(y2-y1)
        gcd = math.gcd(dx, dy)

        if not dx: # up and down
            for y in range(y_min+1, y_max):
                if (x1, y) in asteroids:
                    return False

        elif not dy: # left and right
            for x in range(x_min+1, x_max):
                if (x, y1) in asteroids:
                    return False

        elif (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2): # top left and bottom right quadrants (y decreases from top to bottom)
            y = y_min + int(dy/gcd)
            for x in range(x_min+int(dx/gcd), x_max, int(dx/gcd)):
                if (x, y) in asteroids:
                    return False
                y += int(dy/gcd)

        else: # top right and bottom left quadrants
            y = y_max - int(dy/gcd)
            for x in range(x_min+int(dx/gcd), x_max, int(dx/gcd)):
                if (x, y) in asteroids:
                    return False
                y -= int(dy/gcd)

        return True

    n_visible_asteroids = max((sum(check_visibility(*a, *b) for b in asteroids), a) for a in asteroids)[0]
    return n_visible_asteroids


def aoc2019_day10_part2(puzzle_input):

    asteroids = [(x, y) for y, line in enumerate(puzzle_input.split("\n")) for x, pos in enumerate(line) if pos == '#']

    def check_visibility(x1, y1, x2, y2) -> bool:
        '''Make sure the two asteroids aren't the same. Then check vertically, horizontally, 
        with positive and with negative slope whether or not there's another asteroid in the way'''

        if (x1, y1) == (x2, y2):
            return False

        x_min, x_max, y_min, y_max = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
        dx, dy = abs(x2-x1), abs(y2-y1)
        gcd = math.gcd(dx, dy)

        if not dx: # up and down
            for y in range(y_min+1, y_max):
                if (x1, y) in asteroids:
                    return False

        elif not dy: # left and right
            for x in range(x_min+1, x_max):
                if (x, y1) in asteroids:
                    return False

        elif (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2): # top left and bottom right quadrants (y decreases from top to bottom)
            y = y_min + int(dy/gcd)
            for x in range(x_min+int(dx/gcd), x_max, int(dx/gcd)):
                if (x, y) in asteroids:
                    return False
                y += int(dy/gcd)

        else: # top right and bottom left quadrants
            y = y_max - int(dy/gcd)
            for x in range(x_min+int(dx/gcd), x_max, int(dx/gcd)):
                if (x, y) in asteroids:
                    return False
                y -= int(dy/gcd)

        return True

    optimal_coords = max((sum(check_visibility(*a, *b) for b in asteroids), a) for a in asteroids)[1]
    x, y = optimal_coords
    x_max = max(x for x, _ in asteroids)
    y_max = max(y for _, y in asteroids)

    up    = [(None, x2, y2) for x2, y2 in asteroids if x2 == x and y2 < y and check_visibility(x, y, x2, y2)]
    down  = [(None, x2, y2) for x2, y2 in asteroids if x2 == x and y2 > y and check_visibility(x, y, x2, y2)]
    right = sorted(((y2-y)/(x2-x), x2, y2) for x2, y2 in asteroids if x2 in range(x+1, x_max+1) and y2 in range(0, y_max+1) and check_visibility(x, y, x2, y2))
    left  = sorted(((y2-y)/(x2-x), x2, y2) for x2, y2 in asteroids if x2 in range(0, x) and y2 in range(0, y_max+1) and check_visibility(x, y, x2, y2))

    clockwise = up + right + down + left
    _, x2, y2 = clockwise[200-1]
    return 100 * x2 + y2


####################################################################################################


def aoc2019_day11_part1(puzzle_input):
    pass


def aoc2019_day11_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day12_part1(puzzle_input):
    pass


def aoc2019_day12_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day13_part1(puzzle_input):
    pass


def aoc2019_day13_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day14_part1(puzzle_input):
    pass


def aoc2019_day14_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day15_part1(puzzle_input):
    pass


def aoc2019_day15_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day16_part1(puzzle_input):
    pass


def aoc2019_day16_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day17_part1(puzzle_input):
    pass


def aoc2019_day17_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day18_part1(puzzle_input):
    pass


def aoc2019_day18_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day19_part1(puzzle_input):
    pass


def aoc2019_day19_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day20_part1(puzzle_input):
    pass


def aoc2019_day20_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day21_part1(puzzle_input):
    pass


def aoc2019_day21_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day22_part1(puzzle_input):
    pass


def aoc2019_day22_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day23_part1(puzzle_input):
    pass


def aoc2019_day23_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day24_part1(puzzle_input):
    pass


def aoc2019_day24_part2(puzzle_input):
    pass


####################################################################################################


def aoc2019_day25_part1(puzzle_input):
    pass


def aoc2019_day25_part2(puzzle_input):
    pass



