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
# # Example answer  = 41


def find_start_pos(map: list[list[str]]) -> tuple[int, int]:
    for line in lines:
        if '^' in line:
            return (line.index('^'), lines.index(line))

directions = list('^>v<')
map = [list(l) for l in lines]
(x, y) = find_start_pos(map)
dir = directions[0]

while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
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

coverage = sum([row.count('X') for row in map])
print(coverage)

