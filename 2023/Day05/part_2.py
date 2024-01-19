from aoc_utilities.input_handling import TxtInput

"""
Man, I needed some hints on this one. Very hard.
"""

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
    return data


def main(lines):
    mappings = parse_mapping_data(lines)
    origins = [(range_low, range_low + range_high) for range_low, range_high in
               zip(mappings['seeds'][::2], mappings['seeds'][1::2])]
    blocks = [mappings[block] for block in mappings.keys() if block != 'seeds']

    for block in blocks:
        valid_ranges = []
        while len(origins) > 0:
            seed_start, seed_end = origins.pop()
            for source_start, destination_start, offset in block:
                intersection_start = max(seed_start, destination_start)
                intersection_end = min(seed_end, destination_start + offset)
                # Only if there is an overlap we go on
                if intersection_start < intersection_end:
                    valid_ranges.append((intersection_start - destination_start + source_start,
                                         intersection_end - destination_start + source_start))
                    if intersection_start > seed_start:
                        origins.append((seed_start, intersection_start))
                    if seed_end > intersection_end:
                        origins.append((intersection_end, seed_end))
                    break
            else:
                valid_ranges.append((seed_start, seed_end))
        origins = valid_ranges

    print("Found the following valid ranges:")
    for origin in sorted(origins, reverse=True):
        print(origin)

    return sorted(origins)[0][0]


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    print(f"\nSolution (lowest location number): {main(lines)}")
