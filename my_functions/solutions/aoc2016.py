import string
import hashlib
import re
import numpy as np



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
        if hash[:5] == '00000':
            pw += hash[5]
        i += 1
    return pw


def aoc2016_day5_part2(puzzle_input):
    pw = {}
    i = 1
    while len(pw) < 8:
        hash = hashlib.md5((puzzle_input + str(i)).encode()).hexdigest()
        if hash[:5] == '00000' and hash[5].isnumeric():
            index = int(hash[5])
            if index in range(8) and index not in pw:                    
                pw[index] = hash[6]
        i += 1
    pw = ''.join(pw[i] for i in range(8))


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

    formatted = ''
    for row in display:
        row = ['#' if element == 1 else ' ' for element in row]
        formatted += '\n' + ''.join(row)
    return formatted


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
                return length
                
        return decompress(puzzle_input)


####################################################################################################


def aoc2016_day10_part1(puzzle_input):
    pass


def aoc2016_day10_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day11_part1(puzzle_input):
    pass


def aoc2016_day11_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day12_part1(puzzle_input):
    pass


def aoc2016_day12_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day13_part1(puzzle_input):
    pass


def aoc2016_day13_part2(puzzle_input):
    pass


####################################################################################################


def aoc2016_day14_part1(puzzle_input):
    pass


def aoc2016_day14_part2(puzzle_input):
    pass


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



