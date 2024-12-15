with open("input-15.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

ROBOT, BOX, WALL, EMPTY, BOX_L, BOX_R = "@O#.[]"
N,E,S,W = "^>v<"
X, Y = 0, 1

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
# # Example answer for part 2 = 9021


def parse(input: list[str]) -> tuple[list[list[str]], tuple[int,int], str]:
    i_sep = input.index('')
    map = [list(s) for s in input[:i_sep]]
    movements = ''.join(input[i_sep+1:])
    return (map, get_robot_pos(map), movements)

def get_robot_pos(map: list[list[str]]) -> tuple[int,int]:
    for y in range(len(map)):
        if ROBOT in map[y]:
            return (map[y].index(ROBOT), y)

def widen(map: list[list[str]]) -> list[list[str]]:
    wider = {
        WALL: WALL + WALL,
        BOX: BOX_L + BOX_R,
        EMPTY: EMPTY + EMPTY,
        ROBOT: ROBOT + EMPTY,
    }

    return [list(''.join([wider[s] for s in row])) for row in map]

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

    # move to empty square:
    if map[ny][nx] == EMPTY:
        map[ny][nx] = ROBOT
        map[sy][sx] = EMPTY
        pos = (nx, ny)
    elif map[ny][nx] == BOX:
        while map[y][x] == BOX:
            x, y = next_pos((x, y), dir)
        # move and push boxes
        if map[y][x] == EMPTY:
            map[sy][sx] = EMPTY
            map[ny][nx] = ROBOT
            map[y][x] = BOX
            pos = (nx, ny)
    elif map[ny][nx] in [BOX_L, BOX_R]:
        cells_to_move = [pos]
        for cell in cells_to_move:
            nx, ny = next_pos(cell, dir)
            if map[ny][nx] == WALL:
                cells_to_move.append((nx, ny))
                break
            elif map[ny][nx] in [BOX_L, BOX_R]:
                box_cells = [(nx, ny)]
                if dir in [N, S]:
                    if map[ny][nx] == BOX_L: box_cells.append((nx+1, ny))
                    else: box_cells.append((nx-1, ny))
                cells_to_move.extend([c for c in box_cells if c not in cells_to_move])

        cell = cells_to_move[-1]
        if map[cell[Y]][cell[X]] != WALL:
            for cx, cy in reversed(cells_to_move):
                nx, ny = next_pos((cx, cy), dir)
                map[ny][nx] = map[cy][cx]
                map[cy][cx] = EMPTY
            pos = (nx, ny)

    return map, pos

def sum_box_coords(map: list[str]) -> int:
    coords = []
    for row in range(len(map)):
        for col in [i for i in range(len(map[row])) if map[row][i] in [BOX, BOX_L]]:
            coords.append(100*row + col)
    return sum(coords)

def print_map(map: list[list[str]], dir: str = None) -> None:
    print(dir)
    for row in map:
        print(''.join(row))


map, pos, movements = parse(lines)

for move in movements:
    map, pos = move_robot(map, pos, move)

answer = sum_box_coords(map)

print('Part 1:', answer)

map, pos, movements = parse(lines)
map = widen(map)
pos = get_robot_pos(map)

# print_map(map)
for move in movements:
    map, pos = move_robot(map, pos, move)
    # print_map(map, move)

answer = sum_box_coords(map)

print('Part 2:', answer)
