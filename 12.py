with open("input-12.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# AAAA
# BBCD
# BBCC
# EEEC
# """.splitlines()][1:]
# # Example answer for part 1 = 140
# # Example answer for part 2 = 80

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
# # Example answer for part 2 = 1206


def is_in_grid(lines: list[str], row: int, col: int) -> bool:
    return 0 <= row < len(lines) and 0 <= col < len(lines[row])

def get_all_neighbours(row: int, col: int) -> list[tuple[int, int]]:
    return [
        (r,c)
        for r,c in [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]
    ]

def get_neighbours(lines: list[str], row: int, col: int) -> list[tuple[int, int]]:
    return [
        (r,c)
        for r,c in get_all_neighbours(row, col)
        if is_in_grid(lines, r, c)
    ]

def get_s_e_neighbours(lines: list[str], row: int, col: int) -> list[tuple[int, int]]:
    return [
        (r,c)
        for r,c in [(row, col+1), (row+1, col)]
        if is_in_grid(lines, r, c)
    ]

def get_sides(edges: list[tuple[tuple[int, int], tuple[int,int]]]) -> int:
    sides = []
    while len(edges) > 0:
        side = [edges.pop()]
        for (r1, c1), (r2, c2) in side:
            if r1 != r2:
                # horizontal side:
                next_edges = [((r1, c1-1),(r2, c2-1)), ((r1, c1+1),(r2, c2+1))]
            else:
                # vertical side
                next_edges = [((r1-1, c1),(r2-1, c2)), ((r1+1, c1),(r2+1, c2))]

            for edge in [e for e in next_edges if e in edges]:
                side.append(edge)
                edges.remove(edge)
        sides.append(side)
    return sides


regions = []
all_neighbours = []
all_edges = []
for row in range(len(lines)):
    for col in range(len(lines[row])):
        for nrow, ncol in get_s_e_neighbours(lines, row, col):
            if lines[row][col] == lines[nrow][ncol]:
                all_neighbours.append(((row, col), (nrow, ncol)))
        # If cell has no neighbours in all 4 directions, add it as a region of area 1
        if lines[row][col] not in [lines[r][c] for r,c in get_neighbours(lines, row, col)]:
            regions.append((set([(row, col)]), [], [((row, col),(r, c)) for r, c in get_all_neighbours(row, col)]))
        else:
            all_edges.extend([
                ((row,col), (r,c))
                for r,c in get_all_neighbours(row, col)
                if (not is_in_grid(lines, r, c)) or lines[row][col] != lines[r][c]
            ])


while len(all_neighbours) > 0:
    pair = all_neighbours.pop()
    cells = list(pair)
    neighbours = [pair]
    edges = []
    for cell in cells:
        for pair in [p for p in all_neighbours if cell in p]:
            neighbours.append(pair)
            for p in pair:
                if p not in cells:
                    cells.append(p)
            all_neighbours.remove(pair)
        for pair in [p for p in all_edges if p[0] == cell]:
            edges.append(pair)
            all_edges.remove(pair)

    regions.append((set(cells), neighbours, edges))

total_price_a = 0
total_price_b = 0
for cells, neighbours, edges in regions:
    row, col = next(iter(cells))
    label = lines[row][col]
    area = len(cells)
    perim = area * 4 - len(neighbours) * 2
    sides = get_sides(edges)
    print(label, ':', area, 'x', perim, '=', area * perim)
    total_price_a += area * perim
    total_price_b += area * len(sides)

print('Part 1:', total_price_a)
print('Part 2:', total_price_b)
