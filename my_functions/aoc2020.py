import re


def aoc2020_day1_part1(puzzle_input):
    expenses = list(map(int, puzzle_input.split('\n')))
    for i, e1 in enumerate(expenses):
        for _, e2 in enumerate(expenses, start=i+1):
            if e1 + e2 == 2020:
                return e1 * e2


def aoc2020_day1_part2(puzzle_input):
    expenses = list(map(int, puzzle_input.split('\n')))
    for i, e1 in enumerate(expenses):
        for j, e2 in enumerate(expenses, start=i+1):
            for _, e3 in enumerate(expenses, start=j+1):
                if e1 + e2 + e3 == 2020:
                    return e1 * e2 * e3
                

####################################################################################################


def aoc2020_day2_part1(puzzle_input):
    pws = puzzle_input.split('\n')
    count = 0
    for pw in pws:
        count_range, letter, pw = pw.split()
        lower, upper = count_range.split('-')
        count_range = range(int(lower), int(upper)+1)
        letter = letter.strip(':')
        if pw.count(letter) in count_range:
            count += 1
    return count


def aoc2020_day2_part2(puzzle_input):
    pws = puzzle_input.split('\n')
    count = 0
    for pw in pws:
        indices, letter, pw = pw.split()
        i, j = map(lambda x: int(x)-1, indices.split('-'))
        letter = letter.strip(':')
        if (pw[i] == letter and not pw[j] == letter) or (not pw[i] == letter and pw[j] == letter):
            count += 1
    return count


####################################################################################################


def aoc2020_day3_part1(puzzle_input):
    slope = puzzle_input.split('\n')
    tree_count = 0
    j = 0
    l = len(slope[0])
    for row in slope:
        if row[j] == '#':
            tree_count += 1
        j = (j + 3) % l
    return tree_count


def aoc2020_day3_part2(puzzle_input):

    def count_trees(right=3, down=1):
        tree_count = 0
        j = 0
        l = len(slope[0])
        for i, row in enumerate(slope):
            if down == 2 and i%2:
                continue
            if row[j] == '#':
                tree_count += 1
            j = (j + right) % l
        return tree_count
    
    slope = puzzle_input.split('\n')
    instructions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    mul = 1
    for right, down in instructions:
        mul *= count_trees(right, down)
    return mul


####################################################################################################


def aoc2020_day4_part1(puzzle_input):
    passports = [p.split() for p in puzzle_input.split('\n\n')]
    valid = 0
    for p in passports:
        if len(p) == 8:
            valid += 1
        elif len(p) == 7 and not any(f.startswith('cid') for f in p):
            valid += 1
    return valid


