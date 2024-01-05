from aoc_utilities.input_handling import TxtInput

directions = [(0, -1), (0, 1), (-1, 0), (1, 0),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]


def check_neighbours(location: tuple[int, int], grid: list[str]):
    for direction in directions:
        try:
            item = grid[location[0] + direction[0]][location[1] + direction[1]]
            if not item.isdigit() and item != '.':
                return True
        except IndexError:
            pass
    return False


def main(lines):
    confirmed_numbers = []
    for y_index, line in enumerate(lines):
        current_number = ""
        confirmed = False
        for x_index, char in enumerate(line):
            if char.isdigit():
                # If char is digit, we keep going for the full number
                current_number += char
                if not confirmed:
                    confirmed = check_neighbours((y_index, x_index), lines)
            else:
                # If char is not digit, we check if we have a confirmed number
                if confirmed:
                    confirmed_numbers.append(int(current_number))
                confirmed = False
                current_number = ""
            # We need to check the last number in the line when there's no more chars
            if x_index == len(line) - 1 and confirmed:
                confirmed_numbers.append(int(current_number))

    return sum(confirmed_numbers)


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    result = main(lines)

    print(f"Solution: {result}")
