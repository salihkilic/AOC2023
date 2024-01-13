from aoc_utilities.input_handling import TxtInput
from collections import defaultdict

directions = [(0, -1), (0, 1), (-1, 0), (1, 0),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]


def check_neighbours(location: tuple[int, int], grid: list[str]):
    for direction in directions:
        try:
            y_index = location[0] + direction[0]
            x_index = location[1] + direction[1]
            item = grid[y_index][x_index]
            if item == '*':
                return (y_index, x_index)
        except IndexError:
            pass
    return False


def main(lines):
    confirmed_numbers = []
    for y_index, line in enumerate(lines):
        current_number = ""
        gear_index = False
        for x_index, char in enumerate(line):
            if char.isdigit():
                # If char is digit, we keep going for the full number
                current_number += char
                if not gear_index:
                    gear_index = check_neighbours((y_index, x_index), lines)
            else:
                # If char is not digit, we check if we have a confirmed number
                if gear_index:
                    confirmed_numbers.append((int(current_number), gear_index))
                gear_index = False
                current_number = ""
            # We need to check the last number in the line when there's no more chars
            if x_index == len(line) - 1 and gear_index:
                confirmed_numbers.append((int(current_number), gear_index))

    # Now we need to match the numbers to their gears
    potential_ratios = defaultdict(list)
    for number, coordinates in confirmed_numbers:
        potential_ratios[coordinates].append(number)

    # Filter out the gears that have more than 2 numbers
    ratios = [ratio[0] * ratio[1] for ratio in potential_ratios.values() if len(ratio) == 2]

    return sum(ratios)


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    result = main(lines)
    print(result)

    print(f"Solution: {result}")

"""
- Find numbers and check neighbours for each number
- If neighbour is *, add * to number tuple
- Get all stars and their neighbour numbers -> if 2 numbers, ratio, otherwise drop
"""
