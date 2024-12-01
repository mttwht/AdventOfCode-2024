with open("input-01.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# """.splitlines()][1:]
# # Example answer  = 11


def parse_input(lines):
    left, right = [], []
    for i in range(len(lines)):
        l, r = lines[i].split()
        left.append(int(l))
        right.append(int(r))
    return left, right

left, right = parse_input(lines)
total_dist = 0
left.sort()
right.sort()
for i in range(len(left)):
    dist = abs(right[i] - left[i])
    total_dist += dist

print(total_dist)
