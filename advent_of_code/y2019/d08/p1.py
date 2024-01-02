def part1(puzzle_input):
    pixels = puzzle_input
    n = 25 * 6
    layers = []
    while pixels:
        layers.append(pixels[:n])
        pixels = pixels[n:]
    least_zeros = min((layer.count('0'), layer) for layer in layers)[1]
    return least_zeros.count('1') * least_zeros.count('2')