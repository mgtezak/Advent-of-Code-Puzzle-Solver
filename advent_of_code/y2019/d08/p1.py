from utils.handle_puzzle_input import is_example_input

def part1(puzzle_input):

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
        
    least_zeros = min((layer.count('0'), layer) for layer in layers)[1]
    return least_zeros.count('1') * least_zeros.count('2')