import aoc

START, END, EMPTY, WALL = "SE.#"
MIN_CHEAT = 100
input = aoc.read_file_lines("input-20.txt")

# input = aoc.read_lines("""
# ###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############
# """)
# MIN_CHEAT = 0
# # Example answer for part 1 = 44


sx, sy = aoc.get_pos_in_input(START, input)
ex, ey = aoc.get_pos_in_input(END, input)

cheats = []
for cx,cy in [(x,y) for x in range(1, len(input[0])-1) for y in range(1, len(input)-1)]:
    if input[cy][cx] == WALL:
        if len([1
                for dx,dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]
                if input[cy+dy][cx+dx] != WALL]) >= 2:
            cheats.append((cx,cy))

benchmark = aoc.shortest_path_len(input, (sx, sy), (ex, ey))

worthy_cheats = []
map = [list(row) for row in input]
for cx,cy in cheats:
    map[cy][cx] = EMPTY
    path_len = aoc.shortest_path_len(map, (sx, sy), (ex, ey))
    if path_len <= benchmark - MIN_CHEAT:
        print(cx,cy, benchmark - path_len)
        worthy_cheats.append((cx,cy))
    map[cy][cx] = WALL

print('Part 1:', len(worthy_cheats))
