with open("input-06.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """.splitlines()][1:]
# # Example answer for part 1 = 41
# # Example answer for part 2 = 6


def find_start_pos(map: list[list[str]]) -> tuple[int, int]:
    for line in lines:
        if '^' in line:
            return (line.index('^'), lines.index(line))

def traverse_map(map: list[list[str]], x: int, y: int, dir: str) -> list[list[str]]:
    traversed_locations = set()
    while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
        # return None if we detect a loop
        if (x, y, dir) in traversed_locations:
            return None

        traversed_locations.add((x, y, dir))
        map[y][x] = 'X'
        if dir == '^':
            x2, y2 = x, y-1
        elif dir == '>':
            x2, y2 = x+1, y
        elif dir == 'v':
            x2, y2 = x, y+1
        elif dir == '<':
            x2, y2 = x-1, y
        
        try:
            if map[y2][x2] == '#':
                dir = directions[(directions.index(dir)+1) % len(directions)]
            else:
                x, y = x2, y2
        except IndexError:
            break
    return map

def get_traversed_locations(map: list[list[str]]) -> list[tuple[int, int]]:
    locations = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'X':
                locations.append((x, y))
    return locations

def copy_map(map: list[list[str]]) -> list[list[str]]:
    return [row.copy() for row in map]


directions = list('^>v<')
map = [list(l) for l in lines]

(x, y) = find_start_pos(map)
dir = directions[0]

# Part 1
traversed_map = traverse_map(copy_map(map), x, y, dir)
traversed_positions = get_traversed_locations(traversed_map)
print('Part 1:', len(traversed_positions))

# Part 2
loop_locations = []
traversed_positions.remove((x, y))
for position in traversed_positions:
    temp_map = copy_map(map)
    (tx, ty) = position
    temp_map[ty][tx] = '#'
    if traverse_map(temp_map, x, y, dir) is None:
        loop_locations.append(position)
print('Part 2:', len(loop_locations))
