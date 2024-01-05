import json
from pathlib import Path
import re
import shutil

# Local imports
from utils.handle_puzzle_data import get_puzzle_dir_path
from utils.handle_puzzle_input import get_example_inputs
from utils.handle_solutions import get_solving_func
from utils.toolbox import solution_exists


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

    path = get_puzzle_dir_path(year, day) / 'example_input.json'
    if not overwrite and path.exists():
        raise FileExistsError("Set overwrite to True.")

    tuple_list = []
    for example in input_list:
        print(f'Input: \n{example}\n')
        compatibility = check_part_compatibility(year, day, example)
        print(f'Compatibility: {compatibility}\n\n')
        assert compatibility > 0, "Incompatible with either part"
        tuple_list.append(example, compatibility)

    path.write_text(json.dumps(tuple_list, indent=2))



def update_compatibility(year: int, day: int, idx: int, new_value: int) -> None:
    """Useful in cases where the example input is compatible with both parts, when it should 
    actually only work with one of them.
    """
    input_list = get_example_inputs(year, day)
    input_list[idx] = (input_list[idx][0], new_value)
    print(f'Puzzle input:\n{input_list[idx][0]}\n\nUpdated compatibility: {new_value}')



def copy_solution_scripts(year: int, day: int) -> None:
    """Copies solution scripts from the original repo."""

    source_file = Path(f'../../Advent_of_Code/{year}/Day_{day:02}.py')
    scripts = extract_part_scripts(source_file.read_text())
    parts = (1, 2) if day < 25 else (1,)
    destination_dir = get_puzzle_dir_path(year, day)    

    for part in parts:
        destination_file = destination_dir / f'p{part}.py'
        destination_file.write_text(scripts[part])



def extract_part_scripts(original_script: str) -> dict[int, str]:
    """Extracts both script parts from my original script including the approriate import statements.
    Strips away the print statements and the reading of the puzzle input.
    """
    import_regex = r'(?:(import \w+ as( \w+))|(import( \w+))|(from \w* import( \w+)))'
    import_lines = re.findall(import_regex, original_script)

    imports = {}
    for line1, i1, line2, i2, line3, i3 in import_lines:
        if line1:
            imports[i1] = line1
        elif line2:
            imports[i2] = line2
        elif line3:
            imports[i3] = line3

    func_regex = r'(def part(1|2).*?    return [^\n]+)'
    func_lines = re.findall(func_regex, original_script, re.DOTALL)
    scripts = {1: '', 2: ''}

    for f, part in func_lines:
        part = int(part)
        has_imports = False
        for i, line in imports.items():
            if i in f:
                scripts[part] += line + '\n'
                has_imports = True

        if has_imports:
            scripts[part] += '\n'

        scripts[part] += f

    return scripts



def create_description_template(year: int, day: int) -> None:
    """Upload a puzzle description, to be viewed on the main page."""

    path =  get_puzzle_dir_path(year, day) / 'description.txt'
    if path.exists():
        print('Description exists already')
        return
    
    template = '#### Part 1 task:\n\n\n\n#### My approach:\n\n\n\n___\n\n\n\n#### Part 2 task:\n\n\n\n#### My approach:\n\n\n\n___'
    path.write_text(template)



def upload_new_puzzle(year: int, day: int, input_list: list[str] | None = None, overwrite: bool = False) -> None:
    """Copies solution scripts, creates description template and if available adds example inputs."""

    if not overwrite and solution_exists(year, day):
        raise FileExistsError("Set overwrite to True")

    copy_solution_scripts(year, day)
    create_description_template(year, day)
    if input_list:
        add_example_inputs(year, day, input_list, True)



def delete_puzzle_dir(year: int, day: int) -> None:
    """Deletes a puzzle directory."""

    shutil.rmtree(get_puzzle_dir_path(year, day))