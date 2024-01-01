from heapq import heappop, heappush

def part2(puzzle_input):
    grid = [[int(d) for d in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    # tuple: (heat-loss, x-coord, y-coord, length-of-current-run, x-direction, y-direction)
    q = [(0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 1, 0)] 
    visited = set()
    while q:
        loss, x, y, k, dx, dy = heappop(q)

        if x == m-1 and y == n-1:
            if k < 4:
                continue
            break

        if (x, y, k, dx, dy) in visited:
            continue
    
        visited.add((x, y, k, dx, dy))

        for new_dx, new_dy in directions:
            straight = (new_dx == dx and new_dy == dy)
            new_x, new_y = x + new_dx, y + new_dy

            if any((new_dx == -dx and new_dy == -dy,
                    k == 10 and straight,
                    k < 4 and not straight,
                    new_x < 0, new_y < 0, 
                    new_x == m, new_y == n)):
                continue

            new_k = k + 1 if straight else 1
            heappush(q, (loss + grid[new_x][new_y], new_x, new_y, new_k, new_dx, new_dy))

    return loss