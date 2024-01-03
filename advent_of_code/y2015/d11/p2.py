import string
import re


def part2(puzzle_input):

    def is_valid(pw):
        '''check whether pw has two non-overlapping repeated letters and an alphabetical straight'''
        if len(re.findall(r'([a-z])\1', pw)) >= 2 and any(pw[i:i+3] in alphabet for i in range(6)):
            return True
        
    def increment(pw):
        '''alphabetically increments pw from right to left'''
        pw = list(pw)
        for i in range(7, -1, -1):
            next_index = (altered_alphabet.index(pw[i]) + 1) % 23
            pw[i] = altered_alphabet[next_index]
            if pw[i] != 'a':
                break
        return ''.join(pw)

    alphabet = string.ascii_lowercase
    altered_alphabet = re.sub('[iol]', '', alphabet) # removing forbidden letters

    pw = puzzle_input
    for _ in range(2):
        while not is_valid(pw):
            pw = increment(pw)
        pw = increment(pw)

    return pw