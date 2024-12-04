with open("input-04.txt", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]

# lines = [list(line.strip()) for line in """
# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# """.splitlines()][1:]
# # Example answer  = 4

# lines = [list(line.strip()) for line in """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """.splitlines()][1:]
# # Example answer  = 18

def rotate_90_clockwise(grid: list[list]) -> list[list]:
    return list(zip(*grid[::-1]))

def rotate_45_collapsed(grid: list[list]) -> list[list]:
    starts = [(0, y) for y in range(len(grid))] + [(x, len(grid)-1) for x in range(1, len(grid[0]))]
    rows = []
    for x, y in starts:
        line = ''
        while x < len(grid[0]) and y >= 0:
            line += grid[y][x]
            x += 1
            y -= 1
        rows.append(list(line))
    return rows

def word_search(grid: list[list], target: str) -> int:
    lines = [''.join(row) for row in grid]
    lines += [''.join(row) for row in rotate_45_collapsed(grid)]
    for i in range(3):
        grid = rotate_90_clockwise(grid)
        lines += [''.join(row) for row in grid]
        lines += [''.join(row) for row in rotate_45_collapsed(grid)]
    return sum([line.count(target) for line in lines])

def print_lines(lines: list[list]) -> None:
    for line in lines:
        print(''.join(line))
    print()

xmas_count = word_search(lines, 'XMAS')
print(xmas_count)
