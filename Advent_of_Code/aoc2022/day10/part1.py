def part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    cycle = row = signal_sum = 0
    x = 1
    image = ['' for _ in range(6)]
    for line in lines:
        for _ in range(len(line)):
            cycle += 1
            if cycle == 41:
                cycle -= 40
                row += 1
            if cycle == 20:
                signal_sum += x * (cycle + 40 * row)
            image[row] += '#' if x in range(cycle-2, cycle+1) else ' '
        if line[0] == 'addx':
            x += int(line[1])
    image = '\n' + '\n'.join(image)
    return signal_sum