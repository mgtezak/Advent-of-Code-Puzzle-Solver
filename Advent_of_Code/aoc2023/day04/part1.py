import re

def part1(puzzle_input):
    regex = r':(.*?)\|(.*)'
    points = 0
    for line in puzzle_input.split('\n'):
        nums = re.search(regex, line)
        win_nums = set(map(int, nums.group(1).split()))
        true_nums = set(map(int, nums.group(2).split()))
        n_matches = len(win_nums & true_nums)
        if n_matches:
            points += 2 ** (n_matches - 1)

    return points