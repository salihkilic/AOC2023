from aoc_utilities.input_handling import TxtInput


def create_cards(lines):
    cards = {}
    # Get the card numbers and winning numbers
    for line in lines:
        card, numbers = line.split(':')
        card_id = int(card.split()[1])
        numbers, winning_numbers = numbers.split("|")
        numbers = [int(number) for number in numbers.split()]
        winning_numbers = [int(number) for number in winning_numbers.split()]

        # Get the amount of winning numbers
        wins = len(set(winning_numbers) & set(numbers))

        cards[card_id] = wins
    return cards


def evaluate_card(cards, card_id):
    wins = cards[card_id]
    # If card has no winning numbers, return 0
    if wins == 0:
        return 0
    # If card has winning numbers, return amount of cards we win in the next layer, recursively
    else:
        amount_of_cards = wins
        for card_offset in range(1, wins + 1):
            amount_of_cards += evaluate_card(cards, card_id + card_offset)
        return amount_of_cards


def main(lines):
    cards = create_cards(lines)
    total_scratchcards = len(cards)

    for card_number, card_wins in cards.items():
        total_scratchcards += evaluate_card(cards, card_number)

    return total_scratchcards


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    print(f"Solution: {main(lines)}")
