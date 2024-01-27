from aoc_utilities.input_handling import TxtInput

"""
Do not try this, it will take a *very* long time.
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

def is_solution(current_nodes) -> bool:
    nodes_end_with_z = [node for node in current_nodes if node.endswith('Z')]
    return len(current_nodes) == len(nodes_end_with_z)

def main(lines):
    steps = 0
    instructions, maps = parse_lines(lines)
    current_nodes = [key for key in maps.keys() if key.endswith('A')]

    while not is_solution(current_nodes):
        for instruction in instructions:
            steps += 1
            new_nodes = []
            for node in current_nodes:
                new_nodes.append(maps[node][instruction])
            print(f"Step: {steps} -- Current nodes: {current_nodes} -- New nodes: {new_nodes}")
            current_nodes = new_nodes
    return steps


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    print(f"Solution: {main(lines)}")
