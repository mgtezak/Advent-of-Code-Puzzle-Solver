from collections import defaultdict
from utils.handle_puzzle_input import is_example_input

def part2(puzzle_input):

    if is_example_input(2019, 8, puzzle_input):
        width, height = 2, 2
    else:
        width, height = 25, 6

    pixels = puzzle_input
    n = width * height
    layers = []
    while pixels:
        layers.append(pixels[:n])
        pixels = pixels[n:]
    image = defaultdict(str)
    for layer in layers:
        for i, p in enumerate(layer):
            if p in ('0', '1') and not image[i]:
                image[i] = ' ' if p == '0' else '#'

    lines = [[] for _ in range(height)]
    for i in range(n):
        line = i // width
        lines[line].append(image[i])

    return '\n'.join(''.join(line) for line in lines)