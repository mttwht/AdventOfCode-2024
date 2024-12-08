with open("input-07.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """.splitlines()][1:]
# # Example answer for part 1 = 3749
# # Example answer for part 1 = 11387


def can_make_true(value: int, operands: list[int], part2: bool = False) -> bool:
    if len(operands) == 1:
        return value == operands[0]
    
    a, b = operands[0:2]

    if a * b <= value:
        if can_make_true(value, [a * b] + operands[2:], part2):
            return True
    
    if a + b <= value:
        if can_make_true(value, [a + b] + operands[2:], part2):
            return True
    
    if part2 and (int(str(a) + str(b)) <= value):
        if can_make_true(value, [int(str(a) + str(b))] + operands[2:], part2):
            return True
    
    return False


result1 = 0
result2 = 0
for line in lines:
    value, operands = line.split(':')
    value = int(value)
    operands = [int(x) for x in operands.split()]

    if can_make_true(value, operands):
        result1 += value
    if can_make_true(value, operands, part2=True):
        result2 += value

print('Part 1:', result1)
print('Part 2:', result2)
