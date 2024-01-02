import re

def part1(puzzle_input):
    times, distances = puzzle_input.split('\n')
    times = list(map(int, re.findall('\d+', times)))
    distances = list(map(int, re.findall('\d+', distances)))
    total = 1
    for t, d in zip(times, distances):
        wins = 0
        speed = 0
        for acceleration in range(1, t):
            speed += 1
            travelled = (t-acceleration) * speed
            if travelled > d:
                wins += (travelled > d)
            elif wins:
                break

        total *= wins
    
    return total