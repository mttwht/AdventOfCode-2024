
def read_file_lines(filename: str) -> list[str]:
    '''Read and return all lines of text from a file'''
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def read_lines(input_text: str) -> list[str]:
    lines = input_text.splitlines()
    if lines[0] == '': lines.pop(0)
    if lines[-1] == '': lines.pop()
    return [line.strip() for line in lines]

def print_grid(grid: list[list[str]]):
    for row in grid:
        if row is str:
            print(row)
        elif type(row) is list:
            print("".join(row))

def get_pos_in_input(target: str, input: list[str]) -> tuple[int, int]:
    for y, row in enumerate(input):
        if target in row:
            return (row.index(target), y)
    return None

def shortest_path_len(
    map: list[str],
    start: tuple[int, int],
    end: tuple[int, int],
    path_char: str = '.',
    wall_char: str = '#'
) -> int:
    UNKNOWN = -1
    dist_map = [[UNKNOWN for _ in range(len(map[0]))] for _ in range(len(map))]
    dist_map[start[1]][start[0]] = 0
    queue = [start]
    
    while queue:
        x, y = queue.pop(0)
        if (x, y) == end:
            return dist_map[y][x]
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(map[0]) and 0 <= new_y < len(map) and map[new_y][new_x] != wall_char and dist_map[new_y][new_x] == UNKNOWN:
                dist_map[new_y][new_x] = dist_map[y][x] + 1
                queue.append((new_x, new_y))
