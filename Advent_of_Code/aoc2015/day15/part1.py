import random
import re


def part1(puzzle_input):

    def get_score(recipe: list) -> int:
        '''calculate total score of cookie'''
        capacity = sum([recipe[i] * lines[i][0] for i in range(len(lines))])
        durability = sum([recipe[i] * lines[i][1] for i in range(len(lines))])
        flavor = sum([recipe[i] * lines[i][2] for i in range(len(lines))])
        texture = sum([recipe[i] * lines[i][3] for i in range(len(lines))])
        score = capacity * durability * flavor * texture
        return score

    def make_child_recipe(recipe: list) -> list:
        '''alter recipe by randomly adding and removing 10 teaspoons of ingredients'''
        child = recipe.copy()
        for _ in range(10):
            child[random.randint(0, 3)] += 1
        for _ in range(10):
            child[random.randint(0, 3)] -= 1
        return child

    def improve_recipe(parent: list) -> list:
        '''compare parent recipe and 5 of its children and return the one with the best score'''
        recipes =  [parent] + [make_child_recipe(parent) for _ in range(5)]
        best_recipe = max(recipes, key=lambda r: get_score(r))
        return best_recipe


    lines = [list(map(int, re.findall('(-?\d)', line))) for line in puzzle_input.split('\n')]
    recipe = [30, 30, 20, 20]
    for _ in range(100):
        recipe = improve_recipe(recipe)

    return get_score(recipe)