def aoc2020_day4_part2(puzzle_input):
    passports = [p.split() for p in puzzle_input.split('\n\n')]
    valid = 0
    for p in passports:
        if len(p) < 7:
            continue
        if len(p) == 7 and any(f.startswith('cid') for f in p):
            continue

        fields = {f.split(':')[0]: f.split(':')[1] for f in p}

        if int(fields['byr']) not in range(1920, 2003):
            continue

        if int(fields['iyr']) not in range(2010, 2021):
            continue

        if int(fields['eyr']) not in range(2020, 2031):
            continue
        
        if fields['hgt'][-2:] not in ('cm', 'in'):
            continue
        if fields['hgt'][-2:] == 'cm' and int(fields['hgt'][:-2]) not in range(150, 194):
            continue
        if fields['hgt'][-2:] == 'in' and int(fields['hgt'][:-2]) not in range(59, 77):
            continue

        if not fields['hcl'].startswith('#') or len(fields['hcl']) != 7:
            continue
        if any(char not in '0123456789abcdef' for char in fields['hcl'][1:]):
            continue

        if fields['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        
        if len(fields['pid']) != 9:
            continue

        valid += 1

    return valid


####################################################################################################


def aoc2020_day5_part1(puzzle_input):

    boarding_passes = puzzle_input.split('\n')
    seat_ids = []

    for b in boarding_passes:
        row_partitioning = b[:7]
        col_partitioning = b[7:]

        # find row
        r_low, r_high = 0, 127
        for p in row_partitioning:
            if p == 'F':
                r_high = r_low + (r_high - r_low) // 2
            else:
                r_low = r_low + (r_high - r_low) // 2 + 1
        row = r_low
        
        # find col
        c_low, c_high = 0, 7         
        for p in col_partitioning:
            if p == 'L':
                c_high = c_low + (c_high - c_low) // 2
            else:
                c_low = c_low + (c_high - c_low) // 2 + 1
        col = c_low

        seat_ids.append(row * 8 + col)

    return max(seat_ids)


def aoc2020_day5_part2(puzzle_input):

    boarding_passes = puzzle_input.split('\n')
    occupied = {i: [] for i in range(128)}

    for b in boarding_passes:
        row_partitioning = b[:7]
        col_partitioning = b[7:]

        # find row
        r_low, r_high = 0, 127
        for p in row_partitioning:
            if p == 'F':
                r_high = r_low + (r_high - r_low) // 2
            else:
                r_low = r_low + (r_high - r_low) // 2 + 1
        row = r_low
        
        # find col
        c_low, c_high = 0, 7         
        for p in col_partitioning:
            if p == 'L':
                c_high = c_low + (c_high - c_low) // 2
            else:
                c_low = c_low + (c_high - c_low) // 2 + 1
        col = c_low
        occupied[row].append(col)

    middle_of_plane = False

    for row in occupied:
        if len(occupied[row]) == 8:
            middle_of_plane = True

        elif middle_of_plane and len(occupied[row]) < 8:
            my_seat_id = row * 8 + [i for i in range(8) if i not in occupied[row]].pop()
            break

    return my_seat_id


####################################################################################################


def aoc2020_day6_part1(puzzle_input):

    groups = [g.split('\n') for g in puzzle_input.split('\n\n')]
    any_yes_sum = 0 # part 1

    for g in groups:
        any_yes = set(q for p in g for q in p)
        any_yes_sum += len(any_yes)

    return any_yes_sum


def aoc2020_day6_part2(puzzle_input):

    groups = [g.split('\n') for g in puzzle_input.split('\n\n')]
    all_yes_sum = 0

    for g in groups:
        all_yes = set(q for q in g[0] if all(q in g[i] for i, _ in enumerate(g)))
        all_yes_sum += len(all_yes)

    return all_yes_sum


####################################################################################################

# 1 TOO HIGH answer: 378
def aoc2020_day7_part1(puzzle_input):

    lines = puzzle_input.split('\n')
    bags = {}

    for line in lines[:]:
        (_, outer), *content = re.findall(r'(\d*) ?(\w+ \w+) bag', line)
        if content[0][0]:
            bags[outer] = {inner: int(n) for n, inner in content}
        else:
            bags[outer] = []

    content = {'shiny gold'}

    while True:
        new = set()
        for inner in content:
            new |= {outer for outer in bags if inner in bags[outer]}

        if new.difference(content):
            content |= new
        else:
            return len(content) - 1   # need to subtract shiny gold bag


def aoc2020_day7_part2(puzzle_input):

    lines = puzzle_input.split('\n')
    bags = {}

    for line in lines[:]:
        (_, outer), *content = re.findall(r'(\d*) ?(\w+ \w+) bag', line)
        if content[0][0]:
            bags[outer] = {inner: int(n) for n, inner in content}
        else:
            bags[outer] = []

    total = 0
    queue = [('shiny gold', 1)]

    while queue:
        outer, n = queue.pop()
        content = bags[outer]
        for inner in content:
            n_inner = n * bags[outer][inner]
            queue.append((inner, n_inner))
            total += n_inner

    return total


####################################################################################################


def aoc2020_day8_part1(puzzle_input):
    ins = [(i.split()[0], int(i.split()[1])) for i in puzzle_input.split('\n')]
    accumulator = 0
    unvisited = [i for i in range(len(ins))]
    i = 0
    while i in unvisited:
        unvisited.remove(i)
        op, arg = ins[i]
        if op == 'acc':
            accumulator += arg
        if op == 'jmp':
            i += arg
        else:
            i += 1
    return accumulator


def aoc2020_day8_part2(puzzle_input):
    instructions = [(i.split()[0], int(i.split()[1])) for i in puzzle_input.split('\n')]

    def run_instructions(ins):
        accumulator = 0
        unvisited = [i for i in range(len(ins))]
        i = 0
        while i in unvisited:
            unvisited.remove(i)
            op, arg = ins[i]
            if op == 'acc':
                accumulator += arg
            if op == 'jmp':
                i += arg
            else:
                i += 1

        if i == len(ins):
            return accumulator

    def generate_new_instructions():
        for i, (op, arg) in enumerate(instructions):
            if op == 'nop':
                yield instructions[:i] + [('jmp', arg)] + instructions[i+1:]
            elif op == 'jmp':
                yield instructions[:i] + [('nop', arg)] + instructions[i+1:]

    for ins in generate_new_instructions():
        if (result := run_instructions(ins)):
            return result


####################################################################################################


def aoc2020_day9_part1(puzzle_input):
    
    def validate_num(n, prev):
        for i, n1 in enumerate(prev):
            for _, n2 in enumerate(prev[i+1:]):
                if n == n1 + n2:
                    return True
                
    nums = list(map(int, puzzle_input.split('\n')))
    for i, n in enumerate(nums):
        if i < 25:
            continue
        prev = nums[i-25:i]
        if not validate_num(n, prev):
            return n
        

def aoc2020_day9_part2(puzzle_input):

    def validate_num(n, prev):
        for i, n1 in enumerate(prev):
            for _, n2 in enumerate(prev[i+1:]):
                if n == n1 + n2:
                    return True
                
    nums = list(map(int, puzzle_input.split('\n')))
    for i, n in enumerate(nums):
        if i < 25:
            continue
        prev = nums[i-25:i]
        if not validate_num(n, prev):
            invalid_num = n
            break

    for i in range(nums.index(invalid_num)):
        j = i + 1
        while sum(nums[i:j]) < invalid_num:
            j += 1
        if sum(nums[i:j]) == invalid_num:
            return min(nums[i:j]) + max(nums[i:j])
    

####################################################################################################


def aoc2020_day10_part1(puzzle_input):
    adapters = sorted(map(int, puzzle_input.split('\n')))
    joltage = 0
    jolt_diff = [3]
    for a in adapters:
        jolt_diff.append(a - joltage)
        joltage = a
    return jolt_diff.count(1) * jolt_diff.count(3)


def aoc2020_day10_part2(puzzle_input):
    adapters = sorted(map(int, puzzle_input.split('\n')))
    n_paths = {0: 1}  # n_paths[a] = number of distinct paths to reach adapter a
    for a in adapters:
        n_paths[a] = sum(n_paths.get(a-x, 0) for x in range(1, 4))
    return n_paths[max(adapters)]


####################################################################################################


def aoc2020_day11_part1(puzzle_input):
    pass


def aoc2020_day11_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day12_part1(puzzle_input):
    pass


def aoc2020_day12_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day13_part1(puzzle_input):
    pass


def aoc2020_day13_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day14_part1(puzzle_input):
    pass


def aoc2020_day14_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day15_part1(puzzle_input):
    pass


def aoc2020_day15_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day16_part1(puzzle_input):
    pass


def aoc2020_day16_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day17_part1(puzzle_input):
    pass


def aoc2020_day17_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day18_part1(puzzle_input):
    pass


def aoc2020_day18_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day19_part1(puzzle_input):
    pass


def aoc2020_day19_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day20_part1(puzzle_input):
    pass


def aoc2020_day20_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day21_part1(puzzle_input):
    pass


def aoc2020_day21_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day22_part1(puzzle_input):
    pass


def aoc2020_day22_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day23_part1(puzzle_input):
    pass


def aoc2020_day23_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day24_part1(puzzle_input):
    pass


def aoc2020_day24_part2(puzzle_input):
    pass


####################################################################################################


def aoc2020_day25_part1(puzzle_input):
    pass


def aoc2020_day25_part2(puzzle_input):
    pass



