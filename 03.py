import re

with open("input-03.txt", "r") as file:
    line = file.read().strip()

# line = """
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# """.strip()
# # Example answer  = 48


result = 0

line = re.sub(r'don\'t\(\).*?do\(\)', '', line, flags=re.S)
line = re.sub(r'don\'t\(\).*?$', '', line)

for x, y in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line):
    result += int(x) * int(y)

print(result)
