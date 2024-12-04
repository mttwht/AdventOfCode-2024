with open("input-04.txt", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]

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
# # Example answer  = 9


def word_search(grid: list[list]) -> int:
    count = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[y])-1):
            if(grid[y][x] == 'A'):
                nw, ne, se, sw = grid[y-1][x-1], grid[y-1][x+1], grid[y+1][x+1], grid[y+1][x-1]
                if nw + se in ['MS', 'SM'] and ne + sw in ['MS', 'SM']:
                    count += 1
    return count

x_mas_count = word_search(lines)
print(x_mas_count)
