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


def can_make_true(value: int, operands: list[int]) -> bool:
    if len(operands) == 1:
        return value == operands[0]
    
    a, b = operands[0:2]

    if a * b <= value:
        if can_make_true(value, [a * b] + operands[2:]):
            return True
    
    if a + b <= value:
        return can_make_true(value, [a + b] + operands[2:])


result = 0
for line in lines:
    value, operands = line.split(':')
    value = int(value)
    operands = [int(x) for x in operands.split()]

    if can_make_true(value, operands):
        result += value

print('Part 1:', result)
