from aoc_utilities.input_handling import TxtInput


def find_destination(mapping, original_location):
    for map in mapping:
        if int(map[1]) <= int(original_location) <= int(map[1]) + (int(map[2]) - 1):
            print(f"found {original_location} in {map}")
            return str(int(map[0]) + (int(original_location) - int(map[1])))
    print(f"Did not find {original_location} in mappings, location remains: {original_location}")
    return original_location


def parse_mapping_data(lines) -> dict:
    data = {}
    current_section = None
    for line in lines:
        line = line.strip()
        if line.endswith('map:'):
            current_section = line[:-5]
            data[current_section] = []
        elif line and current_section:
            numbers = [int(num) for num in line.split()]
            data[current_section].append(numbers)
        elif line.startswith("seeds:"):
            data['seeds'] = [int(num) for num in line.split(":")[1].split()]
    """
    data['seeds'] is a list of numbers that represent one seed each
    seed = data['seeds'][x] is the seed number
    x = data['somemap'][0] is destination range start
    y = data['somemap'][1] is source range start
    z = data['somemap'][2] is the range length
    """
    return data


def main(lines):
    mappings = parse_mapping_data(lines)
    seeds = mappings['seeds']
    map_order = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light',
                 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

    end_destinations = []
    for seed in seeds:
        print(f"Checking seed: --- {seed} ---")
        destination = seed
        for map_name in map_order:
            print(f"Checking map: {map_name}")
            destination = find_destination(mappings[map_name], destination)
            print(f"Destination: {destination}")
        print(f"Final destination for {seed}: {destination}")
        end_destinations.append(destination)
        print("-------------------")

    end_destinations = [int(num) for num in end_destinations]
    end_destinations.sort(reverse=True)
    print("Final destinations (sorted):")
    for destination in end_destinations:
        print(destination)
    return min(end_destinations)


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    print(f"\nSolution: {main(lines)}")
