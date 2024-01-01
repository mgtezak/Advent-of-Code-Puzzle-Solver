def part1(puzzle_input):
        nums = list(map(int, puzzle_input.split(',')))
        nums[1], nums[2] = 12, 2
        for i in range(len(nums)):
            val = nums[i]
            if i % 4 == 0:  
                if val == 1:
                    nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
                elif val == 2:
                    nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
                elif val == 99:
                    break
        return nums[0]


def aoc2019_day2_part2(puzzle_input):
    instructions = list(map(int, puzzle_input.split(',')))

    def run_intcode(noun, verb):
        nums = instructions.copy()
        nums[1], nums[2] = noun, verb
        for i, val in enumerate(nums):
            if i % 4 == 0:  
                if val == 1:
                    nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
                elif val == 2:
                    nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
                elif val == 99:
                    break
        return nums[0]
            
    for noun in range(100):
        for verb in range(100):
            if run_intcode(noun, verb) == 19690720:
                return 100 * noun + verb