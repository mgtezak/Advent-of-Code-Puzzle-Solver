def part1(puzzle_input):

    sensors = {}
    for line in puzzle_input.split('\n'):
        x1, y1, x2, y2 = map(int, [line.split()[i].strip('xy=,:') for i in (2,3,8,9)])
        sensors[(x1, y1)] = abs(x1 - x2) + abs(y1 - y2)

    coverage = set()
    for x, y in sensors:
        distance_to_row = abs(2_000_000 - y)
        leftover = sensors[(x, y)] - distance_to_row
        for i in range(-leftover, leftover):
            coverage.add(x + i)

    return len(coverage)