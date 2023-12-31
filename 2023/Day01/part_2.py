from aoc_utilities.input_handling import TxtInput

targets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

conversions = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def make_int(x):
    if x.isdigit():
        return int(x)
    else:
        return conversions[x]


def extract_integers(line) -> list[int]:
    # Find all the targets in the line
    hits = []
    for target in targets:
        start = 0
        # This is annoying and expensive, but targets may be repeated in the line
        while True:
            pos = line.find(target, start)
            if pos == -1:
                break
            hits.append((pos, target))
            start = pos + 1
    # Sort the hits and return first and last
    sorted_hits = sorted(hits, key=lambda x: x[0])
    print(f"Hits: {sorted_hits}")
    filtered_hits = [make_int(sorted_hits[0][1]), make_int(sorted_hits[-1][1])]
    print(f"Filtered hits: {filtered_hits}")
    return filtered_hits


def create_calibration_value(numbers: list) -> int:
    if len(numbers) == 1:
        return numbers[0]
    else:
        return int(f"{numbers[0]}{numbers[-1]}")


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    total = 0
    for line in lines:
        print("--------------------")
        print(f"Line: {line}")
        numbers = extract_integers(line)
        calibration_value = create_calibration_value(numbers)
        print(f"Calibration Value: {calibration_value}")
        total += calibration_value

    print(f"--------------------------- \n\n"
          f"The solution is: {total}")
