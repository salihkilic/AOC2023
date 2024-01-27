from aoc_utilities.input_handling import TxtInput
import math

"""
This was a hard one! Had to learn some new math to solve it before 
the heat death of the universe.

Because the routes are basically cycles, you have to find the combination of
cycles that can be done in the least amount of steps. This is the least
common multiple of the number of steps per cycle.

This number is still too big to brute force, so we have to find a way to
calculate it mathematically instead of walking the graph.
"""


def parse_lines(lines):
    instruction_string = lines[0]
    instructions = [0 if letter == "L" else 1 for letter in instruction_string]
    maps = {}
    for item in lines[2:]:
        subitems = item.split(' ')
        origin = subitems[0]
        left = subitems[2][1:-1]
        right = subitems[3][:-1]
        maps[origin] = (left, right)
    return instructions, maps


def count_steps(current_node):
    steps = 0
    instructions, maps = parse_lines(lines)
    while current_node[2] != 'Z':
        for instruction in instructions:
            steps += 1
            current_node = maps[current_node][instruction]
    return steps


def main(lines):
    instructions, maps = parse_lines(lines)
    starting_nodes = [key for key in maps.keys() if key.endswith('A')]
    steps_per_node = [count_steps(node) for node in starting_nodes]
    return math.lcm(*steps_per_node)


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    print(f"Solution: {main(lines)}")
