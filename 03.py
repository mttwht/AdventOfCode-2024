import re

with open("input-03.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# """.splitlines()][1:]
# # Example answer  = 161


result = 0
for line in lines:
    for x, y in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line):
        result += int(x) * int(y)

print(result)
