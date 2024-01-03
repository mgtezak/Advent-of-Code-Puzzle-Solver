import json
import os

# Local imports
from utils.handle_puzzle_input import get_example_inputs
from utils.handle_solutions import get_solving_func
from utils.toolbox import get_parts


def check_part_compatibility(year: int, day: int, example_input: str) -> int:
    """Returns 1 if the example input is only compatible with part 1, 2 if it's only compatible 
    with part 2 and 3 if it's compatible with both parts, or only part 1 exists (day 25).
    """
    
    compatibility = 0 if day < 25 else 2
    for part in get_parts(year, day):
        solving_func = get_solving_func(year, day, part)
        try:
            solution = solving_func(example_input)
            print(f'Solution part {part}: {solution}')
            compatibility += part
        except:
            pass

    return compatibility



def add_example_inputs(year: int, day: int, input_list: list[str], overwrite: bool = False) -> None:
    """Adds example input for a given year and day to a json file."""

    path = f'advent_of_code/y{year}/d{day:02}/example_input.json'
    if not overwrite and os.path.exists(path):
        raise ValueError(f"{year}-{day} already has example puzzle input.")

    input_dict = {}
    for i, example in enumerate(input_list):
        print(f'Input: \n{example}\n')
        compatibility = check_part_compatibility(year, day, example)
        print(f'Compatibility: {compatibility}\n\n')
        assert compatibility > 0, "Incompatible with either part"
        input_dict[i] = (example, compatibility)

    with open(path, 'w') as f:
        json.dump(input_dict, f, indent=2)
