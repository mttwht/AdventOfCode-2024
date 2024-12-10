with open("input-10.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# """.splitlines()][1:]
# # Example answer for part 1 = 36


def find_peaks(map: list[str], pos: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = pos
    if map[y][x] == '9':
        return set([pos])
    
    peaks = set()
    neighbours = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
    for xx, yy in [(xxx, yyy) for (xxx, yyy) in neighbours if 0 <= xxx < len(map[y]) and 0 <= yyy < len(map)]:
        if int(map[yy][xx]) == int(map[y][x]) + 1:
            peaks.update(find_peaks(map, (xx, yy)))
    
    return list(peaks)


total_score = 0
for y in range(len(lines)):
    for x in [x for x in range(len(lines[y])) if lines[y][x] == '0']:
        peaks = find_peaks(lines, (x, y))
        score = len(peaks)
        total_score += score

print('Part 1:', total_score)
