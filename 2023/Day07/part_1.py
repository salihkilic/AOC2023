from aoc_utilities.input_handling import TxtInput

card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards: list[str] = [card for card in cards]
        self.score = self.calculate_score()
        self.highest_card = self.cards[0]
        self.bid = bid

    def __lt__(self, other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
            for index, card in enumerate(self.cards):
                if card_order.index(card) < card_order.index(other.cards[index]):
                    return False
                elif card_order.index(card) > card_order.index(other.cards[index]):
                    return True

    def __repr__(self):
        return f"\nCards:{self.cards}, Bid:{self.bid} -- Score:{self.score}"

    def calculate_score(self) -> int:
        card_set = set(self.cards)
        if len(card_set) == 1:
            return 7  # Five of a kind
        elif len(card_set) == 2:
            for card in card_set:
                if self.cards.count(card) == 4:
                    return 6  # Four of a kind
            return 5  # Full house
        elif len(card_set) == 3:
            for card in card_set:
                if self.cards.count(card) == 3:
                    return 4  # Three of a kind
            return 3  # Two pair
        elif len(card_set) == 4:
            # One pair
            return 2
        else:
            # High card
            return 1


def parse_input(lines):
    return [(hand, int(bid)) for line in lines for hand, bid in [line.split(" ")]]


def calculate_winnings(hands: list[Hand]) -> int:
    winnings = 0
    for rank, hand in enumerate(hands):
        winnings += (hand.bid * (rank + 1))
        print(f"Rank:{rank + 1}, Hand:{hand}, Winnings:{(hand.bid * (rank + 1))}")
    return winnings


def main(lines):
    hands_data = parse_input(lines)
    hands = [Hand(hand, bid) for hand, bid in hands_data]
    hands.sort()
    return calculate_winnings(hands)


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines

    print(f"Solution: {main(lines)}")
