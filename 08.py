with open("input-08.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............
# """.splitlines()][1:]
# # Example answer for part 1 = 14
# # Example answer for part 2 = 34


def find_antennas(map: list[str]) -> dict[chr, list[tuple[int, int]]]:
    antennas = {}
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == '.':
                continue
            if map[row][col] not in antennas:
                antennas[map[row][col]] = []
            antennas[map[row][col]].append((row, col))
    return antennas

def find_antinodes(antennas: dict[chr, list[tuple[int, int]]], map_height: int, map_width: int) -> dict[chr, list[tuple[int, int]]]:
    antinodes = {}
    for freq, locs in antennas.items():
        antinodes[freq] = []
        for loc1 in locs[:-1]:
            for loc2 in locs[locs.index(loc1)+1:]:
                dr, dc = (loc2[0] - loc1[0]), (loc2[1] - loc1[1])
                node1 = (loc1[0] - dr, loc1[1] - dc)
                node2 = (loc2[0] + dr, loc2[1] + dc)
                if 0 <= node1[0] < map_height and 0 <= node1[1] < map_width:
                    antinodes[freq].append(node1)
                if 0 <= node2[0] < map_height and 0 <= node2[1] < map_width:
                    antinodes[freq].append(node2)
    return antinodes

def find_harmonic_antinodes(antennas: dict[chr, list[tuple[int, int]]], map_height: int, map_width: int) -> dict[chr, list[tuple[int, int]]]:
    antinodes = {}
    for freq, locs in antennas.items():
        antinodes[freq] = []
        for loc1 in locs[:-1]:
            for loc2 in locs[locs.index(loc1)+1:]:
                dr, dc = (loc2[0] - loc1[0]), (loc2[1] - loc1[1])
                node = loc1
                while 0 <= node[0] < map_height and 0 <= node[1] < map_width:
                    antinodes[freq].append(node)
                    node = (node[0] - dr, node[1] - dc)
                node = loc2
                while 0 <= node[0] < map_height and 0 <= node[1] < map_width:
                    antinodes[freq].append(node)
                    node = (node[0] + dr, node[1] + dc)
    return antinodes

def find_distinct_antinodes(antinodes: dict[chr, list[tuple[int, int]]]) -> set[tuple[int, int]]:
    nodes = set()
    for locs in antinodes.values():
        nodes.update(locs)
    return nodes

antennas = find_antennas(lines)
antinodes = find_antinodes(antennas, len(lines), len(lines[0]))
distinct_antinodes = find_distinct_antinodes(antinodes)

print('Part 1:', len(distinct_antinodes))

harmonic_antinodes = find_harmonic_antinodes(antennas, len(lines), len(lines[0]))
distinct_antinodes = find_distinct_antinodes(harmonic_antinodes)

print('Part 2:', len(distinct_antinodes))
