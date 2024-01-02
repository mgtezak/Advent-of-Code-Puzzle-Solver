import re

def part2(puzzle_input):
    lines = puzzle_input.split('\n')
    cards = [1] * len(lines)
    regex = r':(.*?)\|(.*)'
    for i, line in enumerate(lines):
        nums = re.search(regex, line)
        win_nums = set(map(int, nums.group(1).split()))
        true_nums = set(map(int, nums.group(2).split()))
        n_matches = len(win_nums & true_nums)
        for j in range(i + 1, i + 1 + n_matches):
            cards[j] += cards[i]
    
    return sum(cards)