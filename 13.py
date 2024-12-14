import re

with open("input-13.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
# """.splitlines()][1:]
# # Example answer for part 1 = 480


A_COST, B_COST = 3, 1


def parse_input(lines: list[str]):
    machines = []
    machine = []
    for line in lines:
        if line.startswith('Button'):
            machine.append([int(x) for x in re.findall(r'\+(\d+)', line)])
        elif line.startswith('Prize'):
            machine.append([int(x) for x in re.findall(r'=(\d+)', line)])
        else:
            machines.append(machine)
            machine = []
    machines.append(machine)
    return machines

def solve(machine: list[tuple[int, int]]) -> tuple[int, int]:
    (ax, ay), (bx, by), (px, py) = machine
    min_cost = None
    solution = None
    for a in range(101):
        if (px - a * ax) % bx == 0 and (py - a * ay) % by == 0 and (px - a * ax) / bx == (py - a * ay) / by:
            b = int((px - a * ax) / bx)
            if b <= 100:
                if min_cost is None or (a * A_COST + b * B_COST) < min_cost:
                    solution = (a, b)
    return solution


machines = parse_input(lines)

winning_presses = []
for machine in machines:
    presses = solve(machine)
    if presses is not None:
        winning_presses.append(presses)

prizes = len(winning_presses)
cost = sum([a * A_COST + b * B_COST for (a, b) in winning_presses])
print(prizes, 'prizes for', cost, 'tokens')
