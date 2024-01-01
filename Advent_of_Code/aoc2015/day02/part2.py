def part2(puzzle_input):
    lines = [list(map(int, line.split('x'))) for line in puzzle_input.split('\n')]
    total_ribbon = 0
    for line in lines:
        edges = [line[0], line[1], line[2]]
        total_ribbon += np.prod(edges)
        edges.remove(max(edges))
        total_ribbon += sum(edges * 2)
    return total_ribbon