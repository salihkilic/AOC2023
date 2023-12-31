from aoc_utilities.input_handling import TxtInput


class Game:
    def __init__(self):
        self.id = None
        self.max_red = 0
        self.max_green = 0
        self.max_blue = 0

    def __repr__(self):
        return (f'Game(id={self.id}, '
                f'max_red={self.max_red}, '
                f'max_green={self.max_green}, '
                f'max_blue={self.max_blue})')

    def load_from_string(self, line):
        # Extract the game id
        game_info = line.split(':')
        self.id = int(game_info[0].split()[1])

        subset = game_info[1].split(';')
        # Go over subsets
        for subset in subset:
            self.set_max_colour(subset)

    def set_max_colour(self, subset):
        colour_data = subset.split(',')
        for colour in colour_data:
            colour = colour.strip()
            colour_name = colour.split()[1]
            colour_value = int(colour.split()[0])
            if colour_name == 'red' and colour_value > self.max_red:
                self.max_red = colour_value
            elif colour_name == 'green' and colour_value > self.max_green:
                self.max_green = colour_value
            elif colour_name == 'blue' and colour_value > self.max_blue:
                self.max_blue = colour_value
            elif colour_name not in ['red', 'green', 'blue']:
                raise ValueError(f'Unknown colour: {colour_name}')

    def is_possible(self, red: int, green: int, blue: int):
        return self.max_red <= red and self.max_green <= green and self.max_blue <= blue


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    possible_games = []
    for line in lines:
        game = Game()
        game.load_from_string(line)
        print("-----------------")
        if game.is_possible(12, 13, 14):
            print(game)
            print(f"Game {game.id} is possible")
            possible_games.append(game)
        else:
            print(game)
            print(f"Game {game.id} is not possible")

    total = 0
    for game in possible_games:
        total += game.id

    print(f"\n-----------------\n"
          f"The total is: {total}")
