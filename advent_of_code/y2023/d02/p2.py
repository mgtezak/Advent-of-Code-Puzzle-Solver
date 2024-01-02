def part2(puzzle_input):
    power = 0
    for game in puzzle_input.split('\n'):
        game = game.split(': ')[1]
        max_number = {'red': 0, 'green': 0, 'blue': 0}
        for hand in game.split('; '):
            for subset in hand.split(', '):
                n, color = subset.split()
                max_number[color] = max(int(n), max_number[color])

        power += max_number['red'] * max_number['green'] * max_number['blue']

    return power