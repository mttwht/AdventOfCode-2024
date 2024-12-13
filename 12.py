with open("input-12.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# AAAA
# BBCD
# BBCC
# EEEC
# """.splitlines()][1:]
# # Example answer for part 1 = 140

# lines = [line.strip() for line in """
# OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO
# """.splitlines()][1:]
# # Example answer for part 1 = 772

# lines = [line.strip() for line in """
# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
# """.splitlines()][1:]
# # Example answer for part 1 = 1930


def get_neighbours(lines: list[str], row: int, col: int) -> list[tuple[int, int]]:
    return [
        (r,c)
        for r,c in [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]
        if 0 <= r < len(lines) and 0 <= c < len(lines[r])
    ]

def get_s_e_neighbours(lines: list[str], row: int, col: int) -> list[tuple[int, int]]:
    return [
        (r,c)
        for r,c in [(row, col+1), (row+1, col)]
        if 0 <= r < len(lines) and 0 <= c < len(lines[r])
    ]


regions = []
all_neighbours = []
for row in range(len(lines)):
    for col in range(len(lines[row])):
        for nrow, ncol in get_s_e_neighbours(lines, row, col):
            if lines[row][col] == lines[nrow][ncol]:
                all_neighbours.append(((row, col), (nrow, ncol)))
        # If cell has no neighbours in all 4 directions, add it as a region of area 1
        if lines[row][col] not in [lines[r][c] for r,c in get_neighbours(lines, row, col)]:
            regions.append((set([(row, col)]), []))

while len(all_neighbours) > 0:
    pair = all_neighbours.pop()
    cells = list(pair)
    neighbours = [pair]

    for cell in cells:
        # cell = cells[i]
        for pair in [p for p in all_neighbours if cell in p]:
            neighbours.append(pair)
            for p in pair:
                if p not in cells:
                    cells.append(p)
            all_neighbours.remove(pair)

    regions.append((set(cells), neighbours))

total_price = 0
for region in regions:
    row, col = next(iter(region[0]))
    label = lines[row][col]
    area = len(region[0])
    perim = area * 4 - len(region[1]) * 2
    print(label, ':', area, 'x', perim, '=', area * perim)
    total_price += area * perim

print('Part 1', total_price)
