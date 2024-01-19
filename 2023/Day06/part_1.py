from aoc_utilities.input_handling import TxtInput

def parse_input(lines):
    times = list(map(int, lines[0].split(':')[1].split()))
    distances = list(map(int, lines[1].split(':')[1].split()))
    return list(zip(times, distances))


def iterate_from_outside_in(lst) -> tuple[str, int]:
    n = len(lst)
    for i in range(n // 2 + n % 2):
        yield ('lo', lst[i])
        if i != n - i - 1:  # Avoid double yielding the middle element if the list length is odd
            yield ('hi', lst[n - i - 1])

def calculate_distance(total_time:int, wait:int) -> int:
    """
                       time left        *   speed
    Distance is (total_time - waittime) * (waittime)
    """
    return (total_time - wait) * wait

def main(lines):
    race_data = parse_input(lines)
    # Check what the lowest and highest wins are
    total_wins = []
    for race in race_data:
        wins = []
        for time_spent_waiting in iterate_from_outside_in(range(1, race[0])):
            if calculate_distance(race[0], time_spent_waiting[1]) > race[1]:
                wins.append(time_spent_waiting[1])
        print(f"Wins in race {race}: {sorted(wins)}")
        total_wins.append(len(wins))

    # Calculate final number
    result = 1
    for num in total_wins:
        result *= num
    return result





if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    print(parse_input(lines))
    print(f"Solution: {main(lines)}")