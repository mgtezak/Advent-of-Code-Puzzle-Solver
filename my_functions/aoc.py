from inspect import getsource
from time import time

from my_functions.db import get_puzzle_input
from my_functions.solutions.aoc2015 import *
from my_functions.solutions.aoc2016 import *
from my_functions.solutions.aoc2017 import *
from my_functions.solutions.aoc2018 import *
from my_functions.solutions.aoc2019 import *
from my_functions.solutions.aoc2020 import *
from my_functions.solutions.aoc2021 import *
from my_functions.solutions.aoc2022 import *
from my_functions.solutions.aoc2023 import *


def solve(year, day, part):
    start = time()
    f = function_dict[f"aoc{year}_day{day}_part{part}"]
    puzzle_input = get_puzzle_input(year, day)
    solution = f(puzzle_input)
    runtime = time() - start
    return solution, runtime


def get_source_code(year, day, part):
    f = function_dict[f"aoc{year}_day{day}_part{part}"]
    return getsource(f)


function_dict = {
    'aoc2015_day1_part1': aoc2015_day1_part1,
    'aoc2015_day1_part2': aoc2015_day1_part2,
    'aoc2015_day2_part1': aoc2015_day2_part1,
    'aoc2015_day2_part2': aoc2015_day2_part2,
    'aoc2015_day3_part1': aoc2015_day3_part1,
    'aoc2015_day3_part2': aoc2015_day3_part2,
    'aoc2015_day4_part1': aoc2015_day4_part1,
    'aoc2015_day4_part2': aoc2015_day4_part2,
    'aoc2015_day5_part1': aoc2015_day5_part1,
    'aoc2015_day5_part2': aoc2015_day5_part2,
    'aoc2015_day6_part1': aoc2015_day6_part1,
    'aoc2015_day6_part2': aoc2015_day6_part2,
    'aoc2015_day7_part1': aoc2015_day7_part1,
    'aoc2015_day7_part2': aoc2015_day7_part2,
    'aoc2015_day8_part1': aoc2015_day8_part1,
    'aoc2015_day8_part2': aoc2015_day8_part2,
    'aoc2015_day9_part1': aoc2015_day9_part1,
    'aoc2015_day9_part2': aoc2015_day9_part2,
    'aoc2015_day10_part1': aoc2015_day10_part1,
    'aoc2015_day10_part2': aoc2015_day10_part2,
    # 'aoc2015_day11_part1': aoc2015_day11_part1,
    # 'aoc2015_day11_part2': aoc2015_day11_part2,
    # 'aoc2015_day12_part1': aoc2015_day12_part1,
    # 'aoc2015_day12_part2': aoc2015_day12_part2,
    # 'aoc2015_day13_part1': aoc2015_day13_part1,
    # 'aoc2015_day13_part2': aoc2015_day13_part2,
    # 'aoc2015_day14_part1': aoc2015_day14_part1,
    # 'aoc2015_day14_part2': aoc2015_day14_part2,
    # 'aoc2015_day15_part1': aoc2015_day15_part1,
    # 'aoc2015_day15_part2': aoc2015_day15_part2,
    # 'aoc2015_day16_part1': aoc2015_day16_part1,
    # 'aoc2015_day16_part2': aoc2015_day16_part2,
    # 'aoc2015_day17_part1': aoc2015_day17_part1,
    # 'aoc2015_day17_part2': aoc2015_day17_part2,
    # 'aoc2015_day18_part1': aoc2015_day18_part1,
    # 'aoc2015_day18_part2': aoc2015_day18_part2,
    # 'aoc2015_day19_part1': aoc2015_day19_part1,
    # 'aoc2015_day19_part2': aoc2015_day19_part2,
    # 'aoc2015_day20_part1': aoc2015_day20_part1,
    # 'aoc2015_day20_part2': aoc2015_day20_part2,
    # 'aoc2015_day21_part1': aoc2015_day21_part1,
    # 'aoc2015_day21_part2': aoc2015_day21_part2,
    # 'aoc2015_day22_part1': aoc2015_day22_part1,
    # 'aoc2015_day22_part2': aoc2015_day22_part2,
    # 'aoc2015_day23_part1': aoc2015_day23_part1,
    # 'aoc2015_day23_part2': aoc2015_day23_part2,
    # 'aoc2015_day24_part1': aoc2015_day24_part1,
    # 'aoc2015_day24_part2': aoc2015_day24_part2,
    # 'aoc2015_day25_part1': aoc2015_day25_part1,
    # 'aoc2015_day25_part2': aoc2015_day25_part2,
    'aoc2016_day1_part1': aoc2016_day1_part1,
    'aoc2016_day1_part2': aoc2016_day1_part2,
    'aoc2016_day2_part1': aoc2016_day2_part1,
    'aoc2016_day2_part2': aoc2016_day2_part2,
    'aoc2016_day3_part1': aoc2016_day3_part1,
    'aoc2016_day3_part2': aoc2016_day3_part2,
    'aoc2016_day4_part1': aoc2016_day4_part1,
    'aoc2016_day4_part2': aoc2016_day4_part2,
    'aoc2016_day5_part1': aoc2016_day5_part1,
    'aoc2016_day5_part2': aoc2016_day5_part2,
    'aoc2016_day6_part1': aoc2016_day6_part1,
    'aoc2016_day6_part2': aoc2016_day6_part2,
    'aoc2016_day7_part1': aoc2016_day7_part1,
    'aoc2016_day7_part2': aoc2016_day7_part2,
    'aoc2016_day8_part1': aoc2016_day8_part1,
    'aoc2016_day8_part2': aoc2016_day8_part2,
    'aoc2016_day9_part1': aoc2016_day9_part1,
    'aoc2016_day9_part2': aoc2016_day9_part2,
    'aoc2016_day10_part1': aoc2016_day10_part1,
    'aoc2016_day10_part2': aoc2016_day10_part2,
    # 'aoc2016_day11_part1': aoc2016_day11_part1,
    # 'aoc2016_day11_part2': aoc2016_day11_part2,
    # 'aoc2016_day12_part1': aoc2016_day12_part1,
    # 'aoc2016_day12_part2': aoc2016_day12_part2,
    # 'aoc2016_day13_part1': aoc2016_day13_part1,
    # 'aoc2016_day13_part2': aoc2016_day13_part2,
    # 'aoc2016_day14_part1': aoc2016_day14_part1,
    # 'aoc2016_day14_part2': aoc2016_day14_part2,
    # 'aoc2016_day15_part1': aoc2016_day15_part1,
    # 'aoc2016_day15_part2': aoc2016_day15_part2,
    # 'aoc2016_day16_part1': aoc2016_day16_part1,
    # 'aoc2016_day16_part2': aoc2016_day16_part2,
    # 'aoc2016_day17_part1': aoc2016_day17_part1,
    # 'aoc2016_day17_part2': aoc2016_day17_part2,
    # 'aoc2016_day18_part1': aoc2016_day18_part1,
    # 'aoc2016_day18_part2': aoc2016_day18_part2,
    # 'aoc2016_day19_part1': aoc2016_day19_part1,
    # 'aoc2016_day19_part2': aoc2016_day19_part2,
    # 'aoc2016_day20_part1': aoc2016_day20_part1,
    # 'aoc2016_day20_part2': aoc2016_day20_part2,
    # 'aoc2016_day21_part1': aoc2016_day21_part1,
    # 'aoc2016_day21_part2': aoc2016_day21_part2,
    # 'aoc2016_day22_part1': aoc2016_day22_part1,
    # 'aoc2016_day22_part2': aoc2016_day22_part2,
    # 'aoc2016_day23_part1': aoc2016_day23_part1,
    # 'aoc2016_day23_part2': aoc2016_day23_part2,
    # 'aoc2016_day24_part1': aoc2016_day24_part1,
    # 'aoc2016_day24_part2': aoc2016_day24_part2,
    # 'aoc2016_day25_part1': aoc2016_day25_part1,
    # 'aoc2016_day25_part2': aoc2016_day25_part2,
    'aoc2017_day1_part1': aoc2017_day1_part1,
    'aoc2017_day1_part2': aoc2017_day1_part2,
    'aoc2017_day2_part1': aoc2017_day2_part1,
    'aoc2017_day2_part2': aoc2017_day2_part2,
    'aoc2017_day3_part1': aoc2017_day3_part1,
    'aoc2017_day3_part2': aoc2017_day3_part2,
    'aoc2017_day4_part1': aoc2017_day4_part1,
    'aoc2017_day4_part2': aoc2017_day4_part2,
    'aoc2017_day5_part1': aoc2017_day5_part1,
    'aoc2017_day5_part2': aoc2017_day5_part2,
    'aoc2017_day6_part1': aoc2017_day6_part1,
    'aoc2017_day6_part2': aoc2017_day6_part2,
    'aoc2017_day7_part1': aoc2017_day7_part1,
    'aoc2017_day7_part2': aoc2017_day7_part2,
    'aoc2017_day8_part1': aoc2017_day8_part1,
    'aoc2017_day8_part2': aoc2017_day8_part2,
    'aoc2017_day9_part1': aoc2017_day9_part1,
    'aoc2017_day9_part2': aoc2017_day9_part2,
    'aoc2017_day10_part1': aoc2017_day10_part1,
    'aoc2017_day10_part2': aoc2017_day10_part2,
    # 'aoc2017_day11_part1': aoc2017_day11_part1,
    # 'aoc2017_day11_part2': aoc2017_day11_part2,
    # 'aoc2017_day12_part1': aoc2017_day12_part1,
    # 'aoc2017_day12_part2': aoc2017_day12_part2,
    # 'aoc2017_day13_part1': aoc2017_day13_part1,
    # 'aoc2017_day13_part2': aoc2017_day13_part2,
    # 'aoc2017_day14_part1': aoc2017_day14_part1,
    # 'aoc2017_day14_part2': aoc2017_day14_part2,
    # 'aoc2017_day15_part1': aoc2017_day15_part1,
    # 'aoc2017_day15_part2': aoc2017_day15_part2,
    # 'aoc2017_day16_part1': aoc2017_day16_part1,
    # 'aoc2017_day16_part2': aoc2017_day16_part2,
    # 'aoc2017_day17_part1': aoc2017_day17_part1,
    # 'aoc2017_day17_part2': aoc2017_day17_part2,
    # 'aoc2017_day18_part1': aoc2017_day18_part1,
    # 'aoc2017_day18_part2': aoc2017_day18_part2,
    # 'aoc2017_day19_part1': aoc2017_day19_part1,
    # 'aoc2017_day19_part2': aoc2017_day19_part2,
    # 'aoc2017_day20_part1': aoc2017_day20_part1,
    # 'aoc2017_day20_part2': aoc2017_day20_part2,
    # 'aoc2017_day21_part1': aoc2017_day21_part1,
    # 'aoc2017_day21_part2': aoc2017_day21_part2,
    # 'aoc2017_day22_part1': aoc2017_day22_part1,
    # 'aoc2017_day22_part2': aoc2017_day22_part2,
    # 'aoc2017_day23_part1': aoc2017_day23_part1,
    # 'aoc2017_day23_part2': aoc2017_day23_part2,
    # 'aoc2017_day24_part1': aoc2017_day24_part1,
    # 'aoc2017_day24_part2': aoc2017_day24_part2,
    # 'aoc2017_day25_part1': aoc2017_day25_part1,
    # 'aoc2017_day25_part2': aoc2017_day25_part2,
    'aoc2018_day1_part1': aoc2018_day1_part1,
    'aoc2018_day1_part2': aoc2018_day1_part2,
    'aoc2018_day2_part1': aoc2018_day2_part1,
    'aoc2018_day2_part2': aoc2018_day2_part2,
    'aoc2018_day3_part1': aoc2018_day3_part1,
    'aoc2018_day3_part2': aoc2018_day3_part2,
    'aoc2018_day4_part1': aoc2018_day4_part1,
    'aoc2018_day4_part2': aoc2018_day4_part2,
    'aoc2018_day5_part1': aoc2018_day5_part1,
    'aoc2018_day5_part2': aoc2018_day5_part2,
    'aoc2018_day6_part1': aoc2018_day6_part1,
    'aoc2018_day6_part2': aoc2018_day6_part2,
    'aoc2018_day7_part1': aoc2018_day7_part1,
    'aoc2018_day7_part2': aoc2018_day7_part2,
    'aoc2018_day8_part1': aoc2018_day8_part1,
    'aoc2018_day8_part2': aoc2018_day8_part2,
    'aoc2018_day9_part1': aoc2018_day9_part1,
    'aoc2018_day9_part2': aoc2018_day9_part2,
    'aoc2018_day10_part1': aoc2018_day10_part1,
    'aoc2018_day10_part2': aoc2018_day10_part2,
    # 'aoc2018_day11_part1': aoc2018_day11_part1,
    # 'aoc2018_day11_part2': aoc2018_day11_part2,
    # 'aoc2018_day12_part1': aoc2018_day12_part1,
    # 'aoc2018_day12_part2': aoc2018_day12_part2,
    # 'aoc2018_day13_part1': aoc2018_day13_part1,
    # 'aoc2018_day13_part2': aoc2018_day13_part2,
    # 'aoc2018_day14_part1': aoc2018_day14_part1,
    # 'aoc2018_day14_part2': aoc2018_day14_part2,
    # 'aoc2018_day15_part1': aoc2018_day15_part1,
    # 'aoc2018_day15_part2': aoc2018_day15_part2,
    # 'aoc2018_day16_part1': aoc2018_day16_part1,
    # 'aoc2018_day16_part2': aoc2018_day16_part2,
    # 'aoc2018_day17_part1': aoc2018_day17_part1,
    # 'aoc2018_day17_part2': aoc2018_day17_part2,
    # 'aoc2018_day18_part1': aoc2018_day18_part1,
    # 'aoc2018_day18_part2': aoc2018_day18_part2,
    # 'aoc2018_day19_part1': aoc2018_day19_part1,
    # 'aoc2018_day19_part2': aoc2018_day19_part2,
    # 'aoc2018_day20_part1': aoc2018_day20_part1,
    # 'aoc2018_day20_part2': aoc2018_day20_part2,
    # 'aoc2018_day21_part1': aoc2018_day21_part1,
    # 'aoc2018_day21_part2': aoc2018_day21_part2,
    # 'aoc2018_day22_part1': aoc2018_day22_part1,
    # 'aoc2018_day22_part2': aoc2018_day22_part2,
    # 'aoc2018_day23_part1': aoc2018_day23_part1,
    # 'aoc2018_day23_part2': aoc2018_day23_part2,
    # 'aoc2018_day24_part1': aoc2018_day24_part1,
    # 'aoc2018_day24_part2': aoc2018_day24_part2,
    # 'aoc2018_day25_part1': aoc2018_day25_part1,
    # 'aoc2018_day25_part2': aoc2018_day25_part2,
    'aoc2019_day1_part1': aoc2019_day1_part1,
    'aoc2019_day1_part2': aoc2019_day1_part2,
    'aoc2019_day2_part1': aoc2019_day2_part1,
    'aoc2019_day2_part2': aoc2019_day2_part2,
    'aoc2019_day3_part1': aoc2019_day3_part1,
    'aoc2019_day3_part2': aoc2019_day3_part2,
    'aoc2019_day4_part1': aoc2019_day4_part1,
    'aoc2019_day4_part2': aoc2019_day4_part2,
    'aoc2019_day5_part1': aoc2019_day5_part1,
    'aoc2019_day5_part2': aoc2019_day5_part2,
    'aoc2019_day6_part1': aoc2019_day6_part1,
    'aoc2019_day6_part2': aoc2019_day6_part2,
    'aoc2019_day7_part1': aoc2019_day7_part1,
    'aoc2019_day7_part2': aoc2019_day7_part2,
    'aoc2019_day8_part1': aoc2019_day8_part1,
    'aoc2019_day8_part2': aoc2019_day8_part2,
    'aoc2019_day9_part1': aoc2019_day9_part1,
    'aoc2019_day9_part2': aoc2019_day9_part2,
    'aoc2019_day10_part1': aoc2019_day10_part1,
    'aoc2019_day10_part2': aoc2019_day10_part2,
    # 'aoc2019_day11_part1': aoc2019_day11_part1,
    # 'aoc2019_day11_part2': aoc2019_day11_part2,
    # 'aoc2019_day12_part1': aoc2019_day12_part1,
    # 'aoc2019_day12_part2': aoc2019_day12_part2,
    # 'aoc2019_day13_part1': aoc2019_day13_part1,
    # 'aoc2019_day13_part2': aoc2019_day13_part2,
    # 'aoc2019_day14_part1': aoc2019_day14_part1,
    # 'aoc2019_day14_part2': aoc2019_day14_part2,
    # 'aoc2019_day15_part1': aoc2019_day15_part1,
    # 'aoc2019_day15_part2': aoc2019_day15_part2,
    # 'aoc2019_day16_part1': aoc2019_day16_part1,
    # 'aoc2019_day16_part2': aoc2019_day16_part2,
    # 'aoc2019_day17_part1': aoc2019_day17_part1,
    # 'aoc2019_day17_part2': aoc2019_day17_part2,
    # 'aoc2019_day18_part1': aoc2019_day18_part1,
    # 'aoc2019_day18_part2': aoc2019_day18_part2,
    # 'aoc2019_day19_part1': aoc2019_day19_part1,
    # 'aoc2019_day19_part2': aoc2019_day19_part2,
    # 'aoc2019_day20_part1': aoc2019_day20_part1,
    # 'aoc2019_day20_part2': aoc2019_day20_part2,
    # 'aoc2019_day21_part1': aoc2019_day21_part1,
    # 'aoc2019_day21_part2': aoc2019_day21_part2,
    # 'aoc2019_day22_part1': aoc2019_day22_part1,
    # 'aoc2019_day22_part2': aoc2019_day22_part2,
    # 'aoc2019_day23_part1': aoc2019_day23_part1,
    # 'aoc2019_day23_part2': aoc2019_day23_part2,
    # 'aoc2019_day24_part1': aoc2019_day24_part1,
    # 'aoc2019_day24_part2': aoc2019_day24_part2,
    # 'aoc2019_day25_part1': aoc2019_day25_part1,
    # 'aoc2019_day25_part2': aoc2019_day25_part2,
    'aoc2020_day1_part1': aoc2020_day1_part1,
    'aoc2020_day1_part2': aoc2020_day1_part2,
    'aoc2020_day2_part1': aoc2020_day2_part1,
    'aoc2020_day2_part2': aoc2020_day2_part2,
    'aoc2020_day3_part1': aoc2020_day3_part1,
    'aoc2020_day3_part2': aoc2020_day3_part2,
    'aoc2020_day4_part1': aoc2020_day4_part1,
    'aoc2020_day4_part2': aoc2020_day4_part2,
    'aoc2020_day5_part1': aoc2020_day5_part1,
    'aoc2020_day5_part2': aoc2020_day5_part2,
    'aoc2020_day6_part1': aoc2020_day6_part1,
    'aoc2020_day6_part2': aoc2020_day6_part2,
    'aoc2020_day7_part1': aoc2020_day7_part1,
    'aoc2020_day7_part2': aoc2020_day7_part2,
    'aoc2020_day8_part1': aoc2020_day8_part1,
    'aoc2020_day8_part2': aoc2020_day8_part2,
    'aoc2020_day9_part1': aoc2020_day9_part1,
    'aoc2020_day9_part2': aoc2020_day9_part2,
    'aoc2020_day10_part1': aoc2020_day10_part1,
    'aoc2020_day10_part2': aoc2020_day10_part2,
    'aoc2020_day11_part1': aoc2020_day11_part1,
    'aoc2020_day11_part2': aoc2020_day11_part2,
    'aoc2020_day12_part1': aoc2020_day12_part1,
    'aoc2020_day12_part2': aoc2020_day12_part2,
    'aoc2020_day13_part1': aoc2020_day13_part1,
    'aoc2020_day13_part2': aoc2020_day13_part2,
    'aoc2020_day14_part1': aoc2020_day14_part1,
    'aoc2020_day14_part2': aoc2020_day14_part2,
    'aoc2020_day15_part1': aoc2020_day15_part1,
    'aoc2020_day15_part2': aoc2020_day15_part2,
    # 'aoc2020_day16_part1': aoc2020_day16_part1,
    # 'aoc2020_day16_part2': aoc2020_day16_part2,
    # 'aoc2020_day17_part1': aoc2020_day17_part1,
    # 'aoc2020_day17_part2': aoc2020_day17_part2,
    # 'aoc2020_day18_part1': aoc2020_day18_part1,
    # 'aoc2020_day18_part2': aoc2020_day18_part2,
    # 'aoc2020_day19_part1': aoc2020_day19_part1,
    # 'aoc2020_day19_part2': aoc2020_day19_part2,
    # 'aoc2020_day20_part1': aoc2020_day20_part1,
    # 'aoc2020_day20_part2': aoc2020_day20_part2,
    # 'aoc2020_day21_part1': aoc2020_day21_part1,
    # 'aoc2020_day21_part2': aoc2020_day21_part2,
    # 'aoc2020_day22_part1': aoc2020_day22_part1,
    # 'aoc2020_day22_part2': aoc2020_day22_part2,
    # 'aoc2020_day23_part1': aoc2020_day23_part1,
    # 'aoc2020_day23_part2': aoc2020_day23_part2,
    # 'aoc2020_day24_part1': aoc2020_day24_part1,
    # 'aoc2020_day24_part2': aoc2020_day24_part2,
    # 'aoc2020_day25_part1': aoc2020_day25_part1,
    # 'aoc2020_day25_part2': aoc2020_day25_part2,
    'aoc2021_day1_part1': aoc2021_day1_part1,
    'aoc2021_day1_part2': aoc2021_day1_part2,
    'aoc2021_day2_part1': aoc2021_day2_part1,
    'aoc2021_day2_part2': aoc2021_day2_part2,
    'aoc2021_day3_part1': aoc2021_day3_part1,
    'aoc2021_day3_part2': aoc2021_day3_part2,
    'aoc2021_day4_part1': aoc2021_day4_part1,
    'aoc2021_day4_part2': aoc2021_day4_part2,
    'aoc2021_day5_part1': aoc2021_day5_part1,
    'aoc2021_day5_part2': aoc2021_day5_part2,
    'aoc2021_day6_part1': aoc2021_day6_part1,
    'aoc2021_day6_part2': aoc2021_day6_part2,
    'aoc2021_day7_part1': aoc2021_day7_part1,
    'aoc2021_day7_part2': aoc2021_day7_part2,
    'aoc2021_day8_part1': aoc2021_day8_part1,
    'aoc2021_day8_part2': aoc2021_day8_part2,
    'aoc2021_day9_part1': aoc2021_day9_part1,
    'aoc2021_day9_part2': aoc2021_day9_part2,
    'aoc2021_day10_part1': aoc2021_day10_part1,
    'aoc2021_day10_part2': aoc2021_day10_part2,
    'aoc2021_day11_part1': aoc2021_day11_part1,
    'aoc2021_day11_part2': aoc2021_day11_part2,
    'aoc2021_day12_part1': aoc2021_day12_part1,
    'aoc2021_day12_part2': aoc2021_day12_part2,
    'aoc2021_day13_part1': aoc2021_day13_part1,
    'aoc2021_day13_part2': aoc2021_day13_part2,
    'aoc2021_day14_part1': aoc2021_day14_part1,
    'aoc2021_day14_part2': aoc2021_day14_part2,
    # 'aoc2021_day15_part1': aoc2021_day15_part1,
    # 'aoc2021_day15_part2': aoc2021_day15_part2,
    # 'aoc2021_day16_part1': aoc2021_day16_part1,
    # 'aoc2021_day16_part2': aoc2021_day16_part2,
    # 'aoc2021_day17_part1': aoc2021_day17_part1,
    # 'aoc2021_day17_part2': aoc2021_day17_part2,
    # 'aoc2021_day18_part1': aoc2021_day18_part1,
    # 'aoc2021_day18_part2': aoc2021_day18_part2,
    # 'aoc2021_day19_part1': aoc2021_day19_part1,
    # 'aoc2021_day19_part2': aoc2021_day19_part2,
    # 'aoc2021_day20_part1': aoc2021_day20_part1,
    # 'aoc2021_day20_part2': aoc2021_day20_part2,
    # 'aoc2021_day21_part1': aoc2021_day21_part1,
    # 'aoc2021_day21_part2': aoc2021_day21_part2,
    # 'aoc2021_day22_part1': aoc2021_day22_part1,
    # 'aoc2021_day22_part2': aoc2021_day22_part2,
    # 'aoc2021_day23_part1': aoc2021_day23_part1,
    # 'aoc2021_day23_part2': aoc2021_day23_part2,
    # 'aoc2021_day24_part1': aoc2021_day24_part1,
    # 'aoc2021_day24_part2': aoc2021_day24_part2,
    # 'aoc2021_day25_part1': aoc2021_day25_part1,
    # 'aoc2021_day25_part2': aoc2021_day25_part2,
    'aoc2022_day1_part1': aoc2022_day1_part1,
    'aoc2022_day1_part2': aoc2022_day1_part2,
    'aoc2022_day2_part1': aoc2022_day2_part1,
    'aoc2022_day2_part2': aoc2022_day2_part2,
    'aoc2022_day3_part1': aoc2022_day3_part1,
    'aoc2022_day3_part2': aoc2022_day3_part2,
    'aoc2022_day4_part1': aoc2022_day4_part1,
    'aoc2022_day4_part2': aoc2022_day4_part2,
    'aoc2022_day5_part1': aoc2022_day5_part1,
    'aoc2022_day5_part2': aoc2022_day5_part2,
    'aoc2022_day6_part1': aoc2022_day6_part1,
    'aoc2022_day6_part2': aoc2022_day6_part2,
    'aoc2022_day7_part1': aoc2022_day7_part1,
    'aoc2022_day7_part2': aoc2022_day7_part2,
    'aoc2022_day8_part1': aoc2022_day8_part1,
    'aoc2022_day8_part2': aoc2022_day8_part2,
    'aoc2022_day9_part1': aoc2022_day9_part1,
    'aoc2022_day9_part2': aoc2022_day9_part2,
    'aoc2022_day10_part1': aoc2022_day10_part1,
    'aoc2022_day10_part2': aoc2022_day10_part2,
    # 'aoc2022_day11_part1': aoc2022_day11_part1,
    # 'aoc2022_day11_part2': aoc2022_day11_part2,
    # 'aoc2022_day12_part1': aoc2022_day12_part1,
    # 'aoc2022_day12_part2': aoc2022_day12_part2,
    # 'aoc2022_day13_part1': aoc2022_day13_part1,
    # 'aoc2022_day13_part2': aoc2022_day13_part2,
    # 'aoc2022_day14_part1': aoc2022_day14_part1,
    # 'aoc2022_day14_part2': aoc2022_day14_part2,
    # 'aoc2022_day15_part1': aoc2022_day15_part1,
    # 'aoc2022_day15_part2': aoc2022_day15_part2,
    # 'aoc2022_day16_part1': aoc2022_day16_part1,
    # 'aoc2022_day16_part2': aoc2022_day16_part2,
    # 'aoc2022_day17_part1': aoc2022_day17_part1,
    # 'aoc2022_day17_part2': aoc2022_day17_part2,
    # 'aoc2022_day18_part1': aoc2022_day18_part1,
    # 'aoc2022_day18_part2': aoc2022_day18_part2,
    # 'aoc2022_day19_part1': aoc2022_day19_part1,
    # 'aoc2022_day19_part2': aoc2022_day19_part2,
    # 'aoc2022_day20_part1': aoc2022_day20_part1,
    # 'aoc2022_day20_part2': aoc2022_day20_part2,
    # 'aoc2022_day21_part1': aoc2022_day21_part1,
    # 'aoc2022_day21_part2': aoc2022_day21_part2,
    # 'aoc2022_day22_part1': aoc2022_day22_part1,
    # 'aoc2022_day22_part2': aoc2022_day22_part2,
    # 'aoc2022_day23_part1': aoc2022_day23_part1,
    # 'aoc2022_day23_part2': aoc2022_day23_part2,
    # 'aoc2022_day24_part1': aoc2022_day24_part1,
    # 'aoc2022_day24_part2': aoc2022_day24_part2,
    # 'aoc2022_day25_part1': aoc2022_day25_part1,
    # 'aoc2022_day25_part2': aoc2022_day25_part2,
    # 'aoc2023_day1_part1': aoc2023_day1_part1,
    # 'aoc2023_day1_part2': aoc2023_day1_part2,
    # 'aoc2023_day2_part1': aoc2023_day2_part1,
    # 'aoc2023_day2_part2': aoc2023_day2_part2,
    # 'aoc2023_day3_part1': aoc2023_day3_part1,
    # 'aoc2023_day3_part2': aoc2023_day3_part2,
    # 'aoc2023_day4_part1': aoc2023_day4_part1,
    # 'aoc2023_day4_part2': aoc2023_day4_part2,
    # 'aoc2023_day5_part1': aoc2023_day5_part1,
    # 'aoc2023_day5_part2': aoc2023_day5_part2,
    # 'aoc2023_day6_part1': aoc2023_day6_part1,
    # 'aoc2023_day6_part2': aoc2023_day6_part2,
    # 'aoc2023_day7_part1': aoc2023_day7_part1,
    # 'aoc2023_day7_part2': aoc2023_day7_part2,
    # 'aoc2023_day8_part1': aoc2023_day8_part1,
    # 'aoc2023_day8_part2': aoc2023_day8_part2,
    # 'aoc2023_day9_part1': aoc2023_day9_part1,
    # 'aoc2023_day9_part2': aoc2023_day9_part2,
    # 'aoc2023_day10_part1': aoc2023_day10_part1,
    # 'aoc2023_day10_part2': aoc2023_day10_part2,
    # 'aoc2023_day11_part1': aoc2023_day11_part1,
    # 'aoc2023_day11_part2': aoc2023_day11_part2,
    # 'aoc2023_day12_part1': aoc2023_day12_part1,
    # 'aoc2023_day12_part2': aoc2023_day12_part2,
    # 'aoc2023_day13_part1': aoc2023_day13_part1,
    # 'aoc2023_day13_part2': aoc2023_day13_part2,
    # 'aoc2023_day14_part1': aoc2023_day14_part1,
    # 'aoc2023_day14_part2': aoc2023_day14_part2,
    # 'aoc2023_day15_part1': aoc2023_day15_part1,
    # 'aoc2023_day15_part2': aoc2023_day15_part2,
    # 'aoc2023_day16_part1': aoc2023_day16_part1,
    # 'aoc2023_day16_part2': aoc2023_day16_part2,
    # 'aoc2023_day17_part1': aoc2023_day17_part1,
    # 'aoc2023_day17_part2': aoc2023_day17_part2,
    # 'aoc2023_day18_part1': aoc2023_day18_part1,
    # 'aoc2023_day18_part2': aoc2023_day18_part2,
    # 'aoc2023_day19_part1': aoc2023_day19_part1,
    # 'aoc2023_day19_part2': aoc2023_day19_part2,
    # 'aoc2023_day20_part1': aoc2023_day20_part1,
    # 'aoc2023_day20_part2': aoc2023_day20_part2,
    # 'aoc2023_day21_part1': aoc2023_day21_part1,
    # 'aoc2023_day21_part2': aoc2023_day21_part2,
    # 'aoc2023_day22_part1': aoc2023_day22_part1,
    # 'aoc2023_day22_part2': aoc2023_day22_part2,
    # 'aoc2023_day23_part1': aoc2023_day23_part1,
    # 'aoc2023_day23_part2': aoc2023_day23_part2,
    # 'aoc2023_day24_part1': aoc2023_day24_part1,
    # 'aoc2023_day24_part2': aoc2023_day24_part2,
    # 'aoc2023_day25_part1': aoc2023_day25_part1,
    # 'aoc2023_day25_part2': aoc2023_day25_part2
}