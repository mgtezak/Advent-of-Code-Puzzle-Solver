from collections import deque
from utils.handle_puzzle_input import is_example_input


def part1(puzzle_input):
    grid = [list(row) for row in puzzle_input.split('\n')]
    n, m = len(grid), len(grid[0])
    for x, row in enumerate(grid):
        if 'S' in row:
            start = (x, row.index('S'))
            break

    if is_example_input(2023, 21, puzzle_input):
        target = 6
    else:
        target = 64 

    visited = set()
    queue = deque([start])
    total = 0
    for step in range(1, target+1):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if i < 0 or j < 0 or i == n or j == m or (i, j) in visited or grid[i][j] == '#':
                    continue
                visited.add((i, j))
                queue.append((i, j))
                if step % 2 == 0:
                    total += 1

    return total