def part1(puzzle_input):

    def get_distance(r):
        name, speed, fly_secs, rest_secs = r[0], int(r[3]), int(r[6]), int(r[-2])
        full_fly_cycles = (2503 // (fly_secs + rest_secs)) * fly_secs
        partial_fly_cycle = min(fly_secs, 2503 % (fly_secs + rest_secs))
        full_distance = (full_fly_cycles + partial_fly_cycle) * speed
        return (full_distance, name)

    reindeers = [line.split() for line in puzzle_input.split('.\n')]
    winners = sorted([get_distance(r) for r in reindeers])
    winners = [r for r in winners if r[0] == winners[-1][0]] ### select multiple if multiple in first place
    return winners[0][0]