from aoc_utilities.input_handling import TxtInput


def main(lines):
    score = 0
    # Get the card numbers and winning numbers
    for line in lines:
        card, numbers = line.split(':')
        numbers, winning_numbers = numbers.split("|")
        numbers = [int(number) for number in numbers.split()]
        winning_numbers = [int(number) for number in winning_numbers.split()]

        # Get the amount of winning numbers
        wins = len(set(winning_numbers) & set(numbers))
        # Calculate score
        score += 2 ** (wins - 1) if wins > 0 else 0

    return int(score)


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    print(f"Solution: {main(lines)}")
