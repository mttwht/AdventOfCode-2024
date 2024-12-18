import re

import aoc


input = aoc.read_file_lines("input-17.txt")

# input = aoc.read_lines("""
# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0
# """)
# # Example answer for part 1 = 4,6,3,5,6,3,5,2,1,0


def parse(input: list[str]) -> tuple[dict[str,int], list[int]]:
    state, instructions = {}, []
    for line in input:
        if re.match("Register", line):
            match = re.match("Register (\w): (\d+)", line)
            state[match[1]] = int(match[2])
        elif re.match("Program", line):
            match = re.match("Program: (.+)", line)
            instructions = [int(x) for x in match[1].split(',')]
    return state, instructions

def combo(operand: int, state: dict[str,int]) -> int:
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return state['A']
    elif operand == 5:
        return state['B']
    elif operand == 6:
        return state['C']
    else:
        raise Exception(f"Invalid combo operand {operand}")

state, instructions = parse(input)
output = []

i = 0
while i < len(instructions):
    instruction, operand = instructions[i:i+2]
    if instruction == 0: # adv
        state['A'] = int(state['A'] / pow(2, combo(operand, state)))
    elif instruction == 1: # bxl
        state['B'] = state['B'] ^ operand
    elif instruction == 2: # bst
        state['B'] = combo(operand, state) % 8
    elif instruction == 3: # jnz
        if state['A'] != 0:
            i = operand - 2
    elif instruction == 4: # bxc
        state['B'] = state['B'] ^ state['C']
    elif instruction == 5: # out
        output.append(combo(operand, state) % 8)
    elif instruction == 6: # bdv
        state['B'] = int(state['A'] / pow(2, combo(operand, state)))
    elif instruction == 7: # cdv
        state['C'] = int(state['A'] / pow(2, combo(operand, state)))
    
    i += 2

print(','.join([str(o) for o in output]))
