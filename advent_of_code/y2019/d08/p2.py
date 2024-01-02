from collections import defaultdict

def part2(puzzle_input):
    pixels = puzzle_input
    n = 25 * 6
    layers = []
    while pixels:
        layers.append(pixels[:n])
        pixels = pixels[n:]
    image = defaultdict(str)
    for layer in layers:
        for i, p in enumerate(layer):
            if p in ('0', '1') and not image[i]:
                image[i] = ' ' if p == '0' else '#'

    lines = [[] for _ in range(6)]
    for i in range(n):
        line = i // 25
        lines[line].append(image[i])

    return '\n'.join(''.join(line) for line in lines)