def part1(puzzle_input):
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