from aoc_utilities.input_handling import TxtInput


def extract_integers(line) -> list[int]:
    return [int(x) for x in line if x.isdigit()]


def create_calibration_value(numbers: list) -> int:
    return int(f"{numbers[0]}{numbers[-1]}")


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    total = 0
    for line in lines:
        numbers = extract_integers(line)
        total += create_calibration_value(numbers)
    print(f"The solution is: {total}")
