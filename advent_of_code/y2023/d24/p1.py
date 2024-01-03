from itertools import combinations
from utils.handle_puzzle_input import is_example_input


def part1(puzzle_input):
    hailstones = []
    for line in puzzle_input.split('\n'):
        nums = line.replace('@', ',').split(',')
        hailstones.append(tuple(map(int, nums)))

    if is_example_input(2023, 24, puzzle_input):
        lo, hi = 7, 27
    else:
        lo, hi = 2e14, 4e14
        
    total = 0
    for h1, h2 in combinations(hailstones, 2):
        x1, y1, _, dx1, dy1, _ = h1
        x2, y2, _, dx2, dy2, _ = h2
        m1 = dy1 / dx1
        m2 = dy2 / dx2
        if m1 == m2:   # they move in parallel and never meet
            continue
        b1 = y1 - m1*x1
        b2 = y2 - m2*x2
        x = (b2-b1) / (m1-m2)
        y = m1*x + b1
        if all((lo <= x <= hi,  # x and y need to be in range
                lo <= y <= hi,
                (x > x1 and dx1 > 0) or (x < x1 and dx1 < 0),  # itersection needs to happen in the future
                (x > x2 and dx2 > 0) or (x < x2 and dx2 < 0))):
            total += 1

    return total