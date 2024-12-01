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
# # Example answer  = 31

def parse_input(lines):
    left, right = [], []
    for i in range(len(lines)):
        l, r = lines[i].split()
        left.append(int(l))
        right.append(int(r))
    return left, right


left, right = parse_input(lines)
total_similarity = 0
for i in left:
    similarity = i * right.count(i)
    total_similarity += similarity

print(total_similarity)
