import aoc

EMPTY, BYTE = ".#"
GRID_SIZE = 70
NUM_BYTES = 1024

input = aoc.read_file_lines("input-18.txt")

# input = aoc.read_lines("""
# 5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0
# """)
# GRID_SIZE = 6
# NUM_BYTES = 12
# # Example answer for part 1 = 22


def parse(input: list[str]) -> list[tuple[int, int]]:
    return [(int(x), int(y)) for x, y in [line.split(",") for line in input]]

def shortest_path_len(
    map: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int]
) -> int:
    dists = [[-1 for _ in range(len(row))] for row in map]
    (sx, sy), (ex, ey) = start, end
    dists[sy][sx] = 0
    queue = [(sx, sy)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map) and dists[ny][nx] == -1 and map[ny][nx] == EMPTY:
                dists[ny][nx] = dists[y][x] + 1
                queue.append((nx, ny))
    return dists[ey][ex]

start, end = (0,0), (GRID_SIZE, GRID_SIZE)
map = [['.' for _ in range(GRID_SIZE+1)] for _ in range(GRID_SIZE+1)]
falling_bytes = parse(input)

for x, y in falling_bytes[:NUM_BYTES]:
    map[y][x] = '#'

aoc.print_grid(map)

answer = shortest_path_len(map, start, end)
print('Part 1:', answer)
