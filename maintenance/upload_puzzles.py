import json
import os
import shutil

# Local imports
from utils.handle_puzzle_input import get_example_inputs
from utils.handle_solutions import get_solving_func


def check_part_compatibility(year: int, day: int, example_input: str) -> int:
    """Returns 1 if the example input is only compatible with part 1, 2 if it's only compatible 
    with part 2 and 3 if it's compatible with both parts, or only part 1 exists (day 25).
    """
    
    if day < 25:
        compatibility = 0
        parts = (1, 2)
    else:
        compatibility = 2
        parts = (1,)

    for part in parts:
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



def update_compatibility(year: int, day: int, idx: int, new_value: int) -> None:
    """Useful in cases where the example input is compatible with both parts, when it should 
    actually only work with one of them.
    """
    idx = str(idx)
    input_dict = get_example_inputs(year, day)
    input_dict[idx] = (input_dict[idx][0], new_value)
    print(f'Puzzle input:\n{input_dict[idx][0]}\n\nUpdated compatibility: {new_value}')



def copy_solution_scripts(year: int, day: int) -> None:
    year_path = f'advent_of_code/y{year}'
    day_path = year_path + f'/d{day:02}'
    os.makedirs(day_path)
    
    parts = (1, 2) if day < 25 else (1,)
    for part in parts:
        source_file = f''
        destination_file = day_path + f'/p{part}.py'
        shutil.copy(source_file, destination_file)


def upload_description(year: int, day: int, description: str, overwrite: bool = False) -> None:
    """Upload a puzzle description, to be viewed on the main page."""

    path = f'advent_of_code/y{year}/d{day:02}/description.txt'
    if os.path.exists(path) and overwrite == False:
        raise FileExistsError("Set overwrite to true.")
    
    with open(path, 'w') as f:
        f.write(description)