with open("input-15.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

ROBOT, BOX, WALL, EMPTY = "@O#."
N,E,S,W = "^>v<"

# lines = [line.strip() for line in """
# ########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<
# """.splitlines()][1:]
# # Example answer for part 1 = 2028

# lines = [line.strip() for line in """
# ##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
# """.splitlines()][1:]
# # Example answer for part 1 = 10092


def parse(input: list[str]) -> tuple[list[str], tuple[int,int], str]:
    i_sep = input.index('')
    map = [list(s) for s in input[:i_sep]]
    movements = ''.join(input[i_sep+1:])
    for y in range(len(lines)):
        if ROBOT in lines[y]:
            pos = (lines[y].index(ROBOT), y)
            break
    return (map, pos, movements)

def next_pos(pos: tuple[int,int], dir: str) -> tuple[int,int]:
    x, y = pos
    if dir == N: return (x, y - 1)
    elif dir == E: return (x + 1, y)
    elif dir == S: return (x, y + 1)
    elif dir == W: return (x - 1, y)

def move_robot(map: list[str], pos: tuple[int,int], dir: str) -> tuple[list[str], tuple[int,int]]:
    sx, sy = pos # robot pos
    nx, ny = next_pos(pos, dir) # robot move pos
    x, y = nx, ny

    while map[y][x] == BOX:
        x, y = next_pos((x, y), dir)
    
    # move to empty square:
    if map[ny][nx] == EMPTY:
        map[ny][nx] = ROBOT
        map[sy][sx] = EMPTY
        pos = (nx, ny)
    # move and push boxes
    elif map[y][x] == EMPTY:
        map[sy][sx] = EMPTY
        map[ny][nx] = ROBOT
        map[y][x] = BOX
        pos = (nx, ny)
    
    return map, pos

def sum_box_coords(map: list[str]) -> int:
    coords = []
    for row in range(len(map)):
        for col in [i for i in range(len(map[row])) if map[row][i] == BOX]:
            coords.append(100*row + col)
    return sum(coords)


map, pos, movements = parse(lines)

for move in movements:
    map, pos = move_robot(map, pos, move)

answer = sum_box_coords(map)

print('Part 1:', answer)
