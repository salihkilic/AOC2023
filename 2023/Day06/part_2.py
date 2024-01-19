from aoc_utilities.input_handling import TxtInput


def parse_input(lines):
    time = int(''.join(lines[0].split(':')[1].split()))
    distance = int(''.join(lines[1].split(':')[1].split()))
    return (time, distance)


def iterate_from_outside_in(lst) -> tuple[str, int]:
    # This was not necessary in the end, but I thought we'd get a stupid amount of races to calculate
    n = len(lst)
    for i in range(n // 2 + n % 2):
        yield ('lo', lst[i])
        # Avoid double yielding the middle element if the list length is odd
        if i != n - i - 1:
            yield ('hi', lst[n - i - 1])


def calculate_distance(total_time: int, wait: int) -> int:
    """
                       time left        *   speed
    Distance is (total_time - waittime) * (waittime)
    """
    return (total_time - wait) * wait


def main(lines):
    race = parse_input(lines)
    # Check what the lowest and highest wins are
    total_wins = []

    wins = []
    # We could speed this up by not checking inside outer bounds that we already know are going to win.
    # This script takes only a couple of seconds to run, so I didn't bother
    for time_spent_waiting in iterate_from_outside_in(range(1, race[0])):
        if calculate_distance(race[0], time_spent_waiting[1]) > race[1]:
            wins.append(time_spent_waiting[1])
    total_wins.append(len(wins))

    # Calculate final number
    result = 1
    for num in total_wins:
        result *= num
    return result


if __name__ == '__main__':
    print("Calculating by bruteforce... Might take a couple seconds")
    lines = TxtInput('input.txt').lines
    print(f"Solution: {main(lines)}")
