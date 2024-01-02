def part2(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    pos = [[] for _ in range(9)]
    start = lines[:9]
    for j in range(8, -1, -1):
        for i in range(1, len(start[j]), 4):
            if start[j][i].isupper():
                pos[int(i/4)].append(start[j][i])   

    instructions = [list(map(int, line.split()[1:6:2])) for line in lines[10:]]
    for q, f, t in instructions:                      # q: quantity, f: from, t: to
        crates = pos[f-1][-q:]                        # identify q crates at f
        pos[f-1] = pos[f-1][:-q]                      # remove them at f
        pos[t-1] += crates                            # add them at t
    return ''.join(crate[-1] for crate in pos)        # return upper crate of each position